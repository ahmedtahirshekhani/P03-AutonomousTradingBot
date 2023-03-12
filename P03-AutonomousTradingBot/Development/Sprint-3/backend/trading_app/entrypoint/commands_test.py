import pytest

from .commands import *
from ..entrypoint import unit_of_work
from ..domain.utils import hash_password


def seed_analyst(uow):
    return create_analyst(
        address="LUMS",
        email="test@analyst.com",
        name="Test user",
        password="12345678",
        phone_number="+92 333 3442255",
        uow=uow,
    )


def seed_investor(uow):
    return register_investor(

        name="Test investor",
        address="LUMS",
        analyst_email="test@analyst.com",
        email="test@investor.com",
        phone_number="+92 444 4565684",
        ntn_number="240129412049",
        uow=uow,
    )

def seed_bot(uow, analyst_id, investor_id):
    """
     balance: float,
    risk_appetite: RiskAppetite,
    target_return: float,
    """
    return add_bot(
        analyst_id=analyst_id,
        investor_id=investor_id,
        stocks_ticker="AAPL",
        balance=100000,
        risk_appetite=RiskAppetite.LOW,
        target_return=0.1,
        uow=uow,
    )



def test_create_analyst():

    with unit_of_work.FakeUnitOfWork() as uow:
        seed_analyst(uow)
        fetched_analyst = uow.analysts.get(analyst_email="test@analyst.com")

    assert fetched_analyst.address == "LUMS"
    assert fetched_analyst.email == "test@analyst.com"
    assert fetched_analyst.name == "Test user"
    assert fetched_analyst.hashed_password == hash_password("12345678")
    assert fetched_analyst.phone_number == "+92 333 3442255"


def test_analyst_login():
    with unit_of_work.FakeUnitOfWork() as uow:
        seed_analyst(uow)

        analyst_login(
            analyst_email="test@analyst.com",
            password="12345678",
            uow=uow,
        )

        # Wrong email
        with pytest.raises(Exception) as e_info:
            analyst_login(
                analyst_email="test@analyst.coms",
                password="12345678",
                uow=uow,
            )

        # Wrong password
        with pytest.raises(Exception) as e_info:
            analyst_login(
                analyst_email="test@analyst.com",
                password="123456789",
                uow=uow,
            )


def test_register_investor():
    with unit_of_work.FakeUnitOfWork() as uow:
        seed_analyst(uow)
        investor_seed = seed_investor(uow)

        fetched_investor = uow.investors.get("test@investor.com")

    assert fetched_investor.name == "Test investor"
    assert fetched_investor.address == "LUMS"
    assert fetched_investor.email == "test@investor.com"
    assert fetched_investor.phone_number == "+92 444 4565684"
    assert fetched_investor.hashed_password == hash_password(
        investor_seed.plain_text_password
    )

def test_investor_login():
    with unit_of_work.FakeUnitOfWork() as uow:
        seed_analyst(uow)
        investor_seed = seed_investor(uow)


        investor_login(
            investor_email="test@investor.com",
            password=investor_seed.plain_text_password,
            uow=uow,
        )

        # Wrong email
        with pytest.raises(Exception) as e_info:
            investor_login(
                investor_email="123@test.com",
                password=investor_seed.plain_text_password,
                uow=uow,
            )

        # Wrong password
        with pytest.raises(Exception) as e_info:
            investor_login(
                investor_email="test@investor.com",
                password="123456789",
                uow=uow,
            )
        
def test_investor_logout():
    # testing if logout works
    with unit_of_work.FakeUnitOfWork() as uow:
        seed_analyst(uow)
        investor_seed = seed_investor(uow)

        investor_login(
            investor_email="test@investor.com",
            password=investor_seed.plain_text_password,
            uow=uow,
        )

        investor_logout(
            investor_email="test@investor.com",
            uow=uow,
        )

        # Wrong email
        with pytest.raises(Exception) as e_info:
            investor_logout(
                investor_email="test@investor1.com",
                uow=uow,
            )


def test_add_bot():
    with unit_of_work.FakeUnitOfWork() as uow:
        analyst = seed_analyst(uow)
        investordata = seed_investor(uow)
        bot = seed_bot(uow, analyst.id, investordata.investor.id)


        fetched_bot = uow.bots.get(bot.id)
    
        assert fetched_bot.initial_balance == 100000
        assert fetched_bot.current_balance == 100000
        assert fetched_bot.risk_appetite == RiskAppetite.LOW
        assert fetched_bot.target_return == 0.1
        assert fetched_bot.stocks_ticker == "AAPL"
        assert fetched_bot.analyst_id == analyst.id
        assert fetched_bot.investor_id == investordata.investor.id


def test_initiate_bot_execution():
    with unit_of_work.FakeUnitOfWork() as uow:
        analyst = seed_analyst(uow)
        investordata = seed_investor(uow)
        bot = seed_bot(uow, analyst.id, investordata.investor.id)

        initiate_bot_execution(
            bot_id=bot.id,
            uow=uow,
        )

        fetched_bot = uow.bots.get(bot.id)

        assert fetched_bot.state == BotState.RUNNING

def test_terminate_bot():
    with unit_of_work.FakeUnitOfWork() as uow:
        analyst = seed_analyst(uow)
        investordata = seed_investor(uow)
        bot = seed_bot(uow, analyst.id, investordata.investor.id)

        terminate_bot(
            bot_id=bot.id,
            uow=uow,
        )

        fetched_bot = uow.bots.get(bot.id)

        assert fetched_bot.state == BotState.TERMINATED
