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
from typing import Dict, List
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
    trades: List[Trade],
    assigned_model: int,
    risk_appetite: RiskAppetite,
    target_return: float,
    duration: datetime,
    amount:int,
    uow: AbstractUnitOfWork,
):

    new_bot = Bot(
        analyst_id=analyst_id,
        investor_id=investor_id,
        state=BotState.IDLE,
        trades=trades,
        assigned_model=assigned_model,
        risk_appetite=risk_appetite,
        target_return=target_return,
        duration=duration,
        amount=amount,
        id=str(uuid4()),
    )
    with uow:
        uow.bots.add(new_bot)


def initiate_bot_execution(
    bot_id: str,
    uow: AbstractUnitOfWork,
):
    pass
    # print(uow, "HERER UOW")
    # with uow:
    #     # print("HERE beforefb\n")
    #     fetched_bot = uow.bots.get(bot_id)
    #     # print("HERE fb\n")

    #     fetched_bot.initiate_execution()
    #     # print("HERE ie\n")

    #     uow.bots.save(fetched_bot)
    #     # print("HERE no issue")



def terminate_bot(
    bot_id: str,
    uow: AbstractUnitOfWork,
):
    pass
    # with uow:
    #     fetched_bot = uow.bots.get(bot_id)
    #     fetched_bot.terminate()
    #     uow.bots.save(fetched_bot)


# trigger bot execution after every n minutes
def handle_execution(uow: AbstractUnitOfWork):
    # get all bots in running state
    with uow:
        fetch_all_running_bots = uow.bots.get_all_running_bots()

        for bot in fetch_all_running_bots:
            # Do trade etc
            pass
        return fetch_all_running_bots
