from celery.result import AsyncResult
import Service.mysql.db as db
from flask import Blueprint, request, jsonify
from . import quey_interface
import time
from .utility import make_delete_statement, DeepcopyRequest, MergeAsRequest
from Service.tables.web.ocd import WebOcdArticle, WebProgram
from Service import db as flask_db
bp = Blueprint("deepcopy_ocd", __name__, url_prefix="/deepcopy/ocd")

# http://localhost:5000/deepcopy/ocd


@bp.route("/merge_as", methods=["GET"])
def merge_article_with_deepcopy_as():
    print("merge_as........")
    params = MergeAsRequest(**dict(request.values))

    if request.args.get("as_task", True):
        from Service.api.deepcopy.ocd.tasks import celery_task_merge_article_with_deepcopy_as
        result: AsyncResult = celery_task_merge_article_with_deepcopy_as.delay(
            article=params.article, program=params.program, merge_as=params.merge_as, merge_with=params.merge_with
        )

        return {
            "description": f"merge {params.article} von {params.program} als {params.merge_as} mit {params.merge_with}",
            "result_id": result.id
        }
    else:
        from Service.api.deepcopy.ocd.tasks.tasks import merge_article_with_deepcopy_as
        return merge_article_with_deepcopy_as(article=params.article, program=params.program, merge_as=params.merge_as,
                                       merge_with=params.merge_with), 200


@bp.route("/merge", methods=["GET"])
def merge_article_with_deepcopy():

    article = request.args.get("article")
    program = request.args.get("program")
    web_program_name = request.args.get("merge_with")
    print(f"args :: article={article} ; program={program} ; merge_with={web_program_name}")
    assert article and program and web_program_name, "article, program, merge_with need to be specified."

    if request.args.get("as_task", True):
        from Service.api.deepcopy.ocd.tasks import celery_task_merge_article_with_deepcopy

        result: AsyncResult = celery_task_merge_article_with_deepcopy.delay(
            article=article, program=program, merge_with=web_program_name
        )

        print("ready ? ", result.id, result.ready(), AsyncResult(result.id).ready())

        return {
            "description": f"merge {article} von {program} mit {web_program_name}",
            "result_id": result.id
        }
    else:
        from Service.api.deepcopy.ocd.tasks.tasks import merge_article_with_deepcopy
        return merge_article_with_deepcopy(article=article, program=program, merge_with=web_program_name), 200


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


@bp.route("", methods=["POST"])
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
        return {"error": f"program with this name '{body.name}' already exists"}, 400
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
