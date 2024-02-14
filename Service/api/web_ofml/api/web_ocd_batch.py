from functools import cache

from flask import Blueprint, request
from loguru import logger

from Service import db
from Service.api.web_ofml.utility import query_table, patch_item
from Service.tables.utility import get_model_class_by_table_name

bp = Blueprint("web_ofml_ocd_batch", __name__, url_prefix="/web_ofml/ocd/batch")


@bp.route("/<string:table_name>", methods=["PATCH"])
def patch_items_(table_name: str):
    """
    patches 1 or n items in the given table where patch_body is applied for each item separately
    """
    patch_bodies = request.json
    table_class = get_model_class_by_table_name(table_name)
    for patch_body in patch_bodies:
        assert "db_key" in patch_body
        identifier = patch_body["db_key"]

        item: table_class = query_table(table_class=table_class,
                                        select_clause=None,
                                        where_clause=f"db_key = {identifier}",
                                        limit=1,
                                        make_json=False
                                        )
        assert item is not None, f"item requested by {patch_body} not found"
        logger.debug(f"PATCH {item} with f{patch_body}")
        patch_item(item, patch_body)
        logger.info(f"new: {item}")

    db.session.commit()

    return {}, 204


@bp.route("/web_ocd_artbase/exec_artbase_all", methods=["POST"])
def exec_artbase_all():
    where_clause = request.args.get("where", None)
    assert where_clause, "where_clause needed"
    artbase_items = request.json
    property2artbase_items = {_["property"]: _ for _ in artbase_items}
    print("where_clause", where_clause)
    print("artbase_item...")
    print(artbase_items)
    add_counter = 0
    property_class_items: list[...] = query_table(table_class=get_model_class_by_table_name("web_ocd_propertyclass"),
                                                  select_clause=None,
                                                  where_clause=where_clause,
                                                  limit=None,
                                                  make_json=False
                                                  )

    @cache
    def _query_properties(web_program_name: str, sql_db_program: str, prop_class: str):
        return query_table(table_class=get_model_class_by_table_name("web_ocd_property"),
                           select_clause=None,
                           where_clause=f"web_program_name = \"{web_program_name}\" AND sql_db_program = \"{sql_db_program}\" AND prop_class = \"{prop_class}\"",
                           limit=None,
                           make_json=False
                           )

    @cache
    def _property_value_exists(web_program_name: str, sql_db_program: str, prop_class: str, property_: str, value: str):
        return bool(query_table(table_class=get_model_class_by_table_name("web_ocd_propertyvalue"),
                                select_clause=None,
                                where_clause=f"web_program_name = \"{web_program_name}\" AND sql_db_program = \"{sql_db_program}\" AND prop_class = \"{prop_class}\" AND property = \"{property_}\" AND value_from = \"{value}\"",
                                limit=1,
                                make_json=False
                                ))

    @cache
    def _artbase_item_exists(web_program_name: str, sql_db_program: str, article_nr: str, prop_class: str,
                             property_: str, value: str):
        return bool(query_table(table_class=get_model_class_by_table_name("web_ocd_artbase"),
                                select_clause=None,
                                where_clause=f"web_program_name = \"{web_program_name}\" AND sql_db_program = \"{sql_db_program}\" AND article_nr = \"{article_nr}\" AND prop_class = \"{prop_class}\" AND property = \"{property_}\" AND prop_value = \"{value}\"",
                                limit=1,
                                make_json=False
                                ))

    print("found items", len(property_class_items))
    for class_item in property_class_items:
        print(class_item.article_nr, class_item.prop_class)
        property_items = _query_properties(class_item.web_program_name, class_item.sql_db_program,
                                           class_item.prop_class)
        matching_properties = set([_["property"] for _ in artbase_items]) & set([_.property for _ in property_items])
        print("matching_properties", matching_properties)
        for property_name in matching_properties:
            client_artbase_item = property2artbase_items[property_name]
            print("artbase_item", client_artbase_item, class_item.prop_class)

            value_exists = _property_value_exists(class_item.web_program_name,
                                                  class_item.sql_db_program,
                                                  class_item.prop_class,
                                                  client_artbase_item["property"],
                                                  client_artbase_item["value"]
                                                  )
            print("value_exists", value_exists)
            if not value_exists:
                continue

            artbase_item = {
                "web_program_name": class_item.web_program_name,
                "sql_db_program": class_item.sql_db_program,
                "article_nr": class_item.article_nr,
                "prop_class": class_item.prop_class,
                "property": client_artbase_item["property"],
                "prop_value": client_artbase_item["value"],
            }

            artbase_item_exists = _artbase_item_exists(*artbase_item.values())

            if artbase_item_exists:
                continue

            print("artbase_item_exists", artbase_item_exists)

            table_class = get_model_class_by_table_name("web_ocd_artbase")

            item = table_class.from_json(table_class, artbase_item)
            item.db_key = None
            print("ADD", item)
            db.session.add(item)
            add_counter += 1

    print(f"... added {add_counter}")
    db.session.commit()
    return {
        "insert_rows": add_counter
    }, 200
