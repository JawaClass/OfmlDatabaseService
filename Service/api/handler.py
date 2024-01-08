from flask import jsonify, abort, request
from Service.tables import TABLE_NAME_2_CLASS


def handle_table(program, table_name, column=None, value=None):
    table_class = TABLE_NAME_2_CLASS[table_name]
    columns = {k for k in table_class.__dict__.keys() if not k.startswith("_")}

    requested_columns = request.args.get("columns", None)
    where_clause = request.args.get("where", None)

    if column and value:

        if column not in columns:
            abort(404, description=f"Column '{column}' not found in columns {columns} of table '{table_name}'.")

        query = table_class.query.filter(
            getattr(table_class, column) == value,
            getattr(table_class, "sql_db_program") == program)

    else:
        query = table_class.query.filter(table_class.sql_db_program == program)

    if requested_columns:

        requested_columns = requested_columns.split(",")

        unknown_requested_columns = set(requested_columns).difference(set(columns))
        if unknown_requested_columns:
            abort(404, f"Column(s) {unknown_requested_columns} not present in {columns}")

        base_columns = [getattr(table_class, c) for c in requested_columns]
        query = query.with_entities(*base_columns)

    res = query.all()
    res = prepare_json(res, requested_columns)

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
