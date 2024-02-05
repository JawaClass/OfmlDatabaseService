import Service.mysql.db as db
from flask import Blueprint, request, jsonify
from . import quey
import time
from .utility import make_delete_statement, DeepcopyRequest
from ...tables.web.ocd import WebOcdArticle, WebProgram
from Service import db as flask_db
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
    """
    2 step process:
    step 1: deepcopy from ocd tables
    step 2: create web_program resource
    """
    start = time.perf_counter()
    body = DeepcopyRequest(**request.json)

    existing_web_program = WebProgram.query.filter(
            WebProgram.name == body.name,
        ).exists()
    exists = flask_db.session.query(existing_web_program).scalar()
    if exists:
        return {"error": "program with this name already exists"}, 400
    """ deepcopy ocd tables """
    with db.new_connection() as connection:
        c = connection.cursor(dictionary=True)
        quey.deepcopy(body.articlenumbers_and_programs, c, body.name, fetch=True)
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
