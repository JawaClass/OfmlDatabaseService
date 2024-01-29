from flask import Blueprint, jsonify, request, abort
from Service import db
from Service.tables.utility import get_model_class_by_table_name
from loguru import logger
from Service.web_ofml.utility import query_table, patch_items, patch_item, ReturnQueryType

bp = Blueprint("web_ofml_ocd", __name__, url_prefix="/web_ofml/ocd/")


@bp.route("/<string:table_name>/details", methods=["GET"])
def get_item_details_(table_name: str):
    """
    returns 1 or n item in the given table
    where item is of type article or subset of article
    """
    if table_name == "web_ocd_article":
        table_class = get_model_class_by_table_name(table_name)
        print("get_item_details_", table_name, table_class)

        articles_result = query_table(table_class=table_class,
                                      select_clause=request.args.get("select", None),
                                      where_clause=request.args.get("where", None),
                                      limit=request.args.get("limit", None),
                                      make_json=True,
                                      as_type=ReturnQueryType.LIST
                                      )

        print("T articles_result", type(articles_result))
        for a in articles_result:
            a["kurztext"] = query_table(table_class=get_model_class_by_table_name("web_ocd_artshorttext"),
                                   where_clause=f"web_program_name = \"{a['web_program_name']}\" AND sql_db_program = \"{a['sql_db_program']}\" AND textnr = \"{a['short_textnr']}\" AND language = \"de\"",
                                   make_json=True,
                                   limit=None,
                                   select_clause=None,
                                   as_type=ReturnQueryType.TRIM
                                   )

            a["langtext"] = query_table(table_class=get_model_class_by_table_name("web_ocd_artlongtext"),
                                   where_clause=f"web_program_name = \"{a['web_program_name']}\" AND sql_db_program = \"{a['sql_db_program']}\" AND textnr = \"{a['long_textnr']}\" AND language = \"de\"",
                                   make_json=True,
                                   limit=None,
                                   select_clause=None,
                                   as_type=ReturnQueryType.LIST
                                   )

            a["klassen"] = query_table(table_class=get_model_class_by_table_name("web_ocd_propertyclass"),
                                   where_clause=f"web_program_name = \"{a['web_program_name']}\" AND sql_db_program = \"{a['sql_db_program']}\" AND article_nr = \"{a['article_nr']}\"",
                                   make_json=True,
                                   limit=None,
                                   select_clause=None,
                                   as_type=ReturnQueryType.LIST
                                   )

        return jsonify(articles_result)

    abort(404, "Not supported")


@bp.route("/<string:table_name>", methods=["GET"])
def get_item_(table_name: str):
    """
    returns 1 or n item in the given table
    where item is of type article or subset of article
    """
    table_class = get_model_class_by_table_name(table_name)
    return jsonify(
        query_table(table_class=table_class,
                    select_clause=request.args.get("select", None),
                    where_clause=request.args.get("where", None),
                    limit=request.args.get("limit", None),
                    make_json=True
                    )
    )


@bp.route("/<string:table_name>", methods=["PATCH"])
def patch_item_(table_name: str):
    """
    patches 1 or n items in the given table
    """
    table_class = get_model_class_by_table_name(table_name)
    articles: list[table_class] = query_table(table_class=table_class,
                                              select_clause=None,
                                              where_clause=request.args.get("where", None),
                                              limit=None,
                                              make_json=False
                                              )
    patch_body = request.json
    assert patch_body
    logger.debug(f"PATCH {len(articles)} articles")
    patch_items(articles, patch_body)
    db.session.commit()
    return {}, 204


@bp.route("/<string:table_name>/<int:identifier>", methods=["DELETE"])
def delete_item_(table_name: str, identifier: int):
    """
    deletes 1 item
    """
    table_class = get_model_class_by_table_name(table_name)
    article: table_class | None = query_table(table_class=table_class,
                                              select_clause=None,
                                              where_clause=f"db_key = {identifier}",
                                              limit=1,
                                              make_json=False
                                              )

    logger.debug(f"DELETE {article} ")
    if article is None:
        return {}, 404

    db.session.delete(article)
    db.session.commit()

    return {}, 200


@bp.route("/<string:table_name>", methods=["POST"])
def post_item_(table_name: str):
    """
    inserts 1 item
    """
    table_class = get_model_class_by_table_name(table_name)
    post_body = request.json
    assert post_body
    logger.debug(f"POST {post_body} ")
    article = table_class.from_json(table_class, post_body)
    article.db_key = None
    article_json = article.to_json()
    db.session.add(article)
    db.session.commit()
    return jsonify(article_json), 200


@bp.route("/<string:table_name>/<int:identifier>", methods=["PUT"])
def put_item_(table_name: str, identifier: int):
    """
    replaces 1 item
    raises sqlalchemy.exc.IntegrityError if supplied put_body is insufficient
    """
    table_class = get_model_class_by_table_name(table_name)
    put_body = request.json
    assert put_body

    logger.debug(f"PUT {put_body} @ {identifier}")

    item: table_class | None = query_table(table_class=table_class,
                                           select_clause=None,
                                           where_clause=f"db_key = {identifier}",
                                           limit=1,
                                           make_json=False
                                           )
    if item is None:
        return {}, 404

    item: table_class
    # delete fields except the identifier
    item_as_json = item.to_json()
    del item_as_json["db_key"]
    patch_item(item, {k: None for k in item_as_json})
    # set fields applied in put_body
    patch_item(item, put_body)
    item_json = item.to_json()
    db.session.commit()
    return jsonify(item_json), 200
