from datetime import datetime, timedelta
from hashlib import sha256
from uuid import uuid4, UUID

import pytest

from .model import Analyst, Investor, LoginReturn

# Helper functions


def create_analyst():
    return Analyst(
        id=str(uuid4()),
        name="Ahmed",
        address="Lums",
        email="ahmed@lums.com",
        phone_number="+92 333 3464655",
        # SHA256 hash of password
        password="832598e496ec310643ff62380fadf9a7d4d91ebf59da4b39eb86af7628c53ec6",
    )


# Test cases
def test_create_new_analyst():
    new_analyst = create_analyst()

    assert new_analyst.name == "Ahmed"
    assert new_analyst.address == "Lums"
    assert new_analyst.email == "ahmed@lums.com"
    assert new_analyst.phone_number == "+92 333 3464655"
    assert (
        new_analyst.password
        == "832598e496ec310643ff62380fadf9a7d4d91ebf59da4b39eb86af7628c53ec6"
    )


def test_analyst_login():
    new_analyst = create_analyst()

    success_attempt: LoginReturn = new_analyst.login(
        email="ahmed@lums.com",
        password="832598e496ec310643ff62380fadf9a7d4d91ebf59da4b39eb86af7628c53ec6",
    )
    one_hour_later = datetime.now() + timedelta(hours=1)

    assert success_attempt.success == True
    assert success_attempt.message == "User successfully logged in!"

   



    fail_attempt = new_analyst.login(
        email="ahmed@lums.com",
        password="5151sda5s1d5as1d5asd",
    )
    assert fail_attempt.success == False
    assert fail_attempt.message == "User failed to log in!"
 

def test_analyst_logout():
    new_analyst = create_analyst()

    success_attempt: LoginReturn = new_analyst.login(
        email="ahmed@lums.com",
        password="832598e496ec310643ff62380fadf9a7d4d91ebf59da4b39eb86af7628c53ec6",
    )

    one_hour_later = datetime.now() + timedelta(hours=1)

    assert success_attempt.success == True
    assert success_attempt.message == "User successfully logged in!"

   
    

    new_analyst.logout()
   


def test_register_investor():
    new_analyst = create_analyst()

    registered_invester = new_analyst.register_investor(
        name="Suleman",
        address="Lums",
        email="suleman@test.com",
        phone_number="+92 333 3455488",
    )
    password = registered_invester["plain_text_password"]

    assert type(password) is str
    assert len(password) >= 8


def test_investor_login():
    new_analyst = create_analyst()
    registered_invester = new_analyst.register_investor(
        name="Suleman",
        address="Lums",
        email="suleman@test.com",
        phone_number="+92 333 3455488",
    )["investor"]

    success_attempt: LoginReturn = registered_invester.login(
        email=registered_invester.email,
        password=registered_invester.password,
    )
    one_hour_later = datetime.now() + timedelta(hours=1)

    assert success_attempt.success == True
    assert success_attempt.message == "User successfully logged in!"

  

    fail_attempt = registered_invester.login(
        email="ahmed@lums.com",
        password="5151sda5s1d5as1d5asd",
    )
    assert fail_attempt.success == False
    assert fail_attempt.message == "User failed to log in!"
    

def test_investor_logout():
    new_analyst = create_analyst()
    registered_invester = new_analyst.register_investor(
        name="Suleman",
        address="Lums",
        email="suleman@test.com",
        phone_number="+92 333 3455488",
    )["investor"]

    success_attempt: LoginReturn = registered_invester.login(
        email=registered_invester.email,
        password=registered_invester.password,
    )
    one_hour_later = datetime.now() + timedelta(hours=1)

    assert success_attempt.success == True
    assert success_attempt.message == "User successfully logged in!"


    registered_invester.logout()
    