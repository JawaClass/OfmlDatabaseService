from pathlib import Path

import pandas as pd
from loguru import logger

from Service.api import table_descriptions
from Service.api.program_creation.create_interface import CreateInterface
from Service.api.program_creation.util import export_ofml_part, remove_columns
from Service.tables.oam import OamArticle2odbparams, OamProperty2mat, OamArticle2ofml


class OamCreator(CreateInterface):

    def __init__(self, *,
                 web_program_name: str,
                 articlenumbers: [str],
                 programs: [str],
                 connection,
                 program_path: Path,
                 program_name,
                 exports_odb: bool):  # con: Connection = db.session.connection()
        self.web_program_name = web_program_name
        self.articlenumbers = articlenumbers
        self.programs = programs
        self.tables = {}
        self.connection = connection
        self.program_path = program_path
        self.program_name = program_name
        self.path = self.program_path / "DE" / "2" / "oam"
        self.exports_odb = exports_odb

    def load(self):

        self.tables["oam_article2ofml"] = pd.read_sql(
            OamArticle2ofml.query.filter(
                OamArticle2ofml.article.in_(self.articlenumbers),
                OamArticle2ofml.sql_db_program.in_(self.programs)
            ).statement,
            self.connection)

        # apply any article rows on missing oam entries
        missing_oam = set(self.articlenumbers) - set(self.tables["oam_article2ofml"]["article"].tolist())
        any_articles_df = pd.DataFrame(columns="article ofml_type odb_name params".split(),
                                       data=[f"{_};::ofml::xoi::xOiAnyArticle;;".split(";") for _ in missing_oam])
        self.tables["oam_article2ofml"] = pd.concat([
            self.tables["oam_article2ofml"],
            any_articles_df
        ])

        self.tables["oam_article2odbparams"] = pd.read_sql(
            OamArticle2odbparams.query.filter(
                OamArticle2odbparams.article.in_(self.articlenumbers),
                OamArticle2odbparams.sql_db_program.in_(self.programs)
            ).statement,
            self.connection)

        self.tables["oam_property2mat"] = pd.read_sql(
            OamProperty2mat.query.filter(
                OamProperty2mat.article.in_(self.articlenumbers),
                OamProperty2mat.sql_db_program.in_(self.programs)
            ).statement,
            self.connection)

    def update(self):

        def replace_odb_name_in_oam(odb_name: str):
            fields = odb_name.split("::")
            logger.debug(f"replace_odb_name_in_oam:: ({len(fields)}) :: {fields}")
            if len(fields) == 4:
                program = fields[2]  # use program from odb_name_path
                return "::".join(fields[:2]) + f"::{self.program_name}" + f"::{fields[3].strip()}_{program.upper()}"
            else:
                return odb_name

        if self.exports_odb:
            self.tables["oam_article2ofml"]["odb_name"] = (self.tables["oam_article2ofml"].apply(
                lambda row: replace_odb_name_in_oam(row["odb_name"]),
                axis=1))

        def maybe_replace_ofml_type_in_oam(ofml_type: str):
            """
            supporting custom ofml_type too much work
            replace with default if it is custom
            """
            fields = ofml_type.split("::")
            if len(fields) == 4:
                _, manufacturer, program, cls = fields
                if manufacturer == "kn":
                    ofml_type = "::ofml::oi::OiOdbPlElement"
            return ofml_type

        self.tables["oam_article2ofml"]["ofml_type"] = (self.tables["oam_article2ofml"].apply(
            lambda row: maybe_replace_ofml_type_in_oam(row["ofml_type"]),
            axis=1))

    def export(self):
        remove_columns(self.tables)
        export_ofml_part(program_name=self.program_name,
                         export_path=self.path,
                         tables=self.tables,
                         inp_descr_content=table_descriptions.oam.INP_DESCR,
                         inp_descr_filename="oam.inp_descr")
