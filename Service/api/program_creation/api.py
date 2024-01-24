from flask import Blueprint, jsonify, request
from Service.api.program_creation.creator import ProgramCreator
# from Service.api.db import yield_all_tables

bp = Blueprint("program_creation", __name__, url_prefix="/program_creation")


# @bp.route('/from_articlenumbers')
# def from_articlenumbers():
#     print("from_articlenumbers")
#
#     articles = ["TLTN16880A", "TLTN20880A"]
#     if not len(set(articles)) == len(articles):
#         return "articles not unique"
#
#     for _ in yield_all_tables(articles):
#         print(_["table"])
#         print(len(_["content"]), _["content"])
#         input("...")
#     return "ok"


#print(from_articlenumbers())

@bp.route('/create', methods=["POST"])
def create_program():

    body: dict = request.get_json()
    assert body

    program_creator = ProgramCreator(body)

    return jsonify({
        "export_path": str(program_creator.export_program_path_windows)
    })
