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
            insert into analysts (id, name, address, email, phone_number, hashed_password)
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
            select id, name, address, email, phone_number, hashed_password
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
            set name=%s, address=%s, email=%s, phone_number=%s, hashed_password=%s
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
            insert into investors (id, name, address, email, phone_number, hashed_password, ntn_number)
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
                investor.ntn_number,
            ],
        )

    def get(self, investor_email: str) -> Investor:
        sql = """
            select id, name, address, email, phone_number, hashed_password, ntn_number
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
                ntn_number=row[6]
            )

    def get_all(self) -> List[Investor]:
        sql = """
            select id, name, address, email, phone_number, hashed_password, ntn_number
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
                    ntn_number=row[6]
                )
                for row in rows
            ]

    def save(self, investor: Investor):
        sql = """
            update investors
            set name=%s, address=%s, email=%s, phone_number=%s, hashed_password=%s, ntn_number=%s
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
                investor.ntn_number,
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

    # TODO: add new trades here and on save also
    def add(self, bot: Bot):
        sql = """
            insert into bots (id, analyst_id, investor_id, stocks_ticker, initial_balance, current_balance, target_return, risk_appetite, in_trade, state, prices, start_time, end_time, assigned_model)
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        self.cursor.execute(
            sql,
            [
                bot.id,
                bot.analyst_id,
                bot.investor_id,
                bot.stocks_ticker,
                bot.initial_balance,
                bot.current_balance,
                bot.target_return,
                bot.risk_appetite.name,
                bot.in_trade,
                bot.state.name,
                bot.prices,
                bot.start_time,
                bot.end_time,
                bot.assigned_model,
            ],
        )

    def get(self, bot_id: str) -> Bot:
        bot_sql = """
            select id, analyst_id, investor_id, stocks_ticker, initial_balance, current_balance, target_return, risk_appetite, in_trade, state, prices, start_time, end_time, assigned_model
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
            stocks_ticker = bot_row[3],
            initial_balance = bot_row[4],
            current_balance = bot_row[5],
            target_return=bot_row[6],
            risk_appetite=bot_row[7],
            in_trade=bot_row[8],
            state=bot_row[9],
            prices = bot_row[10],
            start_time=bot_row[11],
            end_time=bot_row[12],
            assigned_model=bot_row[13],
            trades=[
                Trade(
                    id=r[0],
                    amount=r[2],
                    start_price=r[3],
                    started_at=r[4],
                    trade_type=r[5],
                    ended_at=r[6],
                    end_price=r[7],
                    is_profit=r[8],
                )
                for r in trades_rows
                if r[1] == bot_row[1]
            ]
        )

    def save(self, bot: Bot):
        sql = """
            update bots
            set analyst_id=%s, investor_id=%s, stocks_ticker=%s, initial_balance=%s, current_balance=%s, target_return=%s, risk_appetite=%s, in_trade=%s, state=%s, prices=%s, start_time=%s, end_time=%s, assigned_model=%s
            where id=%s
        """
        finalState = bot.state.name
        self.cursor.execute(
            sql,
            [
                bot.analyst_id,
                bot.investor_id,
                bot.stocks_ticker,
                bot.initial_balance,
                bot.current_balance,
                bot.target_return,
                bot.risk_appetite.name,
                bot.in_trade,
                finalState,
                bot.prices,
                bot.start_time,
                bot.end_time,
                bot.assigned_model,
                bot.id,
            ],

        )

    def get_all_running_bots(self) -> List[Bot]:
        bot_sql = """
            select id, analyst_id, investor_id, stocks_ticker, initial_balance, current_balance, target_return, risk_appetite, in_trade, state, prices, start_time, end_time, assigned_model
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
            stocks_ticker = bot_row[3],
            initial_balance = bot_row[4],
            current_balance = bot_row[5],
            target_return=bot_row[6],
            risk_appetite=bot_row[7],
            in_trade=bot_row[8],
            state=bot_row[9],
            prices = bot_row[10],
            start_time=bot_row[11],
            end_time=bot_row[12],
            assigned_model=bot_row[13],
            trades=[
                Trade(
                     id=r[0],
                    amount=r[2],
                    start_price=r[3],
                    started_at=r[4],
                    trade_type=r[5],
                    ended_at=r[6],
                    end_price=r[7],
                    is_profit=r[8],
                )
                for r in trades
                if r[1] == bot_row[1]
            ]
            )
            ret.append(new_bot)

        return ret
