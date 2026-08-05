# from psycopg_pool import ConnectionPool
import psycopg

from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv("DATABASE_URL")

# pool_conn = ConnectionPool(
#     conninfo=db_url, 
#     min_size=2,
#     max_size=10,
#     timeout=30,
#     )


def get_connection():
    # return pool_conn.connection()
    return psycopg.connect(db_url)