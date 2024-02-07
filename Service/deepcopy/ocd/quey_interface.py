import re

from mysql.connector.cursor import MySQLCursor
from Service.deepcopy.ocd.query_statement import QUERIES, TABLES


def _insert_tables(articles: list, cursor: MySQLCursor, web_program_name: str):
    placeholders = ', '.join(['%s'] * len(articles))
    c: MySQLCursor
    operation = QUERIES.format(placeholders=placeholders, web_program_name=web_program_name)
    cursor_generator = cursor.execute(
                operation=operation,
                params=articles,
                multi=True
            )
    """ consume """
    for _ in cursor_generator:
        pass


def _query_tables(articles: list, cursor: MySQLCursor):
    placeholders = ', '.join(['%s'] * len(articles))
    c: MySQLCursor
    operation = re.sub(r"INSERT\s+INTO\s+web_(.|\n)*?;", "", QUERIES).format(placeholders=placeholders)
    # print("op::")
    # print(operation)
    cursor_generator = cursor.execute(
                operation=operation,
                params=articles,
                multi=True
            )
    for i, c in enumerate(cursor_generator):
        # print(c.statement[0:30])
        if c.statement.startswith("SELECT"):
            table_name_idx = 4 if c.statement.startswith("SELECT DISTINCT") else 3
            table_name = c.statement.split()[table_name_idx].replace("_TEMP_LOCAL_1", "").replace("_TEMP", "")
            yield table_name, c.fetchall()


def _create_temp_table(table_name: str, programs: list, cursor: MySQLCursor):
    placeholders = ', '.join(['%s'] * len(programs))

    sql = f"""
    CREATE TEMPORARY TABLE {table_name}_TEMP
    AS SELECT *
    FROM {table_name}
    WHERE sql_db_program IN ({placeholders});
    """
    cursor.execute(sql, programs)


def _create_temporary_tables(programs: list, cursor: MySQLCursor):
    print("_create_temporary_tables")
    for table_name in TABLES:
        _create_temp_table(table_name, programs, cursor)


def _get_programs(articles: list, cursor: MySQLCursor):
    placeholders = ', '.join(['%s'] * len(articles))
    sql = f"""
    SELECT DISTINCT sql_db_program FROM ocd_article WHERE article_nr IN ({placeholders})
    """
    cursor.execute(sql, articles)
    result = list(map(lambda x: x['sql_db_program'], cursor.fetchall()))
    return result


def deepcopy_insert(articles_and_programs: list[(str, str,)], cursor: MySQLCursor, web_program_name: str):
    """
    articles: list of article;program tuples
    """
    print("deepcopy")
    articles = list(set([_[0] for _ in articles_and_programs]))
    programs = list(set([_[1] for _ in articles_and_programs]))
    _create_temporary_tables(programs, cursor)
    _insert_tables(articles, cursor, web_program_name)
    return None


def deepcopy_query(articles_and_programs: list[(str, str,)], cursor: MySQLCursor):
    """
    articles: list of article;program tuples
    """
    print("deepcopy")
    articles = list(set([_[0] for _ in articles_and_programs]))
    programs = list(set([_[1] for _ in articles_and_programs]))
    _create_temporary_tables(programs, cursor)
    return _query_tables(articles, cursor)
