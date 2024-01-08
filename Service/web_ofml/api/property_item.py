from flask import Blueprint, jsonify, abort, request
from ..models import PropertyItem
bp = Blueprint("property_item", __name__, url_prefix="/web_ofml/property_item")


@bp.route('/save', methods=['POST'])
def create():
    body = request.get_json()
    assert "pClass" in body
    assert "program" in body
    assert "sessionId" in body
    assert "json" in body

    item = PropertyItem(
        p_class=body["pClass"],
        program=body["program"],
        session_id=body["sessionId"],
        json=body["json"]
    )

    PropertyItem.delete_by_p_class_program(item.p_class, item.program)
    PropertyItem.create(item)

    return jsonify(item.id)


@bp.route('/save_list', methods=['POST'])
def create_list():
    body = request.get_json()
    assert "pClass" in body
    assert "program" in body
    assert "sessionId" in body
    assert "json" in body

    ids = []
    PropertyItem.delete_by_p_class_program(body["pClass"], body["program"])

    for item_json in body["json"]:
        item = PropertyItem(
            p_class=body["pClass"],
            program=body["program"],
            session_id=body["sessionId"],
            json=item_json
        )

        PropertyItem.create(item)

        ids.append(item.id)

    return jsonify(ids)


@bp.route('/by_session_id/<session_id>', methods=['GET'])
def fetch(session_id):
    items = PropertyItem.by_session_id(session_id)
    return jsonify([_.as_dict() for _ in items])
