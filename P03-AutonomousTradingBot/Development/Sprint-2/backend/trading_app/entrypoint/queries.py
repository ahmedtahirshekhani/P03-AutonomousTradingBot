from .unit_of_work import UnitOfWork
from ..domain.model import Bot, Analyst


import requests
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .mlmodelclass import TrainModel

def get_analyst(analyst_email: str, uow: UnitOfWork) -> Analyst:
    with uow:
        fetched_analyst = uow.analysts.get(analyst_email=analyst_email)
        return fetched_analyst


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
Polygon APIs
"""
api_key = os.environ.get("POLYGON_API_KEY")


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
    polygon_api = f"https://api.polygon.io/v2/aggs/ticker/{stock_ticker}/range/1/hour/{timestamp}/{timestamp}?adjusted=true&sort=asc&apiKey={api_key}"
    response = requests.get(polygon_api)
    res = response.json()
    return res.results[-1].c, res.results[-1].t


def get_train_data(stock_ticker: str):
    now = datetime.today().date()
    three_month_earlier = (datetime.today() + relativedelta(months=-3)).date()
    polygon_api = f"https://api.polygon.io/v2/aggs/ticker/{stock_ticker}/range/1/hour/{three_month_earlier}/{now}?adjusted=true&sort=asc&limit=50000&apiKey={api_key}"
    response = requests.get(polygon_api)
    res = response.json()
    return res["results"]


"""
ML Module APIs
"""


# def atr_col(df):
#     high_low = df["High"] - df["Low"]
#     high_prev_close = np.abs(df["High"] - df["Close"].shift())
#     low_prev_close = np.abs(df["Low"] - df["Close"].shift())
#     atr_df = pd.concat([high_low, high_prev_close, low_prev_close], axis=1)
#     true_range = np.max(atr_df, axis=1)
#     atr = true_range.rolling(14).mean()
#     atr_df = atr.to_frame(name="ATR")
#     ndf = pd.concat([df, atr_df], axis=1)
#     ndf = ndf.dropna()
#     return ndf


def predict(model, ticker):
    
    train_model = TrainModel(ticker)
    return train_model.predict(model)


