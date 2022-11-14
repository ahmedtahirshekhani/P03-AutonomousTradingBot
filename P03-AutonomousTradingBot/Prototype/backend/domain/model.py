import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from hashlib import sha256
from typing import Dict, List
from uuid import uuid4

"""
Use cases
- Create a new analyst
- Analyst can log in
- Analyst can log out
- Analyst registers an investor
- Anaylst gets credentials for an investor
- Investor can log in
- Investor can log out

Invariants
- No two users can have the same email

Value Objects
- LoginReturn

Aggregates
- Analyst
- Investor
"""


@dataclass(frozen=True)
class LoginReturn:
    success: str
    message: str
    expiry: datetime
    token: str


@dataclass(frozen=True)
class InvestorRegistrationReturn:
    success: str
    message: str
    investor: Dict[str, str]
    password: str
    username: str


@dataclass
class Analyst:
    id: str
    name: str
    address: str
    email: str
    phone_number: str
    password: str
    expiry: datetime = None
    token: str = None

    @property
    def is_logged_in(self) -> bool:
        # Check if session exists
        if self.expiry is None:
            return False

        # Check if session has expired
        if datetime.now() > self.expiry:
            return False

        return True

    def login(self, email: str, password: str) -> LoginReturn:
        if email == email and password == password:
            self.expiry = datetime.now() + timedelta(hours=1)
            self.token = str(uuid4())

            return LoginReturn(
                True,
                "User successfully logged in!",
                self.expiry,
                self.token,
            )
        else:
            return LoginReturn(
                False,
                "User failed to log in!",
                None,
                None,
            )

    def logout(self):
        self.expiry = None
        self.token = None

    def register_investor(self, name, address, email, phone_number) -> InvestorRegistrationReturn:
        password = str(uuid4())

        investor = Investor(
            id=str(uuid4()),
            name=name,
            address=address,
            email=email,
            phone_number=phone_number,
            password=str(sha256(password.encode('utf-8')).hexdigest())
        )
        investorDetails = investor.get_investor_details()
        returnRegInvestor = InvestorRegistrationReturn(
            True,
            "Investor successfully registered!",
            investorDetails,
            password,
            email
        )
        return returnRegInvestor


@dataclass
class Investor:
    id: str
    name: str
    address: str
    email: str
    phone_number: str
    password: str

    def login(self, email: str, password: str):
        pass

    def logout(self):
        pass

    def get_investor_details(self):
        investorJson = {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "email": self.email,
            "phone_number": self.phone_number,
        }
        return json.dumps(investorJson)
