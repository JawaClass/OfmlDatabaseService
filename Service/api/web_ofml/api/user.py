from flask import Blueprint, jsonify, abort, request
from ..models import User
bp = Blueprint("user", __name__, url_prefix="/web_ofml/user")


@bp.route('/create', methods=['POST'])
def create():
    body = request.get_json()
    assert "email" in body

    existing_user = User.by_email(body["email"])

    if existing_user:
        return jsonify(existing_user.as_dict())

    user = User(
        email=body["email"],
        name=body.get("name", None),
    )

    User.create(user)
    return jsonify(user.as_dict())


@bp.route('/by_email/<email>', methods=['GET'])
def by_email(email):
    user = User.by_email(email)
    if user:
        return jsonify(user.as_dict())
    return jsonify(None)


@bp.route('/all', methods=['GET'])
def all_users():
    users = User.all()
    return jsonify([_.as_dict() for _ in users])


@bp.route('/test', methods=['GET'])
def test():
    print("test")
    return "test..."