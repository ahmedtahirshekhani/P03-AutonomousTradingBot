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


def create_analyst(
    name: str,
    address: str,
    email: str,
    phone_number: str,
    password: str,
    uow: AbstractUnitOfWork,
):
    hashed_pass = str(sha256(password.encode("utf-8")).hexdigest())

    new_analyst: Analyst = Analyst(
        name=name,
        address=address,
        email=email,
        phone_number=phone_number,
        password=hashed_pass,
    )
    with uow:
        uow.analysts.add(new_analyst)


def analyst_login(
    analyst_email: str, password: str, uow: AbstractUnitOfWork
) -> LoginReturn:
    with uow:
        fetched_analyst = uow.analysts.get(analyst_email=analyst_email)
        creds: LoginReturn = fetched_analyst.login(
            email=analyst_email, password=password
        )
        return creds


def analyst_logout(analyst_email: str, uow: AbstractUnitOfWork):
    with uow:
        fetched_analyst = uow.analysts.get(analyst_email=analyst_email)
        fetched_analyst.logout()


def register_investor(
    name: str,
    address: str,
    email: str,
    phone_number: str,
    password: str,
    analyst_email: str,
    uow: AbstractUnitOfWork,
) -> Dict[str, Investor | str]:
    with uow:
        fetched_analyst = uow.analysts.get(analyst_email=analyst_email)
        return fetched_analyst.register_investor(
            name=name,
            address=address,
            email=email,
            phone_number=phone_number,
            password=password,
        )


def investor_login(investor_email: str, uow: AbstractUnitOfWork) -> LoginReturn:
    with uow:
        fetched_investor = uow.investors.get(investor_email=investor_email)
        creds: LoginReturn = fetched_investor.login()
        return creds


def investor_logout(investor_email: str, uow: AbstractUnitOfWork):
    with uow:
        fetched_investor = uow.investors.get(investor_email=investor_email)
        fetched_investor.logout()


"""
Bot module
"""


def add_bot(
    analyst_id: str,
    investor_id: str,
    state: BotState,
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
        state=state,
        trades=trades,
        assigned_model=assigned_model,
        risk_appetite=risk_appetite,
        target_return=target_return,
        duration=duration,
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


def terminate_bot(
    bot_id: str,
    uow: AbstractUnitOfWork,
):
    with uow:
        fetched_bot = uow.bots.get(bot_id)
        fetched_bot.terminate()
