from flask import Blueprint, jsonify, abort
from Service.tables import GoTypes
from .handler import handle_table

bp = Blueprint("go", __name__, url_prefix="/go")


@bp.route('/programs')
def programs():
    res = GoTypes.query.with_entities(GoTypes.sql_db_program).distinct().all()
    res = [_[0] for _ in res]
    return jsonify(res)


@bp.route('/table/<program>/<table_name>')
def table(program, table_name):
    if not str(table_name).startswith("go_"):
        abort(404, description=f"Table {table_name} not part of GO.")
    return handle_table(program, table_name)
