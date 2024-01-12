from flask import Blueprint, jsonify, abort
from Service.tables import Article
from .handler import handle_table

bp = Blueprint("oas", __name__, url_prefix="/oas")


@bp.route('/programs')
def programs():
    res = Article.query.with_entities(Article.sql_db_program).distinct().all()
    res = [_[0] for _ in res]
    return jsonify(res)


@bp.route('/table/<program>/<table_name>')
def table(program, table_name, column=None, value=None):
    if table_name not in "text article resource structure variant".split():
        abort(404, description=f"Table {table_name} not part of OAS.")
    return handle_table(program, table_name)
