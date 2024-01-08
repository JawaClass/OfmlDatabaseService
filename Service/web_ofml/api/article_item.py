from flask import Blueprint, jsonify, abort, request
from ..models import ArticleItem
bp = Blueprint("article_item", __name__, url_prefix="/web_ofml/article_item")


@bp.route('/save', methods=['POST'])
def create():
    body = request.get_json()
    assert "articleNr" in body
    assert "program" in body
    assert "sessionId" in body
    assert "json" in body

    item = ArticleItem.get_by_article_program_session_id(
        body["articleNr"], body["program"], body["sessionId"])

    if item:
        ArticleItem.update(item, json=body["json"])
    else:
        item = ArticleItem(
            article_nr=body["articleNr"],
            program=body["program"],
            session_id=body["sessionId"],
            json=body["json"]
        )

        ArticleItem.create(item)

    return jsonify(item.id)


@bp.route('/by_session_id/<session_id>', methods=['GET'])
def by_session_id(session_id):
    return jsonify([_.as_dict() for _ in ArticleItem.by_session_id(session_id)])


@bp.route('/all', methods=['GET'])
def all_items():
    return jsonify([_.as_dict() for _ in ArticleItem.all()])


@bp.route('/delete', methods=['DELETE'])
def delete():
    body = request.get_json()

    assert "sessionId" in body
    assert "article" in body
    assert "program" in body

    ArticleItem.delete_by_article_program_session_id(body["article"], body["program"], body["sessionId"])

    return jsonify(1)
