import os
import time
import psycopg2
from psycopg2 import OperationalError

host = os.getenv("DATABASE_HOST", "postgres_db")
port = os.getenv("DATABASE_PORT", 5432)
user = os.getenv("DATABASE_USERNAME", "postgres")
password = os.getenv("DATABASE_PASSWORD", "1")
dbname = os.getenv("DATABASE_NAME", "ShopBoom")

while True:
    try:
        conn = psycopg2.connect(
            host=host, port=port, user=user, password=password, dbname=dbname
        )
        conn.close()
        print("Postgres ready!")
        break
    except OperationalError:
        print("Waiting for Postgres...")
        time.sleep(2)
