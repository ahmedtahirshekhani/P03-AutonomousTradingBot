from .unit_of_work import UnitOfWork
from ..domain.model import Bot, Analyst


def get_analyst(analyst_email: str, uow: UnitOfWork) -> Analyst:
    with uow:
        fetched_analyst = uow.analysts.get(analyst_email=analyst_email)
        return fetched_analyst


def view_all_bots(analyst_id: str, investor_id: str, uow: UnitOfWork):
    print("inside view all bots query")
    sql = """ 
        select * from bots where analyst_id = %s and investor_id = %s
    """
    with uow:
        uow.cursor.execute(sql, [analyst_id, investor_id])
        bots = uow.cursor.fetchall()
        retArr = []
        for bot in bots:
            retArr.append(
                Bot(
                    id=bot[0],
                    analyst_id=bot[1],
                    investor_id=bot[2],
                    state=bot[3],
                    assigned_model=bot[4],
                    risk_appetite=bot[5],
                    target_return=bot[6],
                    duration=bot[7],
                )
            )
        return retArr


def get_all_investors(uow: UnitOfWork):
    with uow:
        investors = uow.investors.get_all()
        return investors
