from .unit_of_work import AbstractUnitOfWork
from ..domain.model import Analyst, LoginReturn, Investor
from hashlib import sha256

from typing import Dict


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
