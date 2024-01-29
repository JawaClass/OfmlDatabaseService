from flask import jsonify, abort, request
from sqlalchemy import text

from Service.tables.utility import get_model_class_by_table_name


def handle_table(program, table_name):
    table_class = get_model_class_by_table_name[table_name]
    columns = {k for k in table_class.__dict__.keys() if not k.startswith("_")}

    select_clause = request.args.get("select", None)
    where_clause = request.args.get("where", None)

    print("select_clause ::", select_clause)
    print("where_clause ::", where_clause)

    query = table_class.query.filter(table_class.sql_db_program == program)

    if where_clause:
        query = query.filter(text(where_clause))

    if select_clause:

        requested_columns = select_clause.split(",")

        unknown_requested_columns = set(requested_columns).difference(set(columns))
        if unknown_requested_columns:
            abort(404, f"Column(s) {unknown_requested_columns} not present in {columns}")

        base_columns = [getattr(table_class, c) for c in requested_columns]
        query = query.with_entities(*base_columns)

    res = query.all()
    res = prepare_json(res, select_clause)

    return jsonify(res)


def prepare_json(res, requested_columns=None):
    if not res:
        return []

    from ..tables import Base
    if isinstance(res[0], Base):
        res = [_.to_json() for _ in res]
    else:
        res = [dict(zip(requested_columns, row)) for row in res]
    return res
