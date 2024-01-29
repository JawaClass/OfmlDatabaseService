from typing import Generator

import mysql.connector
from contextlib import contextmanager

from mysql.connector import MySQLConnection

config = {
    'host': 'pdf2obs01',
    'user': 'root',
    'password': '',
    'database': 'ofml'
}

# mysql+mysqlconnector://root:@pdf2obs01/ofml

Connection = Generator[MySQLConnection, None, None]


@contextmanager
def new_connection() -> Connection:
    c = mysql.connector.connect(**config)
    try:
        yield c
    finally:
        c.close()
#
# # def yield_all_tables(articlenumbers, programs=None):
# #     connection = new_connection()
# #     c = connection.cursor(dictionary=True)
# #
# #     tables = execute(articlenumbers, c, programs)
# #     for result_set, table_name in tables:
# #         yield {
# #             "table": table_name,
# #             "content": result_set
# #         }
# #
# #     c.close()
# #     connection.close()
#
#
# def article_table(articlenumbers: list[str]):
#     connection = new_connection()
#     c = connection.cursor(dictionary=True)
#     placeholders = ', '.join(['%s'] * len(articlenumbers))
#     c.execute(
#         f"""
#         SELECT * FROM ocd_article WHERE article_nr IN ({placeholders});
#         """, articlenumbers
#     )
#     result = c.fetchall()
#     c.close()
#     connection.close()
#     return result
