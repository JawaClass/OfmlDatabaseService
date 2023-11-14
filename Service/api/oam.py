from flask import Blueprint, jsonify, abort
from Service.tables import OamArticle2ofml
from Service.tables import TABLE_NAME_2_CLASS

bp = Blueprint("oam", __name__, url_prefix="/oam")


@bp.route('/programs')
def programs():
    res = OamArticle2ofml.query.with_entities(OamArticle2ofml.sql_db_program).distinct().all()
    res = [_[0] for _ in res]
    return jsonify(res)


@bp.route('/table/<program>/<name>')
def table(program, name):

    if not str(name).startswith("oam_"):
        abort(404, description=f"Table {name} not part of OAM.")

    table_class = TABLE_NAME_2_CLASS[name]

    res = table_class.query.filter(table_class.sql_db_program == program).all()

    res = [_.to_json() for _ in res]

    return jsonify(res)
