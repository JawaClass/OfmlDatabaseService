import enum

from sqlalchemy import text
from typing import Type
from Service.tables import Base
from enum import Enum, auto


class ReturnQueryType(Enum):
    TRIM = auto()
    LIST = auto()


def query_table(*, table_class: Type[Base],
                select_clause: str | None,
                where_clause: str | None,
                limit: int | None,
                make_json: bool,
                as_type: ReturnQueryType = ReturnQueryType.TRIM
                ) -> list[dict | Type[Base]] | dict | Type[Base] | None:
    # table_class = WebOcdArticle# get_model_class_by_table_name[table_name]
    assert (select_clause and make_json) or not (select_clause and make_json)
    assert issubclass(table_class, Base), f"table_class {table_class} is not supported"
    columns = {k for k in table_class.__dict__.keys() if not k.startswith("_")}
    # print("columns", columns)
    # select_clause = request.args.get("select", None)
    # where_clause = request.args.get("where", None)
    # limit = request.args.get("limit", None)
    if limit:
        limit = parse_string_to_int(limit)
        assert isinstance(limit, int), f"limit mus be integer, was {limit} ({type(limit)})"

    # print("select_clause ::", select_clause)
    # print("where_clause ::", where_clause)
    # print("limit", limit)

    query = table_class.query
    requested_columns = None
    if where_clause:
        query = query.filter(text(where_clause))

    if select_clause:

        requested_columns = select_clause.split(",")

        unknown_requested_columns = set(requested_columns).difference(set(columns))
        assert len(unknown_requested_columns) == 0, f"Column(s) {unknown_requested_columns} not present in {columns}"

        base_columns = [getattr(table_class, c) for c in requested_columns]
        query = query.with_entities(*base_columns)

    if limit:
        res = query.limit(limit).all()
    else:
        res = query.all()

    if as_type == ReturnQueryType.LIST:
        return jsonify_query_items(res, requested_columns) if make_json else res

    if limit == 1:
        if len(res) >= 1:
            return jsonify_query_item(res[0], requested_columns) if make_json else res[0]
        else:
            return None
    else:
        return jsonify_query_items(res, requested_columns) if make_json else res


def jsonify_query_item(item: Base, requested_columns: None | list[str] = None) -> dict:
    if not requested_columns:
        return item.to_json()
    else:
        return dict(zip(requested_columns, item))


def jsonify_query_items(items: list[Base], requested_columns: None | list[str] = None) -> list[dict]:
    return [jsonify_query_item(item, requested_columns) for item in items]


def parse_string_to_int(value) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None


def patch_item(item: Base, patch_body: dict):
    for key, value in patch_body.items():
        setattr(item, key, value)


def patch_items(items: Base, patch_body: dict):
    for item in items:
        patch_item(item, patch_body)


def resolve_limit(data, limit: int):
    if data is None:
        return None
    if not isinstance(data, list):
        return data
    if len(data) == 0:
        return data
    if limit == 1:
        return data[0]
    return data[:limit]
