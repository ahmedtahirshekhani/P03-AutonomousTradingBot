from .unit_of_work import UnitOfWork
from ..domain.model import Bot, Analyst, Investor
import os


import requests
import os
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from .mlmodelclass import TrainModel
import psx


def get_analyst(analyst_email: str, uow: UnitOfWork) -> Analyst:
    with uow:
        fetched_analyst = uow.analysts.get(analyst_email=analyst_email)
        return fetched_analyst
def get_investor(investor_email: str, uow: UnitOfWork) -> Investor:
    with uow:
        fetched_investor = uow.investors.get(investor_email=investor_email)
        print(fetched_investor)
        return fetched_investor



def investor_bots(analyst_id: str, investor_id: str, uow: UnitOfWork):
    sql = """ 
        select id, analyst_id, investor_id, stocks_ticker, initial_balance, current_balance, target_return, risk_appetite, in_trade, state, prices, start_time, end_time, assigned_model
        from bots
        where investor_id = %s
    """
    with uow:
        uow.cursor.execute(sql, [investor_id])
        bots = uow.cursor.fetchall()
        retArr = []
        for bot in bots:
            retArr.append(
                Bot(
                    id=bot[0],
                    analyst_id=bot[1],
                    investor_id=bot[2],
                    stocks_ticker=bot[3],
                    initial_balance=bot[4],
                    current_balance=bot[5],
                    target_return=bot[6],
                    risk_appetite=bot[7],
                    in_trade=bot[8],
                    state=bot[9],
                    prices=bot[10],
                    start_time=bot[11],
                    end_time=bot[12],
                    assigned_model=bot[13],
                )
            )
        return retArr


def get_bot(bot_id: str, uow: UnitOfWork) -> Bot:
    with uow:
        fetched_bot = uow.bots.get(bot_id=bot_id)

        return fetched_bot


def get_all_investors(uow: UnitOfWork):
    with uow:
        investors = uow.investors.get_all()
        return investors


"""
Stock data APIs
"""


def get_close_price(
    stock_ticker: str,
    timestamp: int = int(datetime.now().timestamp()),
):
    # check if today is a trading day
    # if not, get the last trading day
    # get the last close price from the last trading day
    # return the last close price

    current_date = datetime.fromtimestamp(timestamp)

    datalen = 0
    while datalen == 0:
        # Loop until no exception occurs
        while True:
            try:
                data = psx.stocks(
                    stock_ticker,
                    start=current_date,
                    end=current_date + relativedelta(days=1),
                )
                break
            except:
                print("Exception occured when fetching data from psx stocks")

        datalen = len(data)
        current_date = current_date - relativedelta(days=1)

    # get the last row of the data dataframe
    dataval = data.iloc[-1]
    close_price = dataval["Close"]

    print("Last close price:", close_price, current_date.timestamp())

    return close_price, int(current_date.timestamp())


def get_all_stock_tickers():
    return psx.tickers()


def get_trained_stock_tickers():

    # specify the directory path
    path = "../../../ML"

    # get all files in the directory
    files = [
        f
        for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f)) and ".h5" in f
    ]
    files = [f.replace(".h5", "") for f in files]

    return files


"""
ML Module APIs
"""


def predict(model, ticker, till=date.today()):

    train_model = TrainModel(ticker)
    return train_model.predict(model, till=till)
