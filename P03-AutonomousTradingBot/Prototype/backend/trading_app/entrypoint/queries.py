def view_all_bots(investor_id: str):
    sql = """ 
        select * from bots where investor_id = %s
    """
    cursor.execute(sql, [investor_id])