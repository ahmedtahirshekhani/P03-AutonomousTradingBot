from abc import ABC, abstractmethod
from typing import List, Dict, Set
from uuid import UUID

from ..domain.model import Analyst, Investor, Bot, Trade, BotState


class AnalystAbstractRepository(ABC):
    @abstractmethod
    def add(self, analyst: Analyst):
        pass

    @abstractmethod
    def get(self, analyst_email: str) -> Analyst:
        pass

    @abstractmethod
    def save(self, analyst: Analyst):
        pass


class FakeAnalystRepository(AnalystAbstractRepository):
    def __init__(self):
        self.analyts: Dict[str, Analyst] = {}

    def add(self, analyst: Analyst):
        self.analyts[analyst.id] = analyst

    def get(self, analyst_email: str) -> Analyst:
        for analyst in self.analyts.values():
            if analyst.email == analyst_email:
                return analyst

        raise Exception("No such email exists!")

    def save(self, analyst: Analyst):
        self.analyts[analyst.id] = analyst


class AnalystRepository(AnalystAbstractRepository):
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def add(self, analyst: Analyst):
        sql = """
            insert into analysts (id, name, address, email, phone_number, password)
            values (%s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(
            sql,
            [
                analyst.id,
                analyst.name,
                analyst.address,
                analyst.email,
                analyst.phone_number,
                analyst.hashed_password,
            ],
        )

    def get(self, analyst_email: str) -> Analyst:
        sql = """
            select id, name, address, email, phone_number, password
            from analysts
            where email = %s
        """
        self.cursor.execute(sql, [analyst_email])
        row = self.cursor.fetchone()

        if row is None:
            raise Exception("No such email exists!")
        else:
            return Analyst(
                id=row[0],
                name=row[1],
                address=row[2],
                email=row[3],
                phone_number=row[4],
                hashed_password=row[5],
            )

    def save(self, analyst: Analyst):
        sql = """
            update analysts 
            set name=%s, address=%s, email=%s, phone_number=%s, password=%s
            where id=%s
        """
        self.cursor.execute(
            sql,
            [
                analyst.name,
                analyst.address,
                analyst.email,
                analyst.phone_number,
                analyst.hashed_password,
                analyst.id,
            ],
        )


class InvestorAbstractRepository(ABC):
    @abstractmethod
    def add(self, investor: Investor):
        pass

    @abstractmethod
    def get(self, investor_email: str) -> Investor:
        pass

    @abstractmethod
    def get_all(self) -> List[Investor]:
        pass

    @abstractmethod
    def save(self, investor: Investor):
        pass


class FakeInvestorRepository(InvestorAbstractRepository):
    def __init__(self):
        self.investors: Dict[str, Investor] = {}

    def add(self, investor: Investor):
        self.investors[investor.id] = investor

    def get(self, investor_email: str) -> Investor:
        for analyst in self.investors.values():
            if analyst.email == investor_email:
                return analyst

        raise Exception("No such email exists!")

    def get_all(self) -> List[Investor]:
        return list(self.investors.values())

    def save(self, investor: Investor):
        self.investors[investor.id] = investor


class InvestorRepository(InvestorAbstractRepository):
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def add(self, investor: Investor):
        sql = """
            insert into investors (id, name, address, email, phone_number, password)
            values (%s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(
            sql,
            [
                investor.id,
                investor.name,
                investor.address,
                investor.email,
                investor.phone_number,
                investor.hashed_password,
            ],
        )

    def get(self, investor_email: str) -> Investor:
        sql = """
            select id, name, address, email, phone_number, password
            from investors
            where email = %s
        """
        self.cursor.execute(sql, [investor_email])
        row = self.cursor.fetchone()

        if row is None:
            raise Exception("Investor not found!")
        else:
            return Investor(
                id=row[0],
                name=row[1],
                address=row[2],
                email=row[3],
                phone_number=row[4],
                hashed_password=row[5],
            )

    def get_all(self) -> List[Investor]:
        sql = """
            select id, name, address, email, phone_number, password
            from investors
        """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        if len(rows) == 0:
            raise Exception("Investor not found!")
        else:
            return [
                Investor(
                    id=row[0],
                    name=row[1],
                    address=row[2],
                    email=row[3],
                    phone_number=row[4],
                    hashed_password=row[5],
                )
                for row in rows
            ]

    def save(self, investor: Investor):
        sql = """
            update investors
            set name=%s, address=%s, email=%s, phone_number=%s, password=%s
            where id=%s
        """
        self.cursor.execute(
            sql,
            [
                investor.name,
                investor.address,
                investor.email,
                investor.phone_number,
                investor.hashed_password,
                investor.id,
            ],
        )


"""
Bot module
"""


class BotAbstractRepository(ABC):
    @abstractmethod
    def add(self, bot: Bot) -> None:
        pass

    @abstractmethod
    def get(self, bot_id: str) -> Bot:
        pass

    @abstractmethod
    def save(self, bot: Bot) -> None:
        pass

    @abstractmethod
    def get_all_running_bots(self) -> List[Bot]:
        pass


class FakeBotRepository(BotAbstractRepository):
    def __init__(self):
        self.bots: Dict[str, Bot] = {}

    def add(self, bot: Bot):
        self.bots[bot.id] = bot

    def get(self, bot_id: str) -> Bot:
        return self.bots[bot_id]

    def save(self, bot: Bot):
        self.bots[bot.id] = bot

    def get_all_running_bots(self) -> List[Bot]:
        return [bot for bot in self.bots.values() if bot.state == BotState.RUNNING]


class BotRepository(BotAbstractRepository):
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def add(self, bot: Bot):
        sql = """
            insert into bots (id, analyst_id, investor_id, state, assigned_model, risk_appetite, target_return, duration)
            values (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        finalState = bot.state.name

        self.cursor.execute(
            sql,
            [
                bot.id,
                bot.analyst_id,
                bot.investor_id,
                finalState,
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
        if bot_row is None:
            raise Exception("Bot does not exist!")

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

    def save(self, bot: Bot):
        sql = """
            update bots
            set analyst_id=%s, investor_id=%s, state=%s, assigned_model=%s, risk_appetite=%s, target_return=%s, duration=%s
            where id=%s
        """
        finalState = bot.state.name
        self.cursor.execute(
            sql,
            [
                bot.analyst_id,
                bot.investor_id,
                finalState,
                bot.assigned_model,
                bot.risk_appetite,
                bot.target_return,
                bot.duration,
                bot.id,
            ],
        )

    def get_all_running_bots(self) -> List[Bot]:
        bot_sql = """
            select id, analyst_id, investor_id, state, assigned_model, risk_appetite, target_return, duration
            from bots
            where bots.state = 'RUNNING'
        """
        self.cursor.execute(bot_sql)
        bot_rows = self.cursor.fetchall()
        if len(bot_rows) == 0:
            raise Exception("No running bots found!")

        ids = [bot_row[0] for bot_row in bot_rows]

        trades_sql = """
            select id,bot_id, stock_id, amount, buying_price, selling_price, spread, started_at, ended_at, company_name
            from trades
            where bot_id in %s;
        """
        self.cursor.execute(trades_sql, [tuple(ids)])
        trades = self.cursor.fetchall()

        ret = []

        for bot_row in bot_rows:
            new_bot = Bot(
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
                        stock_id=r[2],
                        amount=r[3],
                        buying_price=r[4],
                        selling_price=r[5],
                        spread=r[6],
                        started_at=r[7],
                        ended_at=r[8],
                        company_name=r[9],
                    )
                    for r in trades
                    if r[1] == bot_row[0]
                ],
            )
            ret.append(new_bot)

        return ret
