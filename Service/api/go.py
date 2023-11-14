from flask import Blueprint, jsonify, abort
from Service.tables import GoTypes
from Service.tables import TABLE_NAME_2_CLASS

bp = Blueprint("go", __name__, url_prefix="/go")


@bp.route('/programs')
def programs():
    res = GoTypes.query.with_entities(GoTypes.sql_db_program).distinct().all()
    res = [_[0] for _ in res]
    return jsonify(res)


@bp.route('/table/<program>/<name>')
def table(program, name):
    if not str(name).startswith("go_"):
        abort(404, description=f"Table {name} not part of GO.")

    table_class = TABLE_NAME_2_CLASS[name]

    res = table_class.query.filter(table_class.sql_db_program == program).all()

    res = [_.to_json() for _ in res]

    return jsonify(res)
