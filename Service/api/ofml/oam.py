from flask import Blueprint, jsonify, abort
from Service.tables.oam import OamArticle2ofml
from .handler import handle_table

bp = Blueprint("oam", __name__, url_prefix="/oam")


@bp.route('/programs')
def programs():
    res = OamArticle2ofml.query.with_entities(OamArticle2ofml.sql_db_program).distinct().all()
    res = [_[0] for _ in res]
    return jsonify(res)


@bp.route('/table/<program>/<table_name>')
def table(program, table_name):
    if not str(table_name).startswith("oam_"):
        abort(404, description=f"Table {table_name} not part of OAM.")
    return handle_table(program, table_name)
