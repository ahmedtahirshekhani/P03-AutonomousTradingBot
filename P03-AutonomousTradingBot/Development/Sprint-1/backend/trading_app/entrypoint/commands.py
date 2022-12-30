from .unit_of_work import AbstractUnitOfWork
from ..domain.model import (
    Analyst,
    LoginReturn,
    Investor,
    Bot,
    Trade,
    BotState,
    RiskAppetite,
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
    # check if analyst exists
    with uow:
        try:
            uow.analysts.get(analyst_email=email)
            raise Exception("Analyst already exists!")
        except Exception as e:
            pass

        hashed_pass = str(sha256(password.encode("utf-8")).hexdigest())

        new_analyst: Analyst = Analyst(
            name=name,
            address=address,
            email=email,
            phone_number=phone_number,
            password=hashed_pass,
        )
        uow.analysts.add(new_analyst)


def analyst_login(
    analyst_email: str, password: str, uow: AbstractUnitOfWork
) -> LoginReturn:
    with uow:

            
        try:
            fetched_analyst = uow.analysts.get(analyst_email=analyst_email)
            creds: LoginReturn = fetched_analyst.login(
            email=analyst_email, password=password
            )
        except Exception as e:
            raise e
        uow.analysts.save(fetched_analyst)
        return creds


def analyst_logout(analyst_email: str, uow: AbstractUnitOfWork):
    with uow:
        fetched_analyst = uow.analysts.get(analyst_email=analyst_email)
        fetched_analyst.logout()
        uow.analysts.save(fetched_analyst)


def get_analyst(analyst_email: str, uow: AbstractUnitOfWork) -> Analyst:
    with uow:
        fetched_analyst = uow.analysts.get(analyst_email=analyst_email)
        return fetched_analyst


def register_investor(
    name: str,
    address: str,
    email: str,
    phone_number: str,
    analyst_email: str,
    uow: AbstractUnitOfWork,
) -> Dict[str, Investor | str]:
    print("In register_investor")
    with uow:
        exist_investor = uow.investors.get(investor_email=email)
        print("exist_investor: ", exist_investor)
        if exist_investor is not None:
            raise Exception("Investor already exists!")
        fetched_analyst = uow.analysts.get(analyst_email=analyst_email)
        if fetched_analyst is not None:
    
            ret = fetched_analyst.register_investor(
                name=name,
                address=address,
                email=email,
                phone_number=phone_number,
            )
            uow.investors.add(ret["investor"])
            return ret
        else:
            raise Exception("Analyst does not exist!")


def investor_login(
    investor_email: str, password: str, uow: AbstractUnitOfWork
) -> LoginReturn:
    with uow:
        fetched_investor = uow.investors.get(investor_email=investor_email)
        if fetched_investor is None:
            raise Exception("No such email exists!")
        creds: LoginReturn = fetched_investor.login(
            email=investor_email, password=password
        )
        uow.investors.save(fetched_investor)
        return creds


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
        id=str(uuid4())
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

def get_bots(analyst_id, investor_id, uow: AbstractUnitOfWork):
    with uow:
        fetched_bots = uow.bots.get_bots(analyst_id, investor_id)
        return fetched_bots
