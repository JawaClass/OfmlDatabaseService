from pathlib import Path

import pandas as pd

from Service.api import table_descriptions
from Service.api.program_creation.create_interface import CreateInterface
from Service.api.program_creation.util import export_ofml_part, unify_column_linkages, remove_columns
from Service.tables.go import GoArticles, GoProperties, GoTypes, GoDeSr


class GoCreator(CreateInterface):

    def __init__(self, *,
                 articlenumbers: list[str],
                 programs: list[str],
                 program_name: str,
                 connection,
                 program_path: Path): # con: Connection = db.session.connection()
        self.articlenumbers = articlenumbers
        self.programs = programs
        self.program_name = program_name
        self.tables = {}
        self.connection = connection
        self.program_path = program_path
        self.path = program_path / "2"

    def load(self):

        self.tables["go_articles"] = pd.read_sql(
            GoArticles.query.filter(
                GoArticles.article_nr.in_(self.articlenumbers),
                GoArticles.sql_db_program.in_(self.programs)
            ).statement,
            self.connection)

        self.tables["go_properties"] = pd.read_sql(
            GoProperties.query.filter(
                GoProperties.key.in_(self.tables["go_articles"]["prm_key"].tolist()),
                GoProperties.sql_db_program.in_(self.programs)
            ).statement,
            self.connection)

        self.tables["go_types"] = pd.read_sql(
            GoTypes.query.filter(
                GoTypes.id.in_(self.tables["go_articles"]["id"].tolist()),
                GoTypes.sql_db_program.in_(self.programs)
            ).statement,
            self.connection)

        # only take polymorphism "ch" and defining props
        self.tables["go_types"] = self.tables["go_types"].loc[
            lambda x: ((x["mode"] & 8) == 0) & (x["format"].isin(["ch", ""]))]

        # sr file
        self.tables[f"{self.program_name}_de"] = pd.read_sql(
            GoDeSr.query.filter(
                GoDeSr.sql_db_program.in_(self.programs)
            ).statement,
            self.connection)

    def update(self):
        self.tables["go_articles"]["program"] = self.program_name
        self.tables["go_articles"]["chprm_key"] = ""
        self._unify_links()

    def _unify_links(self):
        go_links = {
            "go_types": ["id"],
            "go_articles": ["id", "prm_key"],
            "go_properties": ["id", "key"],
        }

        unify_column_linkages(go_links, self.tables)

    def export(self):
        remove_columns(self.tables)
        export_ofml_part(program_name=self.program_name,
                         export_path=self.path,
                         tables=self.tables,
                         inp_descr_content=table_descriptions.go.INP_DESCR,
                         inp_descr_filename="mt.inp_descr")
