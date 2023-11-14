import mysql.connector
from ocd_query import execute

config = {
    'host': 'pdf2obs01',
    'user': 'root',
    'password': '',
    'database': 'ofml'
}


def new_connection():
    # mysql+mysqlconnector://root:@pdf2obs01/ofml
    return mysql.connector.connect(**config)


def yield_all_tables(articlenumbers):
    connection = new_connection()
    c = connection.cursor(dictionary=True)

    tables = execute(articlenumbers, c)
    for result_set, table_name in tables:
        yield {
            "table": table_name,
            "content": result_set
        }

    c.close()
    connection.close()


def article_table(articlenumbers: list[str]):
    connection = new_connection()
    c = connection.cursor(dictionary=True)
    placeholders = ', '.join(['%s'] * len(articlenumbers))
    c.execute(
        f"""
        SELECT * FROM ocd_article WHERE article_nr IN ({placeholders});
        """, articlenumbers
    )
    result = c.fetchall()
    c.close()
    connection.close()
    return result
