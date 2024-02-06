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

    def _translate_export_path(self):
        if self.params.export_path == "TEST_ENV":
            return Config.EXPORT_DATA_PATH_TEST_ENV
        return Config.EXPORT_DATA_PATH_DEFAULT

    def __init__(self, *,
                 params: CreateProgramApiRequest):

        self.params = params
        self.connection = db.session.connection()
        self.articles: list[WebOcdArticle] = self._get_articles()
        self.articles_numbers = [a.article_nr for a in self.articles]
        self.programs = [a.sql_db_program for a in self.articles]
        self.export_path: Path = self._translate_export_path() / self.params.program_name
        self.import_plaintext_path: Path = Config.IMPORT_PLAINTEXT_PATH

    def _run_creator_pipeline(self, c: CreateInterface):
        c.load()
        c.update()
        c.export()
        if self.params.build_ebase:
            c.build_ebase()

    def run_export_pipeline(self):
        self.export_path.mkdir(parents=True, exist_ok=True)
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
        if self.params.build_ebase:
            # "B:\ofml_development\Tools\create_ebase.bat"
            print("build ebase 1")
            import subprocess
            command = Config.CREATE_EBASE_EXE
            param = str(self.export_path)
            ""
            subprocess.Popen([command, param])
            print("build ebase 2")

    def export_registry(self):
        depend_programs = [] if self.params.export_odb else self.programs
        registry_file = self.export_path / f"kn_{self.params.program_name}_DE_2.cfg"
        registry_string = table_descriptions.registry.make_registry(self.params.program_name,
                                                                    self.params.program_id,
                                                                    depend_programs=depend_programs,
                                                                    with_meta=self.params.export_go)
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
        return OcdCreator(
            web_program_name=self.params.web_program_name,
            program_name=self.params.program_name,
            program_path=self.export_path,
            program_id=self.params.program_id
        )

    def build_oam_creator(self):
        return OamCreator(
            web_program_name=self.params.web_program_name,
            articlenumbers=self.articles_numbers,
            programs=self.programs,
            connection=self.connection,
            program_path=self.export_path,
            program_name=self.params.program_name,
            exports_odb=self.params.export_odb
        )

    def build_oas_creator(self):
        return OasCreator(
            articles=self.articles,
            program_name=self.params.program_name,
            program_path=self.export_path
        )

    def build_go_creator(self):
        return GoCreator(
            articlenumbers=self.articles_numbers,
            program_path=self.export_path,
            program_name=self.params.program_name,
            connection=self.connection,
            programs=self.programs
        )

    def build_ofml_creator(self):
        return OfmlCreator(
            program_path=self.export_path,
            program_name=self.params.program_name
        )

    def build_odb_creator(self):
        oam_creator = self.build_oam_creator()
        oam_creator.load()
        return OdbCreator(
            program_path=self.export_path,
            program_name=self.params.program_name,
            connection=self.connection,
            programs=self.programs,
            import_plaintext_path=self.import_plaintext_path,
            oam=oam_creator.tables
        )
