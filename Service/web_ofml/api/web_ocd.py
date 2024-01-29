import time

from flask import Blueprint, jsonify, request, abort
from Service import db
from Service.tables.utility import get_model_class_by_table_name
from loguru import logger
from Service.web_ofml.utility import query_table, patch_items, patch_item, ReturnQueryType
import asyncio
bp = Blueprint("web_ofml_ocd", __name__, url_prefix="/web_ofml/ocd/")


@bp.route("/<string:table_name>/details", methods=["GET"])
def get_item_details_(table_name: str):
    """
    returns item with details attached
    """

    start = time.perf_counter()

    if table_name == "web_ocd_article":
        table_class = get_model_class_by_table_name(table_name)

        articles_result = query_table(table_class=table_class,
                                      select_clause=request.args.get("select", None),
                                      where_clause=request.args.get("where", None),
                                      limit=request.args.get("limit", None),
                                      make_json=True,
                                      as_type=ReturnQueryType.LIST
                                      )

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

    if table_name == "web_program":
        table_class = get_model_class_by_table_name(table_name)

        web_program_result = query_table(table_class=table_class,
                                         select_clause=request.args.get("select", None),
                                         where_clause=request.args.get("where", None),
                                         limit=request.args.get("limit", None),
                                         make_json=True,
                                         as_type=ReturnQueryType.LIST
                                         )
        for p in web_program_result:
            p["owner"] = query_table(table_class=get_model_class_by_table_name("web_user"),
                                     where_clause=f"id = {p['owner_id']}",
                                     make_json=True,
                                     limit=1,
                                     select_clause=None,
                                     as_type=ReturnQueryType.TRIM
                                     )

        return jsonify(web_program_result)

    if table_name == "web_ocd_propertyclass":  # ca. 8 seconds
        table_class = get_model_class_by_table_name(table_name)

        property_class_result = query_table(table_class=table_class,
                                            select_clause=request.args.get("select", None),
                                            where_clause=request.args.get("where", None),
                                            limit=request.args.get("limit", None),
                                            make_json=True,
                                            as_type=ReturnQueryType.LIST
                                            )

        for p_class in property_class_result:
            p_class["properties"] = query_table(table_class=get_model_class_by_table_name("web_ocd_property"),
                                                where_clause=f"web_program_name = \"{p_class['web_program_name']}\" AND sql_db_program = \"{p_class['sql_db_program']}\" AND prop_class = \"{p_class['prop_class']}\"",
                                                make_json=True,
                                                limit=None,
                                                select_clause=None,
                                                as_type=ReturnQueryType.LIST
                                                )
            for prop in p_class["properties"]:
                if prop["scope"] != "C":
                    continue

                prop["text"] = query_table(table_class=get_model_class_by_table_name("web_ocd_propertytext"),
                                           where_clause=f"web_program_name = \"{prop['web_program_name']}\" AND sql_db_program = \"{prop['sql_db_program']}\" AND textnr = \"{prop['prop_textnr']}\" AND language = \"de\" ",
                                           make_json=True,
                                           limit=1,
                                           select_clause=None,
                                           as_type=ReturnQueryType.TRIM
                                           )
                prop["values"] = query_table(table_class=get_model_class_by_table_name("web_ocd_propertyvalue"),
                                             where_clause=f"web_program_name = \"{prop['web_program_name']}\" AND sql_db_program = \"{prop['sql_db_program']}\" AND prop_class = \"{prop['prop_class']}\" AND property = \"{prop['property']}\" ",
                                             make_json=True,
                                             limit=None,
                                             select_clause=None,
                                             as_type=ReturnQueryType.LIST
                                             )

                for val in prop["values"]:
                    val["text"] = query_table(table_class=get_model_class_by_table_name("web_ocd_propvaluetext"),
                                              where_clause=f"web_program_name = \"{val['web_program_name']}\" AND sql_db_program = \"{val['sql_db_program']}\" AND textnr = \"{val['pval_textnr']}\" AND language = \"de\" ",
                                              make_json=True,
                                              limit=1,
                                              select_clause=None,
                                              as_type=ReturnQueryType.TRIM
                                              )
        print(f"time {time.perf_counter()-start:.2f}s")
        return jsonify(property_class_result)

    # if table_name == "web_ocd_propertyclass2":
    #     query = f"""
    #             SELECT simple_ocd_property.pos_prop, simple_ocd_property.prop_type, simple_ocd_property.property, simple_ocd_property.text, simple_ocd_propertyvalue.value_from, simple_ocd_propertyvalue.text, simple_ocd_property.prop_class, simple_ocd_property.sql_db_program
    #             FROM
    #             (SELECT web_ocd_propertyvalue.prop_class, web_ocd_propertyvalue.property, web_ocd_propertyvalue.value_from, web_ocd_propvaluetext.text
    #             FROM web_ocd_propertyvalue
    #             LEFT JOIN (SELECT * FROM web_ocd_propvaluetext WHERE UPPER(ocd_propvaluetext.language) = "DE") web_ocd_propvaluetext ON web_ocd_propertyvalue.pval_textnr = web_ocd_propvaluetext.textnr
    #             WHERE web_ocd_propertyvalue.sql_db_program = "{program}"
    #             AND web_ocd_propertyvalue.prop_class = "{prop_class}"
    #             AND web_ocd_propvaluetext.sql_db_program = "{program}") simple_ocd_propertyvalue
    #             ,
    #             (SELECT web_ocd_property.prop_class, web_ocd_property.property, web_ocd_propertytext.text, web_ocd_property.scope, web_ocd_property.sql_db_program, web_ocd_property.pos_prop, web_ocd_property.prop_type
    #             FROM web_ocd_property
    #             LEFT JOIN (SELECT * FROM web_ocd_propertytext WHERE UPPER(ocd_propertytext.language) = "DE") web_ocd_propertytext ON web_ocd_property.prop_textnr = web_ocd_propertytext.textnr
    #             WHERE web_ocd_property.scope = "C"
    #             AND web_ocd_property.sql_db_program = "{program}"
    #             AND web_ocd_property.prop_class = "{prop_class}"
    #             AND web_ocd_propertytext.sql_db_program = "{program}"
    #             ) simple_ocd_property
    #             WHERE simple_ocd_property.prop_class = simple_ocd_propertyvalue.prop_class
    #             AND simple_ocd_property.property = simple_ocd_propertyvalue.property
    #             ORDER BY simple_ocd_property.pos_prop
    #             ;
    #                 """.format(program="talos", prop_class="TISCH82_B")

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
