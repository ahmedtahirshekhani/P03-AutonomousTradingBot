from abc import ABC, abstractmethod
from typing import List, Dict, Set
from uuid import UUID

from ..domain.model import Analyst, Investor


class AnalystAbstractRepository(ABC):
    @abstractmethod
    def add(self, analyst: Analyst):
        pass

    @abstractmethod
    def get(self, analyst_id: str) -> Analyst:
        pass


class FakeAnalystRepository(AnalystAbstractRepository):
    def __init__(self):
        self.analyts: Dict[str, Analyst] = {}

    def add(self, analyst: Analyst):
        self.analyts[Analyst.id] = Analyst

    def get(self, analyst_id: str) -> Analyst:
        return self.analyts[analyst_id]


class AnalystRepository(AnalystAbstractRepository):
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def add(self, analyst: Analyst):
        sql = """
            insert into analysts (id, name, address, email, phone_number, password, expiry, token)
            values (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(
            sql,
            [
                analyst.id,
                analyst.name,
                analyst.address,
                analyst.email,
                analyst.phone_number,
                analyst.password,
                analyst.expiry,
                analyst.token,
            ],
        )

    def get(self, analyst_email: str) -> Analyst:
        sql = """
            select id, name, address, email, phone_number, password, expiry, token
            from analysts
            where email = %s
        """
        self.cursor.execute(sql, [analyst_email])
        row = self.cursor.fetchone()
        return Analyst(
            id=row[0],
            name=row[1],
            address=row[2],
            email=row[3],
            phone_number=row[4],
            password=row[5],
            expiry=row[6],
            token=row[7],
        )


class InvestorAbstractRepository(ABC):
    @abstractmethod
    def add(self, investor: Investor):
        pass

    @abstractmethod
    def get(self, investor_id: str) -> Investor:
        pass


class FakeInvestorRepository(InvestorAbstractRepository):
    def __init__(self):
        self.analyts: Dict[str, Investor] = {}

    def add(self, investor: Investor):
        self.analyts[investor.id] = investor

    def get(self, investor_id: str) -> Investor:
        return self.analyts[investor_id]


class InvestorRepository(InvestorAbstractRepository):
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def add(self, investor: Investor):
        sql = """
            insert into investors (id, name, address, email, phone_number, password, expiry, token)
            values (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(
            sql,
            [
                investor.id,
                investor.name,
                investor.address,
                investor.email,
                investor.phone_number,
                investor.password,
                investor.expiry,
                investor.token,
            ],
        )

    def get(self, investor_email: str) -> Investor:
        sql = """
            select id, name, address, email, phone_number, password, expiry, token
            from investors
            where email = %s
        """
        self.cursor.execute(sql, [investor_email])
        row = self.cursor.fetchone()
        return Investor(
            id=row[0],
            name=row[1],
            address=row[2],
            email=row[3],
            phone_number=row[4],
            password=row[5],
            expiry=row[6],
            token=row[7],
        )
