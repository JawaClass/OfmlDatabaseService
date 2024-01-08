from flask import Blueprint, jsonify
from .. import db
from sqlalchemy import text
bp = Blueprint("misc", __name__, url_prefix="/misc")


@bp.route('/timestamp')
def timestamp():
    res = db.session.execute(
        text("SELECT date FROM timestamp WHERE type = 'init_tables';"),

    ).fetchone()

    return jsonify(res[0])


@bp.route('/all')
def all_values():
    res = db.session.execute(
        text("SELECT * FROM timestamp;"),

    ).fetchall()
    res = dict(tuple(_[::-1]) for _ in res)

    return jsonify(res)
