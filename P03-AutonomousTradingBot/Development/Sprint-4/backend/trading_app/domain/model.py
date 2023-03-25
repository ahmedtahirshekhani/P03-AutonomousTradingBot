import random

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict
from uuid import uuid4
from enum import Enum
from .utils import hash_password, get_random_id

INVESTOR_PASS_LEN: int = 8

"""
Use cases for Auth module
- Create a new analyst
- Analyst can log in
- Analyst can log out
- Analyst registers an investor and gets credentials for an investor
- Investor can log in
- Investor can log out

Invariants
- No two investors can have the same email
- No two analysts can have the same email

Value Objects
- LoginReturn

Aggregates
- Analyst
- Investor

Future upgrades
- Reset password for an investor by analyst
"""


@dataclass
class Investor:
    id: str
    email: str
    hashed_password: str
    name: str
    address: str
    phone_number: str
    ntn_number: str

    def login(self, email: str, password: str) -> None:
        hashed_pass = hash_password(password=password)

        if self.email == email and self.hashed_password == hashed_pass:
            return
        else:
            raise Exception("Invalid password entered!")

    def logout(self):
        pass


@dataclass(frozen=True)
class RegisterInvestorReturn:
    investor: Investor
    plain_text_password: str


@dataclass
class Analyst:
    id: str
    email: str
    hashed_password: str
    name: str
    address: str
    phone_number: str

    def login(self, email: str, password: str) -> None:
        hashed_pass = hash_password(password=password)

        if self.email == email and self.hashed_password == hashed_pass:
            return
        else:
            raise Exception("Invalid password entered!")

    def logout(self):
        pass

    def register_investor(
        self, name: str, address: str, phone_number: str, email: str, ntn_number: str
    ) -> RegisterInvestorReturn:
        password = str(uuid4())[:INVESTOR_PASS_LEN]  # Autogenerate password
    
        return RegisterInvestorReturn(
            investor=Investor(
                id=str(uuid4()),
                name=name,
                address=address,
                email=email,
                phone_number=phone_number,
                hashed_password=hash_password(password=password),
                ntn_number=ntn_number,
            ),
            plain_text_password=password,
        )


"""
Use cases for Bot
- Initiate bot execution
- Terminate bot execution

Invariants

Value Objects
- Trade

Aggregates
- Bot

Future upgrades
"""


class BotState(Enum):
    IDLE = 1
    RUNNING = 2
    FINISHED = 3
    TERMINATED = 4


class RiskAppetite(Enum):
    LOW = 1
    MID = 2
    HIGH = 3


class TradeType(Enum):
    CALL = 1
    PUT = 2


@dataclass
class Trade:
    id: str
    amount: float
    start_price: float
    started_at: datetime
    trade_type: TradeType
    ended_at: datetime = datetime.max
    end_price: float = 0
    is_profit: bool = False # Was this a profitable trade
    # buying_price: float
    # selling_price: float
    # spread: float

    def add_trade(self, trade_type: TradeType, amount: float, price: float):
        self.trade_type = trade_type
        self.amount = amount
        self.start_price = price
        self.started_at = datetime.now()
        


@dataclass
class Bot:
    id: str
    analyst_id: str
    investor_id: str
    stocks_ticker: str # Identifier of stock
    initial_balance: float
    current_balance: float
    target_return: float
    risk_appetite: RiskAppetite  # Ex: 5% / 10% / 20%

    # Default values
    in_trade: bool = False
    state: BotState = BotState.IDLE
    prices: Dict[int, float] = field(default_factory=dict)  # timestamp -> price
    trades: List[Trade] = field(default_factory=list)
    start_time: datetime = datetime.now()
    end_time: datetime = datetime.max
    assigned_model: int = 0

    def initiate_execution(self):
        self.state = BotState.RUNNING

    def terminate(self):
        self.state = BotState.TERMINATED

    def close_trade(self, timestamp: int, price: float):
        print("Closing trade")
        self.in_trade = False
        last_trade = self.trades[-1]

        last_trade.ended_at = datetime.fromtimestamp(timestamp)
        last_trade.end_price = price
        price_diff = 0
        if type(last_trade.trade_type) == str:
            last_trade.trade_type = TradeType[last_trade.trade_type]
        print("Last trade type: ", last_trade.trade_type)

        if last_trade.trade_type == TradeType.CALL:
            # convert to float

            eP = float(price)
            sP = float(last_trade.start_price)
            price_diff = (eP - sP)*1.0
            
            self.current_balance = float(self.current_balance) + price_diff
            print("Price diff: ", price_diff, "Self balance: ", self.current_balance)
        # else:
        #     eP = float(last_trade.end_price)
        #     sP = float(price)
        #     price_diff = sP - eP
        #     self.current_balance += price_diff

        if price_diff > 0:
            last_trade.is_profit = True

        last_trade.end_price = price
        last_trade.ended_at = datetime.fromtimestamp(timestamp)
        last_trade.trade_type = TradeType.PUT

        self.trades[-1] = last_trade

    def handle_execution(self, timestamp: int, price: float):
        """
        Trading Algorithm

        Fetch the last close price
        Append the price into the bot

        Check bot stopping conditions
        If met
            Stop the bot
            Exit trade if inside one

        If the bot is inside a trade
            Check if it is the right time to exit the trade (exit indicator)
            If yes
               Exit the trade
               Append this action to the bot
        Else
            Check if it is the right time to enter a trade (confirmation indicator)
            If yes
               Enter a trade
               Append this action to the bot
        """

        # pass string to enum to get enum value
        self.state = BotState.RUNNING
        if self.state != BotState.RUNNING:
            raise Exception("Bot is not in running state")
        print("Price: ", price, "Prices: ", self.prices)
        # convert timestamp from datetime to int
        print("Timestamp: ", timestamp, "Type: ", type(timestamp)   )
        self.prices[timestamp] = price
        print("Prices: ", self.prices)
        should_stop_bot = True if random.randint(0, 1) == 1 else True

        if should_stop_bot:
            if self.in_trade:
                print("Closing trade")
                self.close_trade(timestamp=timestamp, price=price)

            self.state = BotState.FINISHED

        if self.in_trade:
            print("In trade")
            # Exit strategies
            should_close_trade = True if random.randint(0, 1) == 1 else True
            print("Should close trade: ", should_close_trade)
            if should_close_trade:
                self.close_trade(timestamp=timestamp, price=price)
        else:
            # Entry strategies
            print("Entering trade")
            indicator, amount = random.randint(-1, 1), 100
            should_enter_trade = False if indicator == 0 else True
            print("Should enter trade: ", should_enter_trade)

            if should_enter_trade:
                self.in_trade = True
                print("Entered trade")
                trade = Trade(
                    id=get_random_id(),
                    trade_type=TradeType.CALL,
                    amount=amount,
                    start_price=price,
                    started_at=datetime.fromtimestamp(timestamp)
                )
                self.trades.append(trade)
            print("Trades: ", self.trades)

        
