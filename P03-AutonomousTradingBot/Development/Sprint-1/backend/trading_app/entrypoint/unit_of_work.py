import psycopg2

from abc import ABC, abstractmethod
from ..adapters.repository import (
    AnalystAbstractRepository,
    AnalystRepository,
    FakeAnalystRepository,
    InvestorAbstractRepository,
    InvestorRepository,
    FakeInvestorRepository,
    BotAbstractRepository,
    BotRepository,
    FakeBotRepository,
)

import os
from dotenv import load_dotenv

load_dotenv()


class AbstractUnitOfWork(ABC):
    analysts: AnalystAbstractRepository
    investors: InvestorAbstractRepository
    bots: BotAbstractRepository

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
        self.connection = psycopg2.connect(
            host=os.environ.get("DB_HOST"),
            database=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            port=os.environ.get("DB_PORT"),
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
