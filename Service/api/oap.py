from flask import Blueprint, jsonify, abort
from Service.tables import OapType
from Service.tables import TABLE_NAME_2_CLASS
from .handler import handle_table
bp = Blueprint("oap", __name__, url_prefix="/oap")


@bp.route('/programs')
def programs():
    res = OapType.query.with_entities(OapType.sql_db_program).distinct().all()
    res = [_[0] for _ in res]
    return jsonify(res)


@bp.route('/table/<program>/<table_name>/<column>/<value>')
@bp.route('/table/<program>/<table_name>')
def table(program, table_name, column=None, value=None):
    if not str(table_name).startswith("oap_"):
        abort(404, description=f"Table {table_name} not part of OAP.")
    return handle_table(program, table_name, column, value)
