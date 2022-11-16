import psycopg2

connection = psycopg2.connect(
    host="ec2-52-1-17-228.compute-1.amazonaws.com",
    database="d6n032iomt2j2b",
    user="wtnfvochnbjkxy",
    password="161aace1eb2a7e56721ca628d0950ec8b41f3b8f348acdb877d3ee5829ff8de4",
)
cursor = connection.cursor()

with open("../db/initialize-db.sql") as sql_init:
    sql = sql_init.read()
    cursor.execute(sql)

    connection.commit()
