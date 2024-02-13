import pandas as pd

import Service.mysql.db as db
from flask import Blueprint, request, jsonify
from . import quey_interface
import time
from .utility import make_delete_statement, DeepcopyRequest, MERGE_KEYS, MergeAsRequest, check_web_article_exists, \
    check_article_exists
from Service.api.export_program.table_links import OCD_LINKS
from Service.api.export_program.util import update_table_links, HashMaker
from Service.tables.web.ocd import WebOcdArticle, WebProgram
from Service import db as flask_db
bp = Blueprint("deepcopy_ocd", __name__, url_prefix="/deepcopy/ocd")

# http://localhost:5000/deepcopy/ocd


def check_exists(row: dict[str, object], keys: list[str], into_table: str, cursor):
    where_clause = " AND ".join([f"{k} = %s" for k in keys])
    sql_check = f"SELECT 1 FROM {into_table} WHERE {where_clause}"
    where_values = [row[key] for key in keys]
    cursor.execute(sql_check, where_values)
    """ fetchone() throws "Unread result found" error sometimes, so we use fetchall() """
    exists = bool(cursor.fetchall())
    return exists


def merge_row(*, row: dict, into_table: str, web_program_name: str, cursor, keys):
    del row["db_key"]
    row["web_filter"] = 0
    row["web_program_name"] = web_program_name
    exists = check_exists(row, keys, into_table, cursor)

    if exists:
        return 0

    columns = ', '.join(row.keys())
    values_template = ', '.join(['%s'] * len(row))
    values = [str(_) for _ in row.values()]

    sql_insert = f"INSERT INTO {into_table} ({columns}) VALUES ({values_template})"
    print("sql_insert", sql_insert, "::", values)
    cursor.execute(sql_insert, values)
    return 1


def merge_rows_into_table_based_on(keys: list[str],
                                   new_rows: list[dict],
                                   into_table: str,
                                   web_program_name: str,
                                   connection):
    print(f"merge_rows_into_table_based_on :: {keys} = {len(new_rows)} ==> {into_table}")
    insertion_count = 0
    with connection.cursor(dictionary=True) as c:
        for row in new_rows:
            insertion_count += merge_row(row=row, into_table=into_table, web_program_name=web_program_name, keys=keys, cursor=c)
    print("insertion_count:", insertion_count)


@bp.route("/merge_as", methods=["GET"])
def merge_article_with_deepcopy_as():
    """ merges article as own separate thing where keys will be unique to this article """
    start = time.perf_counter()
    params = MergeAsRequest(**dict(request.values))
    print(params)
    """ check if article already exists in program and return """
    exists = check_web_article_exists(article=params.merge_as, program=params.program, web_program_name=params.merge_with)
    if exists:
        print(f"{params.merge_as} {params.program} already exists in {params.merge_with}")
        return make_merge_return_object(message=f"'{params.merge_as}' von '{params.program}' bereits in {params.merge_with} enthalten.",
                                        time_start=start, status=0), 200
    """ check if article exists at all """
    exists = check_article_exists(article=params.article, program=params.program)
    if not exists:
        print(f"{params.article} {params.program} doesnt exist.")
        return make_merge_return_object(message=f"'{params.article}' nicht in '{params.program}' gefunden.", time_start=start,
                                        status=0), 200
    ocd_links = OCD_LINKS
    article_numbers_and_programs = [(params.article, params.program,)]
    with db.new_connection() as read_connection:
        with read_connection.cursor(dictionary=True) as c:
            tables_2_yield = quey_interface.deepcopy_query(article_numbers_and_programs, c)
            with db.new_connection() as write_connection:
                hash_maker = HashMaker()
                for table_name, result_set in tables_2_yield:

                    print("table_name::", table_name, len(result_set))
                    df = pd.DataFrame(result_set)
                    if table_name in ocd_links:
                        update_table_links(table=df,
                                           linking_columns=ocd_links[table_name],
                                           hash_maker=hash_maker,
                                           unify_by="VALUE",
                                           unify_string=params.merge_as)
                    if table_name in "ocd_article ocd_artbase ocd_packaging ocd_articletaxes ocd_price ocd_propertyclass".split():
                        df["article_nr"] = params.merge_as

                    result_set = df.to_dict('records')
                    merge_rows_into_table_based_on(
                        MERGE_KEYS[table_name],
                        result_set,
                        f"web_{table_name}",
                        params.merge_with,
                        write_connection
                    )
                write_connection.commit()
    return make_merge_return_object(message=f"'{params.article}' von '{params.program}' als '{params.merge_as}' gemerged", time_start=start, status=1), 200


