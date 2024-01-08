from flask import Blueprint, jsonify, abort, request
from ..models import Session
bp = Blueprint("session", __name__, url_prefix="/web_ofml/session")


@bp.route('/update', methods=['PUT'])
def update():

    body = request.get_json()
    print("update session :::", body)
    assert "id" in body

    session = Session.by_id(body["id"])
    Session.update(session, **body)
    return jsonify(session.id)


@bp.route('/create', methods=['POST'])
def create():
    body = request.get_json()

    print("create session", body)

    assert "name" in body
    assert "isPublic" in body
    assert "ownerId" in body
    assert "articleInput" in body

    session = Session(
        name=body["name"],
        is_public=body["isPublic"],
        owner_id=body["ownerId"],
        article_input=body["articleInput"]
    )

    Session.create(session)

    return jsonify(session.as_dict())


@bp.route('/delete', methods=['DELETE'])
def delete():
    body = request.get_json()
    assert "id" in body

    Session.delete_by_id(body["id"])
    return jsonify(1)


@bp.route('/all', methods=['GET'])
def all_sessions():
    if request.args.get("with_user"):
        sessions_with_user = Session.all_with_user()
        return jsonify([
            {
                "session": session.as_dict(),
                "owner": user.as_dict(),
            } for session, user in sessions_with_user])
    else:
        sessions = Session.all()
        return jsonify([_.as_dict() for _ in sessions])


@bp.route('/by_email/<email>', methods=['GET'])
def by_email(email):
    sessions = Session.by_email(email)
    return jsonify([_.as_dict() for _ in sessions])


@bp.route('/by_id/<session_id>', methods=['GET'])
def by_id(session_id):
    session = Session.by_id(session_id)
    if session:
        return jsonify(session.as_dict())
    return jsonify(None)

