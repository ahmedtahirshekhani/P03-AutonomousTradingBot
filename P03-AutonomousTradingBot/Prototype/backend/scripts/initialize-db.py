import psycopg2

connection = psycopg2.connect(
    host="babar.db.elephantsql.com",
    database="nblnggxg",
    user="nblnggxg",
    password="Tm0JXyT4V5gNuTrbJGpywBkngiwfQ-M4",
)
cursor = connection.cursor()

with open("../trading_app/db/initialize-db.sql") as sql_init:
    sql = sql_init.read()
    cursor.execute(sql)

    connection.commit()
