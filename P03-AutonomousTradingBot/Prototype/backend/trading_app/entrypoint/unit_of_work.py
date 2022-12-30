import psycopg2

from abc import ABC, abstractmethod
from ..adapters.repository import (
    AnalystRepository,
    FakeAnalystRepository,
    InvestorRepository,
    FakeInvestorRepository,
    BotRepository,
    FakeBotRepository,
)

import os
from dotenv import load_dotenv
load_dotenv()


class AbstractUnitOfWork(ABC):
    analysts: AnalystRepository
    investors: InvestorRepository
    bots: BotRepository

    def __enter__(self) -> "AbstractUnitOfWork":
        return self

    def __exit__(self, *args):
        self.commit()
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        super().__init__()
        self.analysts = FakeAnalystRepository()
        self.investors = FakeInvestorRepository()
        self.bots = FakeBotRepository()

    def commit(self):
        pass

    def rollback(self):
        pass


class UnitOfWork(AbstractUnitOfWork):
    def __enter__(self):
        # self.connection = psycopg2.connect(
        #     host="ec2-52-1-17-228.compute-1.amazonaws.com",
        #     database="d6n032iomt2j2b",
        #     user="wtnfvochnbjkxy",
        #     password="161aace1eb2a7e56721ca628d0950ec8b41f3b8f348acdb877d3ee5829ff8de4",
        # )

        self.connection = psycopg2.connect(
            host=os.environ.get("DB_HOST"),
            database=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            port=os.environ.get("DB_PORT")
        )

        self.cursor = self.connection.cursor()

        self.analysts = AnalystRepository(self.connection)
        self.investors = InvestorRepository(self.connection)
        self.bots = BotRepository(self.connection)

        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.connection.close()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()
