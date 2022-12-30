from .unit_of_work import AbstractUnitOfWork
from dataclasses import dataclass, field
from ..domain.model import Bot



def view_all_bots(analyst_id: str, investor_id:str, uow: AbstractUnitOfWork):
    sql = """ 
        select * from bots where analyst_id = %s and investor_id = %s
    """
    with uow:
        uow.cursor.execute(sql, [analyst_id, investor_id])
        bots = uow.cursor.fetchall()
        retArr = []
        for bot in bots:
            retArr.append(Bot(id=bot[0], analyst_id = bot[1], investor_id = bot[2], state = bot[3], assigned_model = bot[4], risk_appetite = bot[5], target_return = bot[6], duration = bot[7]))
        return retArr
            