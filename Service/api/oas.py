from flask import Blueprint, jsonify, abort
from Service.tables import Article
from Service.tables import TABLE_NAME_2_CLASS

bp = Blueprint("oas", __name__, url_prefix="/oas")


@bp.route('/programs')
def programs():
    res = Article.query.with_entities(Article.sql_db_program).distinct().all()
    res = [_[0] for _ in res]
    return jsonify(res)


@bp.route('/table/<program>/<name>')
def table(program, name):

    if name not in "text article resource structure variant".split():
        abort(404, description=f"Table {name} not part of OAS.")

    table_class = TABLE_NAME_2_CLASS[name]

    res = table_class.query.filter(table_class.sql_db_program == program).all()

    res = [_.to_json() for _ in res]

    return jsonify(res)
