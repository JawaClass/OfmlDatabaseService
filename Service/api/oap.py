from flask import Blueprint, jsonify, abort
from Service.tables import OapType
from Service.tables import TABLE_NAME_2_CLASS

bp = Blueprint("oap", __name__, url_prefix="/oap")


@bp.route('/programs')
def programs():
    res = OapType.query.with_entities(OapType.sql_db_program).distinct().all()
    res = [_[0] for _ in res]
    return jsonify(res)


@bp.route('/table/<program>/<name>')
def table(program, name):

    if not str(name).startswith("oap_"):
        abort(404, description=f"Table {name} not part of OAP.")

    table_class = TABLE_NAME_2_CLASS[name]

    res = table_class.query.filter(table_class.sql_db_program == program).all()

    res = [_.to_json() for _ in res]

    return jsonify(res)
