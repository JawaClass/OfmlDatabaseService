import Service.mysql.db as db
from flask import Blueprint, request
from . import quey
import time
from .utility import make_delete_statement, DeepcopyRequest
from ...tables.web.ocd import WebOcdArticle

bp = Blueprint("deepcopy_ocd", __name__, url_prefix="/deepcopy/ocd")

# http://localhost:5000/deepcopy/ocd


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
    start = time.perf_counter   ()

    print("deepcopy...")
    print("request.json")
    print(request.json)

    body = DeepcopyRequest(**request.json)

    print("/deepcopy ::")
    print(body)
    # return "ok..."

    with db.new_connection() as connection:
        c = connection.cursor(dictionary=True)
        """ create web_program record """
        c.execute(
            operation="INSERT INTO web_program (name, owner_id, is_public, article_input) VALUES (%s, %s, %s, %s);",
            params=(body.name, body.owner_id, body.is_public, body.article_input))
        connection.commit()
        """ deepcopy ocd tables """
        quey.deepcopy(body.articlenumbers_and_programs, c, body.name, fetch=True)
        connection.commit()
        c.close()

    t_seconds = time.perf_counter() - start
    print("perCounter", t_seconds)
    return f"ok ({t_seconds}s)"


@bp.route("/test", methods=["GET"])
# @timeit
def test():
    inst = WebOcdArticle.by_program("talos")
    print("inst", inst)
    return "ok"
