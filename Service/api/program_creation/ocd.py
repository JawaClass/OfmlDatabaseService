import subprocess
from pathlib import Path

import pandas as pd
from loguru import logger

from Service.api import table_descriptions
from Service.api.program_creation.create_interface import CreateInterface
from Service.api.program_creation.table_links import OCD_LINKS
from Service.api.program_creation.util import export_ofml_part, unify_column_linkages, remove_columns
#from Service.db import yield_all_tables
from Service.deepcopy.ocd.utility import make_select_statement, WEB_OCD_TABLES
from Service.mysql import db
from settings import Config


class OcdCreator(CreateInterface):

    def __init__(self, *, web_program_name, program_name: str, program_path: Path, program_id: str):
        self.tables = {}
        self.web_program_name = web_program_name
        self.program_name = program_name
        self.program_id = program_id
        self.path = program_path / "DE" / "2" / "db"

    def _make_ocd_version(self):
        non_prefix_table_names = [_.replace("ocd_", "") for _ in list(self.tables.keys())]
        data = [
            [
                "4.1",
                "SAP_4_6",
                "2.16.1",
                "20060801",
                "99991231",
                "DE",
                "",
                0,
                ",".join(non_prefix_table_names),
                ""
            ]
        ]
        columns = "format_version rel_coding data_version date_from date_to region varcond_var placeholder_on tables comment".split()
        return pd.DataFrame(data=data, columns=columns)

    def load(self):
        logger.debug("load")
        multi_stmt_select_all = make_select_statement(self.web_program_name)
        with db.new_connection() as connection:
            cursor = connection.cursor(dictionary=True)
            cursor_generator = cursor.execute(
                operation=multi_stmt_select_all,
                params=None,
                multi=True
            )
            table_names = WEB_OCD_TABLES
            for idx, this_cursor in enumerate(cursor_generator):
                data = this_cursor.fetchall()
                table_name = table_names[idx].replace("web_", "")
                self.tables[table_name] = pd.DataFrame(data)
                # input(".")
            cursor.close()

        self.tables["ocd_version"] = self._make_ocd_version()

    def update(self):
        logger.debug("update")
        self._remove_farb_tabellen_relations()
        self._update_id()
        self._unify_links()

    def _unify_links(self):
        ocd_links = OCD_LINKS
        unify_column_linkages(ocd_links, self.tables)

    def _update_id(self):
        self.tables["ocd_article"]["series"] = self.program_id

    def _remove_farb_tabellen_relations(self):
        assert self.tables

        df_where_table_is_defined: pd.DataFrame = (
            self.tables["ocd_relation"].loc[lambda x: x["rel_block"].str.contains(r"table\s.+?\s\(.+?", regex=True, case=False)]
        )
        df_relations_where_table_is_defined = (
            self.tables["ocd_relation"].loc[lambda x: x["rel_name"].isin(df_where_table_is_defined["rel_name"])]
        )
        self.tables["ocd_relation"] = self.tables["ocd_relation"].drop(df_relations_where_table_is_defined.index)

    def export(self):
        logger.debug("export")
        remove_columns(self.tables)
        export_ofml_part(program_name=self.web_program_name,
                         export_path=self.path,
                         tables=self.tables,
                         inp_descr_content=table_descriptions.ocd.INP_DESCR,
                         inp_descr_filename="pdata.inp_descr")

    def build_ebase(self):
        print("ocd build ebase!!")
        tables_folder = self.path
        inp_descr_filepath = tables_folder / "pdata.inp_descr"
        ebase_filepath = tables_folder / "pdata.ebase"
        command = f"{Config.CREATE_EBASE_EXE} -d {tables_folder} {inp_descr_filepath} {ebase_filepath}"
        subprocess.run(command)
