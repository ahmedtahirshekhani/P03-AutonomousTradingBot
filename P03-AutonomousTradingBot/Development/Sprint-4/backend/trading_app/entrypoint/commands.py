from .unit_of_work import AbstractUnitOfWork
from ..domain.model import (
    Analyst,
    Bot,
    RiskAppetite,
    RegisterInvestorReturn,
    BotState
)
from .queries import (get_last_close_price)
from hashlib import sha256
from datetime import datetime
from typing import List
from uuid import uuid4


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
        return new_analyst

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
    ntn_number: str,
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
            ntn_number=ntn_number,
        )
        print("Investor added to analyst", ret.investor.id)
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
    risk_appetite: str,
    target_return: float,
    uow: AbstractUnitOfWork,
):

    risk_appetite = RiskAppetite[risk_appetite]

    
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

    return new_bot
def initiate_bot_execution(
    bot_id: str,
    uow: AbstractUnitOfWork,
):
    with uow:
        fetched_bot = uow.bots.get(bot_id)
        fetched_bot.risk_appetite = RiskAppetite[fetched_bot.risk_appetite]
        fetched_bot.initiate_execution()
        uow.bots.save(fetched_bot)


def terminate_bot(
    bot_id: str,
    uow: AbstractUnitOfWork,
):
    with uow:
        fetched_bot = uow.bots.get(bot_id)
        fetched_bot.risk_appetite = RiskAppetite[fetched_bot.risk_appetite]
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
            timestamp = int(datetime.now().timestamp())
           
            p, t = get_last_close_price(stock_ticker=stock_ticker, timestamp=timestamp)
            print("Price", p, "Timestamp", t)
            stock_prices[stock_ticker] = p, t

        for bot in fetch_all_running_bots:
            bot.handle_execution(
                price=stock_prices[bot.stocks_ticker][0],
                timestamp=stock_prices[bot.stocks_ticker][1],
            )
            uow.bots.save(bot)


def add_trade(
    bot_id: str,
    price: float,
    quantity: int,
    timestamp: int,
    uow: AbstractUnitOfWork,
):
    with uow:
        fetched_bot = uow.bots.get(bot_id)
        fetched_bot.add_trade(price=price, quantity=quantity, timestamp=timestamp)
        uow.bots.save(fetched_bot)