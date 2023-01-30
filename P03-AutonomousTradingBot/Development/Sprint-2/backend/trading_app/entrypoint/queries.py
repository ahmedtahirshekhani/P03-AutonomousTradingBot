from .unit_of_work import UnitOfWork
from ..domain.model import Bot, Analyst

import numpy as np
import pandas as pd
import keras
from sklearn.preprocessing import MinMaxScaler

import requests
import os

def get_analyst(analyst_email: str, uow: UnitOfWork) -> Analyst:
    with uow:
        fetched_analyst = uow.analysts.get(analyst_email=analyst_email)
        return fetched_analyst


def view_all_bots(analyst_id: str, investor_id: str, uow: UnitOfWork):
    print("inside view all bots query")
    sql = """ 
        select * from bots where analyst_id = %s and investor_id = %s
    """
    with uow:
        uow.cursor.execute(sql, [analyst_id, investor_id])
        bots = uow.cursor.fetchall()
        retArr = []
        for bot in bots:
            retArr.append(
                Bot(
                    id=bot[0],
                    analyst_id=bot[1],
                    investor_id=bot[2],
                    state=bot[3],
                    assigned_model=bot[4],
                    risk_appetite=bot[5],
                    target_return=bot[6],
                    duration=bot[7],
                )
            )
        return retArr


def get_all_investors(uow: UnitOfWork):
    with uow:
        investors = uow.investors.get_all()
        return investors


"""
Polygon APIs
"""


def get_stock_details(stocks):
    stockDetails = {}
    polygon_base_api = "https://api.polygon.io/v3/reference/tickers/"
    for stock in stocks:
        polygon_api = (
            polygon_base_api + stock + "?apiKey=" + os.environ.get("POLYGON_API_KEY")
        )
        response = requests.get(polygon_api)
        stockDetails[stock] = response.json()
    return stockDetails

def get_last_close_price(stock_ticker: str, timestamp: int):
    polygon_api = f"https://api.polygon.io/v2/aggs/ticker/{stock_ticker}/range/1/hour/{timestamp}/{timestamp}?adjusted=true&sort=asc&limit=120&apiKey={os.environ.get('POLYGON_API_KEY')}"
    response = requests.get(polygon_api)
    res = response.json()
    return res.results[-1].c, res.results[-1].t

"""
ML Module APIs
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
