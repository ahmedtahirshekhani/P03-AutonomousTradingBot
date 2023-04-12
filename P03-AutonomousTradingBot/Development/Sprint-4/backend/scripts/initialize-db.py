import psycopg2
from dotenv import load_dotenv

load_dotenv()
import os


connection = psycopg2.connect(
    host=os.environ.get("DB_HOST"),
    database=os.environ.get("DB_NAME"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    port=os.environ.get("DB_PORT"),
)
cursor = connection.cursor()

with open("../trading_app/db/initialize-db.sql") as sql_init:
    sql = sql_init.read()
    print(sql)
    cursor.execute(sql)

    connection.commit()
