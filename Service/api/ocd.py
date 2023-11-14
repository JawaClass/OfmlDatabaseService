from flask import Blueprint, jsonify, abort
from Service.tables import OcdArticle
from Service.tables import TABLE_NAME_2_CLASS

bp = Blueprint("ocd", __name__, url_prefix="/ocd")


@bp.route('/programs')
def programs():
    res = OcdArticle.query.with_entities(OcdArticle.sql_db_program).distinct().all()
    res = [_[0] for _ in res]
    return jsonify(res)


@bp.route('/table/<program>/<name>')
def table(program, name):

    if not str(name).startswith("ocd_"):
        abort(404, description=f"Table {name} not part of OCD.")

    table_class = TABLE_NAME_2_CLASS[name]

    res = table_class.query.filter(table_class.sql_db_program == program).all()

    res = [_.to_json() for _ in res]

    return jsonify(res)
