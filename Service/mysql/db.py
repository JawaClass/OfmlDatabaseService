from typing import Generator
import mysql.connector
from contextlib import contextmanager
from mysql.connector import MySQLConnection
from settings import Config

config = {
    'host': Config.MYSQL_SERVER,
    'user': Config.MYSQL_USER,
    'password': Config.MYSQL_PASSWORD,
    'database': Config.MYSQL_DATABASE
}

Connection = Generator[MySQLConnection, None, None]


@contextmanager
def new_connection() -> Connection:
    c = mysql.connector.connect(**config)
    try:
        yield c
    finally:
        c.close()
