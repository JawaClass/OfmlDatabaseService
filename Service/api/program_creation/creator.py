from pathlib import Path
from typing import Optional
from Service import db
from Service.api import table_descriptions
from Service.api.program_creation.create_interface import CreateInterface
from Service.api.program_creation.go import GoCreator
from Service.api.program_creation.oam import OamCreator
from Service.api.program_creation.oas import OasCreator
from Service.api.program_creation.ocd import OcdCreator
from Service.api.program_creation.odb import OdbCreator
from Service.api.program_creation.ofml import OfmlCreator
from Service.tables.web.ocd import WebOcdArticle
from Service.api.program_creation.util import CreateProgramApiRequest
from settings import Config


class Creator:

    def __init__(self, *,
                 params: CreateProgramApiRequest):

        self.params = params
        self.connection = db.session.connection()
        self.articles: list[WebOcdArticle] = self._get_articles()
        self.articles_numbers = [a.article_nr for a in self.articles]
        self.programs = [a.sql_db_program for a in self.articles]
        self.export_path = Path(self.params.export_path) / self.params.program_name
        self.import_plaintext_path = Config.IMPORT_PLAINTEXT_PATH
        self.creators: dict[str, Optional[CreateInterface]] = {
            "ocd": None,
            "oam": None,
            "oas": None,
            "go": None,
            "ofml": None,
            "odb": None,
        }

    @staticmethod
    def _run_creator_pipeline(c: CreateInterface):
        c.load()
        c.update()
        c.export()

    def run_export_pipeline(self):
        if self.params.export_ocd:
            self._run_creator_pipeline(self.build_ocd_creator())
        if self.params.export_oas:
            self._run_creator_pipeline(self.build_oas_creator())
        if self.params.export_oam:
            self._run_creator_pipeline(self.build_oam_creator())
        if self.params.export_ofml:
            self._run_creator_pipeline(self.build_ofml_creator())
        if self.params.export_go:
            self._run_creator_pipeline(self.build_go_creator())
        if self.params.export_odb:
            self._run_creator_pipeline(self.build_odb_creator())
        if self.params.export_registry:
            self.export_registry()

    def export_registry(self):
        depend_programs = [] if self.params.export_odb else self.programs
        registry_file = self.export_path / f"kn_{self.params.program_name}_DE_2.cfg"
        registry_string = table_descriptions.registry.make_registry(self.params.program_name,
                                                                    self.params.program_id,
                                                                    depend_programs=depend_programs)
        registry_file.write_text(
            registry_string,
            encoding="cp1252"
        )

    def _get_articles(self):
        return WebOcdArticle.query.filter(
            WebOcdArticle.web_program_name == self.params.web_program_name,
            WebOcdArticle.web_filter == 0
        ).all()

    def build_ocd_creator(self):
        self.creators["ocd"] = OcdCreator(
            web_program_name=self.params.web_program_name,
            program_name=self.params.program_name,
            program_path=self.export_path,
            program_id=self.params.program_id
        )
        return self.creators["ocd"]

    def build_oam_creator(self):
        self.creators["oam"] = OamCreator(
            web_program_name=self.params.web_program_name,
            articlenumbers=self.articles_numbers,
            programs=self.programs,
            connection=self.connection,
            program_path=self.export_path,
            program_name=self.params.program_name,
            exports_odb=self.params.export_odb
        )
        return self.creators["oam"]

    def build_oas_creator(self):
        self.creators["oas"] = OasCreator(
            articles=self.articles,
            program_name=self.params.program_name,
            program_path=self.export_path
        )
        return self.creators["oas"]

    def build_go_creator(self):
        self.creators["go"] = GoCreator(
            articlenumbers=self.articles_numbers,
            program_path=self.export_path,
            program_name=self.params.program_name,
            connection=self.connection,
            programs=self.programs
        )
        return self.creators["go"]

    def build_ofml_creator(self):
        self.creators["ofml"] = OfmlCreator(
            program_path=self.export_path,
            program_name=self.params.program_name
        )
        return self.creators["ofml"]

    def build_odb_creator(self):
        if self.creators["oam"] is None:
            self.build_oam_creator()
        self.creators["odb"] = OdbCreator(
            program_path=self.export_path,
            program_name=self.params.program_name,
            connection=self.connection,
            programs=self.programs,
            import_plaintext_path=self.import_plaintext_path,
            oam=self.creators["oam"].tables
        )
        return self.creators["odb"]
