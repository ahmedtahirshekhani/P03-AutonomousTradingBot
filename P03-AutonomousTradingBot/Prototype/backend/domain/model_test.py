import pytest
from uuid import uuid4
from datetime import datetime, timedelta
from .model import Analyst, Investor, LoginReturn

# Helper functions
def create_analyst():
    return Analyst(
        id=str(uuid4()),
        name="Ahmed",
        address="Lums",
        email="ahmed@lums.com",
        phone_number="+92 333 3464655",
        password="832598e496ec310643ff62380fadf9a7d4d91ebf59da4b39eb86af7628c53ec6",  # SHA256 hash of password
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
        uuid4(success_attempt.token)  # This should not raise an exception
    except:
        pytest.fail("Raised an exception due to invalid token")

    fail_attempt = new_analyst.login(
        email="ahmed@lums.com",
        password="5151sda5s1d5as1d5asd",
    )
    assert fail_attempt.success == False
    assert fail_attempt.message == "User failed to log in!"
    assert fail_attempt.expiry == datetime.now() + timedelta(hours=1)
    with pytest.raises(ValueError):
        uuid4(fail_attempt.token)  # Token will be empty on failed log in
