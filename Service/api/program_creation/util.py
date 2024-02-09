import _csv
import csv
from pathlib import Path

import pandas as pd
from loguru import logger
from pydantic import BaseModel

from Service.api.program_creation import Tables


class CreateProgramApiRequest(BaseModel):
    web_program_name: str
    program_name: str
    program_id: str
    export_path: str
    export_ocd: bool
    export_oam: bool
    export_oas: bool
    export_ofml: bool
    export_go: bool
    export_odb: bool
    export_registry: bool
    build_ebase: bool


def remove_columns(ofml_part):
    drop_columns = ["sql_db_program", "sql_db_timestamp_modified", "sql_db_timestamp_read", "db_key", "index", "web_filter", "web_program_name"]

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


class HashMaker:
    def __init__(self, start=1000):
        self.hashes = {}
        self.start = start

    def get(self, input_string: str) -> int:

        if (stored_hash := self.hashes.get(input_string, None)) is not None:
            return stored_hash

        self.hashes[input_string] = self.start + len(self.hashes)
        return self.hashes[input_string]


def update_table_links(*, table: pd.DataFrame,
                       linking_columns: list[str],
                       hash_maker: HashMaker,
                       unify_by: str,
                       unify_string: str):

    assert unify_by in ["COLUMN", "VALUE"]

    if table.empty:
        return

    def update_link(column: pd.Series):
        """
        apply the new links at column values where it's not an empty string / 0
        """
        assert type(column) is pd.Series

        dtype_ = column.dtype
        is_string = pd.api.types.is_string_dtype(dtype_)
        idx = column.loc[column.astype(bool)].index
        """ unique has based on input """
        if is_string:
            column[idx] = (
                    column[idx] +
                    (table[unify_string][idx].apply(lambda x: f"_{x.upper()}")
                     if unify_by == "COLUMN"
                     else unify_string)
            )
        else:
            column[idx] = (
                    column[idx].astype("string").fillna("") +
                    (table[unify_string][idx] if unify_by == "COLUMN" else unify_string)
            ).apply(hash_maker.get).astype(dtype_)
        return column

    table[linking_columns] = table[linking_columns].apply(update_link, axis=0)


def unify_column_linkages(links: dict[str, list[str]], tables: Tables, unify_column="sql_db_program"):
    hash_maker = HashMaker()
    for table_name in links:
        if tables[table_name].empty:
            continue
        table: pd.DataFrame = tables[table_name]
        linking_columns = links[table_name]
        update_table_links(table=table,
                           linking_columns=linking_columns,
                           unify_by="COLUMN",
                           unify_string=unify_column,
                           hash_maker=hash_maker)


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
