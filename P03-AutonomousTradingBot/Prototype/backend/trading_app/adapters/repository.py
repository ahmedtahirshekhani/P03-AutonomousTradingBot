from abc import ABC, abstractmethod
from typing import List, Dict, Set
from uuid import UUID

from ..domain.model import Analyst, Investor, Bot, Trade


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


"""
Bot module
"""


class BotAbstractRepository(ABC):
    @abstractmethod
    def add(self, bot: Bot):
        pass

    @abstractmethod
    def get(self, bot_id: str) -> Bot:
        pass


class FakeBotRepository(BotAbstractRepository):
    def __init__(self):
        self.bots: Dict[str, Bot] = {}

    def add(self, bot: Bot):
        self.bots[bot.id] = bot

    def get(self, bot_id: str) -> Bot:
        return self.bots[bot_id]


class BotRepository(BotAbstractRepository):
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def add(self, bot: Bot):
        sql = """
            insert into bots (id, analyst_id, investor_id, state, assigned_model, risk_appetite, target_return, duration)
            values (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(
            sql,
            [
                bot.id,
                bot.analyst_id,
                bot.investor_id,
                bot.state,
                bot.assigned_model,
                bot.risk_appetite,
                bot.target_return,
                bot.duration,
            ],
        )

    def get(self, bot_id: str) -> Bot:
        bot_sql = """
            select id, analyst_id, investor_id, state, assigned_model, risk_appetite, target_return, duration
            from bots
            where id = %s
        """
        self.cursor.execute(bot_sql, [bot_id])
        bot_row = self.cursor.fetchone()

        trades_sql = """
            select id, stock_id, amount, buying_price, selling_price, spread, started_at, ended_at, company_name
            from trades
            where bot_id = %s
        """
        self.cursor.execute(trades_sql, [bot_id])
        trades_rows = self.cursor.fetchall()

        return Bot(
            id=bot_row[0],
            analyst_id=bot_row[1],
            investor_id=bot_row[2],
            state=bot_row[3],
            assigned_model=bot_row[4],
            risk_appetite=bot_row[5],
            target_return=bot_row[6],
            duration=bot_row[7],
            trades=[
                Trade(
                    id=r[0],
                    stock_id=r[1],
                    amount=r[2],
                    buying_price=r[3],
                    selling_price=r[4],
                    spread=r[5],
                    started_at=r[6],
                    ended_at=r[7],
                    company_name=r[8],
                )
                for r in trades_rows
            ],
        )
