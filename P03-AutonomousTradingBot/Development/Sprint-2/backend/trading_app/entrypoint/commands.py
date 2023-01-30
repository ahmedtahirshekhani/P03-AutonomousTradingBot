from .unit_of_work import AbstractUnitOfWork
from ..domain.model import (
    Analyst,
    Bot,
    Trade,
    BotState,
    RiskAppetite,
    RegisterInvestorReturn,
)
from hashlib import sha256
from datetime import datetime
from typing import List
from uuid import uuid4

import numpy as np
import pandas as pd
import keras
from sklearn.preprocessing import MinMaxScaler

import os
import requests


def create_analyst(
    name: str,
    address: str,
    email: str,
    phone_number: str,
    password: str,
    uow: AbstractUnitOfWork,
):
    with uow:
        exception_raised = False
        try:
            uow.analysts.get(analyst_email=email)
        except Exception as e:
            exception_raised = True

        if not exception_raised:
            raise Exception("Analyst already exists!")

        hashed_pass = str(sha256(password.encode("utf-8")).hexdigest())

        new_analyst: Analyst = Analyst(
            id=str(uuid4()),
            name=name,
            address=address,
            email=email,
            phone_number=phone_number,
            hashed_password=hashed_pass,
        )
        uow.analysts.add(new_analyst)


def analyst_login(analyst_email: str, password: str, uow: AbstractUnitOfWork) -> None:
    with uow:
        fetched_analyst = uow.analysts.get(analyst_email=analyst_email)
        fetched_analyst.login(email=analyst_email, password=password)
        uow.analysts.save(fetched_analyst)


def analyst_logout(analyst_email: str, uow: AbstractUnitOfWork):
    with uow:
        fetched_analyst = uow.analysts.get(analyst_email=analyst_email)
        fetched_analyst.logout()
        uow.analysts.save(fetched_analyst)


def register_investor(
    name: str,
    address: str,
    email: str,
    phone_number: str,
    analyst_email: str,
    uow: AbstractUnitOfWork,
) -> RegisterInvestorReturn:

    with uow:
        try:
            uow.investors.get(investor_email=email)
            raise Exception("Investor already exists!")
        except Exception as e:
            pass

        fetched_analyst = uow.analysts.get(analyst_email=analyst_email)
        ret = fetched_analyst.register_investor(
            name=name,
            address=address,
            email=email,
            phone_number=phone_number,
        )
        uow.investors.add(ret.investor)
        return ret


def investor_login(investor_email: str, password: str, uow: AbstractUnitOfWork) -> None:
    with uow:
        fetched_investor = uow.investors.get(investor_email=investor_email)
        fetched_investor.login(email=investor_email, password=password)
        uow.investors.save(fetched_investor)


def investor_logout(investor_email: str, uow: AbstractUnitOfWork):
    with uow:
        fetched_investor = uow.investors.get(investor_email=investor_email)
        fetched_investor.logout()
        uow.investors.save(fetched_investor)


"""
Bot module
"""


def add_bot(
    analyst_id: str,
    investor_id: str,
    stocks_ticker: str,
    balance: float,
    risk_appetite: RiskAppetite,
    target_return: float,
    uow: AbstractUnitOfWork,
):

    new_bot = Bot(
        id=str(uuid4()),
        analyst_id=analyst_id,
        investor_id=investor_id,
        stocks_ticker=stocks_ticker,
        initial_balance=balance,
        current_balance=balance,
        target_return=target_return,
        risk_appetite=risk_appetite,
    )
    with uow:
        uow.bots.add(new_bot)


def initiate_bot_execution(
    bot_id: str,
    uow: AbstractUnitOfWork,
):
    with uow:
        fetched_bot = uow.bots.get(bot_id)
        fetched_bot.initiate_execution()
        uow.bots.save(fetched_bot)


def terminate_bot(
    bot_id: str,
    uow: AbstractUnitOfWork,
):
    with uow:
        fetched_bot = uow.bots.get(bot_id)
        fetched_bot.terminate()
        uow.bots.save(fetched_bot)


# trigger bot execution after every n minutes
def handle_execution(uow: AbstractUnitOfWork):
    with uow:
        # get all bots in running state
        fetch_all_running_bots = uow.bots.get_all_running_bots()
        stocks_ticker_list = [b.stocks_ticker for b in fetch_all_running_bots]

        # Remove duplicate values
        stocks_ticker_list = list(set(stocks_ticker_list))
        stock_prices = {}

        # Fetch the last close price from api for all the stocks
        for stock_ticker in stocks_ticker_list:
            timestamp = datetime.now().timestamp()
            polygon_api = f"https://api.polygon.io/v2/aggs/ticker/{stock_ticker}/range/1/hour/{timestamp}/{timestamp}?adjusted=true&sort=asc&limit=120&apiKey={os.environ.get('POLYGON_API_KEY')}"
            response = requests.get(polygon_api)
            res = response.json()
            stock_prices[stock_ticker] = res.results[-1].c, res.results[-1].t

        for bot in fetch_all_running_bots:
            bot.handle_execution(
                price=stock_prices[bot.stocks_ticker][0],
                timestamp=stock_prices[bot.stocks_ticker][1],
            )

        return fetch_all_running_bots


"""
ML Module
"""


def atr_col(df):
    high_low = df["High"] - df["Low"]
    high_prev_close = np.abs(df["High"] - df["Close"].shift())
    low_prev_close = np.abs(df["Low"] - df["Close"].shift())
    atr_df = pd.concat([high_low, high_prev_close, low_prev_close], axis=1)
    true_range = np.max(atr_df, axis=1)
    atr = true_range.rolling(14).mean()
    atr_df = atr.to_frame(name="ATR")
    ndf = pd.concat([df, atr_df], axis=1)
    ndf = ndf.dropna()
    return ndf


def predict(model, csv):
    pred_model = keras.models.load_model(model)
    sc = MinMaxScaler(feature_range=(0, 1))
    df = pd.read_csv(csv)
    ndf = atr_col(df)
    pred_X = ndf.iloc[-60:, 2:].values
    pred_scaled = sc.fit_transform(pred_X)
    pred_scaled = pred_scaled.reshape(1, 60, 6)
    predicted_stock_price = pred_model.predict(pred_scaled)
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)

    Open = predicted_stock_price[:, 0][0]
    High = predicted_stock_price[:, 1][0]
    Low = predicted_stock_price[:, 2][0]
    Close = predicted_stock_price[:, 3][0]
    # Volume=predicted_stock_price[:,4][0]
    ATR = predicted_stock_price[:, 5][0]
    return Open, High, Low, Close, ATR


def getStockDetails(stocks):
    stockDetails = {}
    polygon_base_api = "https://api.polygon.io/v3/reference/tickers/"
    for stock in stocks:
        polygon_api = (
            polygon_base_api + stock + "?apiKey=" + os.environ.get("POLYGON_API_KEY")
        )
        response = requests.get(polygon_api)
        stockDetails[stock] = response.json()
    return stockDetails
