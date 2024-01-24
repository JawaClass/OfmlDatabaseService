import _csv
import csv
from pathlib import Path

import pandas as pd
from loguru import logger

from Service.api.program_creation import Tables


def remove_columns(ofml_part):
    drop_columns = ["sql_db_program", "sql_db_timestamp_modified", "sql_db_timestamp_read", "db_key", "index"]

    for table_name in ofml_part:
        if "sql_db_program" not in ofml_part[table_name].columns:
            logger.debug(f"INFO - no sql_db_program::: {table_name}")
            continue

        if ofml_part[table_name].empty:
            logger.debug(f"INFO - EMPTY_TABLE:::{table_name}")

        intersection_drop_columns = list(set(ofml_part[table_name].columns) & set(drop_columns))
        ofml_part[table_name].drop(
            columns=intersection_drop_columns,
            inplace=True)


def unify_column_linkages(links: dict[str, list[str]], tables: Tables):

    class HashMaker:
        def __init__(self):
            self.hashes = {}

        def get(self, input_string: str) -> int:

            if (stored_hash := self.hashes.get(input_string, None)) is not None:
                return stored_hash

            self.hashes[input_string] = 1 + len(self.hashes)
            return self.hashes[input_string]

    hash_maker = HashMaker()

    for table_name in links:

        if tables[table_name].empty:
            continue

        linking_columns = links[table_name]

        def update_link(column: pd.Series):
            """
            apply the new links at column values where it's not an empty string / 0
            """
            assert type(column) is pd.Series

            dtype_ = column.dtype
            is_string = pd.api.types.is_string_dtype(dtype_)
            idx = column.loc[column.astype(bool)].index

            if is_string:
                column[idx] = (
                        column[idx] +
                        (tables[table_name]["sql_db_program"][idx].apply(lambda x: f"_{x.upper()}"))
                )
            else:
                column[idx] = (
                        column[idx].astype("string").fillna("") +
                        tables[table_name]["sql_db_program"][idx]
                ).apply(hash_maker.get).astype(dtype_)
            return column

        tables[table_name][linking_columns] = tables[table_name][linking_columns].apply(update_link, axis=0)


def export_ofml_part(program_name: str,
                     export_path: Path,
                     tables: Tables,
                     inp_descr_content: str | None = None,
                     inp_descr_filename: str | None = None):
    export_path.mkdir(parents=True, exist_ok=True)

    for table_name in tables:
        df = tables[table_name]
        file_name = f"{table_name}.{get_file_ext(table_name, program_name)}"
        encoding = get_encoding(table_name, program_name)
        sep = get_file_seperator(table_name, program_name)
        try:
            df.to_csv(export_path / file_name, header=False, index=False, index_label=False, sep=sep,
                      encoding=encoding, quoting=csv.QUOTE_NONE)  # , quotechar=" "
        except _csv.Error as e:
            print("to_csv ERROR", file_name)  # ocd:relation,
            df.to_csv(export_path / file_name, header=False, index=False, index_label=False, sep=sep,
                      encoding=encoding)

    if inp_descr_content and inp_descr_filename:
        (export_path / inp_descr_filename).write_text(inp_descr_content)


def get_encoding(table_name: str, program_name: str):
    return "cp1252" if table_name.endswith("text") or table_name.endswith("txt") or table_name in {
        "ocd_propertyvalue", "ocd_property", "ocd_relation", f"{program_name}_de"
    } else None


def get_file_ext(table_name: str, program_name: str):
    if table_name == f"{program_name}_de":
        return "sr"
    return "csv"


def get_file_seperator(table_name: str, program_name: str):
    if table_name == f"{program_name}_de":
        return "="
    return ";"