def make_merge_return_object(*, message, time_start, status):
    return {
        "status": status,
        "message": message,
        "time": round(time.perf_counter() - time_start, 2)
    }


@bp.route("/merge", methods=["GET"])
def merge_article_with_deepcopy():

    start = time.perf_counter()
    article = request.args.get("article")
    program = request.args.get("program")
    web_program_name = request.args.get("merge_with")
    print(f"args :: article={article} ; program={program} ; merge_with={web_program_name}")
    assert article and program and web_program_name, "article, program, merge_with need to be specified."
    article = article.strip()
    program = program.strip()
    web_program_name = web_program_name.strip()
    """ check if article already exists in program and return """
    exists = check_web_article_exists(article=article, program=program, web_program_name=web_program_name)
    if exists:
        print(f"{article} {program} already exists in {web_program_name}")
        return make_merge_return_object(message=f"'{article}' von '{program}' bereits in {web_program_name} enthalten.", time_start=start, status=0), 200

    """ check if article exists at all """
    exists = check_article_exists(article=article, program=program)
    if not exists:
        print(f"{article} {program} doesnt exist.")
        return make_merge_return_object(message=f"'{article}' nicht in '{program}' gefunden.", time_start=start, status=0), 200

    article_numbers_and_programs = [(article, program, )]

    with db.new_connection() as read_connection:
        with read_connection.cursor(dictionary=True) as c:
            tables_2_yield = quey_interface.deepcopy_query(article_numbers_and_programs, c)
            with db.new_connection() as write_connection:
                for table_name, result_set in tables_2_yield:
                    print("table_name::", table_name, len(result_set))
                    merge_rows_into_table_based_on(
                        MERGE_KEYS[table_name],
                        result_set,
                        f"web_{table_name}",
                        web_program_name,
                        write_connection
                    )
                write_connection.commit()

    return make_merge_return_object(message=f"'{article}' von '{program}' mit '{web_program_name}' gemerged", time_start=start, status=1), 200


@bp.route("/<string:name>", methods=["DELETE"])
def delete_deepcopy(name: str):
    """
    deletes a web_program by name from all tables
    """
    with db.new_connection() as connection:
        c = connection.cursor()
        """ delete the web_program record """
        c.execute(f"DELETE FROM web_program WHERE name = \"{name}\";")
        connection.commit()
        """ consume multi operation (otherwise can't commit) """
        for _ in c.execute(operation=make_delete_statement(name), multi=True):
            pass
        connection.commit()
        c.close()
    return {}, 200


@bp.route("/", methods=["POST"])
def deepcopy():
    """
    2 step process:
    step 1: deepcopy from ocd tables
    step 2: create web_program resource
    """
    start = time.perf_counter()
    body = DeepcopyRequest(**request.json)
    assert body.articlenumbers_and_programs, "no input"
    existing_web_program = WebProgram.query.filter(
            WebProgram.name == body.name,
        ).exists()
    exists = flask_db.session.query(existing_web_program).scalar()
    if exists:
        return {"error": "program with this name already exists"}, 400
    """ deepcopy ocd tables """
    with db.new_connection() as connection:
        c = connection.cursor(dictionary=True)
        quey_interface.deepcopy_insert(body.articlenumbers_and_programs, c, body.name)
        connection.commit()
        c.close()

    t_seconds = time.perf_counter() - start

    web_program = WebProgram(name=body.name,
                             owner_id=body.owner_id,
                             is_public=body.is_public,
                             article_input=body.article_input
                             )
    flask_db.session.add(web_program)
    flask_db.session.commit()

    # necessary because web_program gets not updated unless we access field directly
    web_program = WebProgram.query.filter(WebProgram.name == body.name).one()
    web_program_as_json = web_program.to_json()
    print("perCounter", t_seconds)
    return jsonify(web_program_as_json), 200


@bp.route("/test", methods=["GET"])
# @timeit
def test():
    inst = WebOcdArticle.by_program("talos")
    print("inst", inst)
    return "ok"
