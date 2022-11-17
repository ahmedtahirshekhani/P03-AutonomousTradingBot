import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from hashlib import sha256
from typing import Dict, List
from uuid import uuid4

INVESTOR_PASS_LEN: int = 8

"""
Use cases
- Create a new analyst
- Analyst can log in
- Analyst can log out
- Analyst registers an investor and gets credentials for an investor
- Investor can log in
- Investor can log out

Invariants
- No two users can have the same email

Value Objects
- LoginReturn

Aggregates
- Analyst
- Investor

Future upgrades
- Reset password for an investor by analyst
"""


@dataclass(frozen=True)
class LoginReturn:
    success: bool
    message: str
    expiry: datetime
    token: str


@dataclass
class Investor:
    name: str
    address: str
    email: str
    phone_number: str
    password: str
    id: str = str(uuid4())
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

    # TODO: handle login rejection using exceptions
    def login(self, email: str, password: str) -> LoginReturn:
        if self.email == email and self.password == password:
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


# Here passwords are stored in has
# TODO: change password name to hashed_password
@dataclass
class Analyst:
    name: str
    address: str
    email: str
    phone_number: str
    password: str
    id: str = str(uuid4())
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
        hashed_pass = str(sha256(password.encode("utf-8")).hexdigest())

        if self.email == email and self.password == hashed_pass:
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

    def register_investor(
        self, name: str, address: str, phone_number: str, email: str
    ) -> Dict[str, Investor | str]:
        password = str(uuid4())[:INVESTOR_PASS_LEN]  # Autogenerate password

        return {
            "investor": Investor(
                name=name,
                address=address,
                email=email,
                phone_number=phone_number,
                password=str(sha256(password.encode("utf-8")).hexdigest()),
            ),
            "plain_text_password": password,
        }
