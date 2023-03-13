from .unit_of_work import UnitOfWork
from ..domain.model import Bot, Analyst


import requests
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .mlmodelclass import TrainModel
import psx 
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


# def get_stock_details(stocks):
#     stockDetails = {}
#     polygon_base_api = "https://api.polygon.io/v3/reference/tickers/"
#     for stock in stocks:
#         polygon_api = (
#             polygon_base_api + stock + "?apiKey=" + os.environ.get("POLYGON_API_KEY")
#         )
#         response = requests.get(polygon_api)
#         stockDetails[stock] = response.json()
#     return stockDetails


def get_last_close_price(stock_ticker: str, timestamp: int):
    # check if today is a trading day
    # if not, get the last trading day
    # get the last close price from the last trading day
    # return the last close price
    day = datetime.today().weekday()
    time = datetime.today().time()
   
    if day >= 0 and day <= 4:
        timestamp = datetime.today()- relativedelta(days=1)
    if day == 5:
        timestamp = datetime.today() - relativedelta(days=2)
    if day == 6:
        timestamp = datetime.today() - relativedelta(days=3)
    if time.hour < 9 or time.hour > 16:
        timestamp = timestamp - relativedelta(days=1)

   
    datalen = 0
    while datalen == 0:
        data = psx.stocks(stock_ticker, start=timestamp, end=datetime.today())
        datalen = len(data)
        timestamp = timestamp - relativedelta(days=1)

    # get the last row of the data dataframe
    dataval = data.iloc[-1]
    print(dataval["Close"])
    
    return dataval["Close"], timestamp.timestamp()
    # polygon_api = f"https://api.polygon.io/v2/aggs/ticker/{stock_ticker}/range/1/hour/{timestamp}/{timestamp}?adjusted=true&sort=asc&apiKey={api_key}"
    # response = requests.get(polygon_api)
    # res = response.json()
    # return res.results[-1].c, res.results[-1].t



"""
ML Module APIs
"""


def predict(model, ticker):
    
    train_model = TrainModel(ticker)
    return train_model.predict(model)


