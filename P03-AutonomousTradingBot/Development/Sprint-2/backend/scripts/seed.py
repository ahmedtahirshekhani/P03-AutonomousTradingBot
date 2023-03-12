
import psycopg2
from dotenv import load_dotenv
load_dotenv()
import os



connection = psycopg2.connect(
    host=os.environ.get("DB_HOST"),
    database=os.environ.get("DB_NAME"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    port=os.environ.get("DB_PORT")
)
cursor = connection.cursor()

sql = '''
write sql here
'''
cursor.execute(sql)

connection.commit()
