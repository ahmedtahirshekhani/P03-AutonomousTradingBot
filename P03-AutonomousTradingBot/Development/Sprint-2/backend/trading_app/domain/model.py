from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from uuid import uuid4
from enum import Enum
from .utils import hash_password

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
        self, name: str, address: str, phone_number: str, email: str
    ) -> RegisterInvestorReturn:
        password = str(uuid4())[:INVESTOR_PASS_LEN]  # Autogenerate password

        return RegisterInvestorReturn(
            investor=Investor(
                name=name,
                address=address,
                email=email,
                phone_number=phone_number,
                hashed_password=hash_password(password=password),
                id=str(uuid4()),
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


@dataclass(frozen=True)
class Trade:
    stock_id: str
    amount: float
    buying_price: float
    selling_price: float
    spread: float
    started_at: datetime
    ended_at: datetime
    company_name: str
    id: str = str(uuid4())


@dataclass
class Bot:
    analyst_id: str
    investor_id: str
    amount: int
    state: BotState = BotState.IDLE
    trades: List[Trade] = field(default_factory=list)
    assigned_model: int = 0
    risk_appetite: RiskAppetite = RiskAppetite.LOW
    target_return: float = 0
    duration: datetime = datetime.now()
    id: str = str(uuid4())

    def initiate_execution(self):
        self.state = BotState.RUNNING

    def terminate(self):
        self.state = BotState.TERMINATED
