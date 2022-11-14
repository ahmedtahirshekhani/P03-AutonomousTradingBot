from datetime import datetime, timedelta
from hashlib import sha256
from uuid import uuid4

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


def create_investor(
    username: str,
    password: str,
    name: str,
    address: str,
    phone_number: str,
):
    return Investor(
        id=str(uuid4()),
        name=name,
        address=address,
        email=username,
        phone_number=phone_number,
        password=sha256(password).hexdigest(),  # SHA256 hash of password
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
    assert success_attempt.success == True
    assert success_attempt.message == "User successfully logged in!"
    assert success_attempt.expiry == datetime.now() + timedelta(hours=1)
    try:
        # This should not raise an exception if token is valid
        uuid4(success_attempt.token)
    except:
        pytest.fail("Raised an exception due to invalid token")

    fail_attempt = new_analyst.login(
        email="ahmed@lums.com",
        password="5151sda5s1d5as1d5asd",
    )
    assert fail_attempt.success == False
    assert fail_attempt.message == "User failed to log in!"
    assert fail_attempt.expiry == None
    assert fail_attempt.token == None


def test_analyst_logout():
    new_analyst = create_analyst()

    success_attempt: LoginReturn = new_analyst.login(
        email="ahmed@lums.com",
        password="832598e496ec310643ff62380fadf9a7d4d91ebf59da4b39eb86af7628c53ec6",
    )
    assert success_attempt.success == True
    assert success_attempt.message == "User successfully logged in!"
    assert success_attempt.expiry == datetime.now() + timedelta(hours=1)
    try:
        uuid4(success_attempt.token)  # This should not raise an exception
    except:
        pytest.fail("Raised an exception due to invalid token")

    try:
        new_analyst.logout()
    except:
        pytest.fail("Raised an exception due to an error in logout")


def test_register_investor():
    new_analyst = create_analyst()

    invester_credentials = new_analyst.register_investor(
        "Suleman", "Lums", "suleman@test.com", "+92 333 3455488")

    assert invester_credentials.success == True
    assert invester_credentials.message == "Investor successfully registered!"

    assert type(invester_credentials.username) is str
    assert len(invester_credentials.username) >= 8

    assert type(invester_credentials.password) is str
    assert len(invester_credentials.password) >= 8


def test_get_investor_credentials():
    new_analyst = create_analyst()
    invester_credentials = new_analyst.get_investor_credentials(
        new_analyst.email)

    username = invester_credentials.username
    password = invester_credentials.password

    fetched_credentials = new_analyst.get_credentials(username)

    assert fetched_credentials.password == password


def test_investor_login():
    new_analyst = create_analyst()
    invester_credentials = new_analyst.register_investor()

    username = invester_credentials.username
    password = invester_credentials.password

    new_investor = create_investor(
        username,
        password,
        "NIC",
        "SSE basement obviously",
        "+92 333 3455488",
    )

    success_attempt: LoginReturn = new_investor.login(
        email=username,
        password=password,
    )
    assert success_attempt.success == True
    assert success_attempt.message == "User successfully logged in!"
    assert success_attempt.expiry == datetime.now() + timedelta(hours=1)
    try:
        uuid4(success_attempt.token)  # This should not raise an exception
    except:
        pytest.fail("Raised an exception due to invalid token")

    fail_attempt = new_investor.login(
        email="ahmed@lums.com",
        password="5151sda5s1d5as1d5asd",
    )
    assert fail_attempt.success == False
    assert fail_attempt.message == "User failed to log in!"
    assert fail_attempt.expiry == None
    assert fail_attempt.token == None


def test_investor_logout():
    new_analyst = create_analyst()
    invester_credentials = new_analyst.register_investor()

    username = invester_credentials.username
    password = invester_credentials.password

    new_investor = create_investor(
        username,
        password,
        "NIC",
        "SSE basement obviously",
        "+92 333 3455488",
    )

    success_attempt: LoginReturn = new_investor.login(
        email="ahmed@lums.com",
        password="832598e496ec310643ff62380fadf9a7d4d91ebf59da4b39eb86af7628c53ec6",
    )
    assert success_attempt.success == True
    assert success_attempt.message == "User successfully logged in!"
    assert success_attempt.expiry == datetime.now() + timedelta(hours=1)
    try:
        uuid4(success_attempt.token)  # This should not raise an exception
    except:
        pytest.fail("Raised an exception due to invalid token")

    try:
        new_investor.logout()
    except:
        pytest.fail("Raised an exception due to an error in logout")
