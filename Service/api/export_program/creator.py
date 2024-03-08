import copy
import sys

from Service.api.export_program.create_interface import CreateInterface
from Service.api.export_program.go import GoCreator
from Service.api.export_program.oam import OamCreator
from Service.api.export_program.oas import OasCreator
from Service.api.export_program.ocd import OcdCreator
from Service.api.export_program.odb import OdbCreator
from Service.api.export_program.ofml import OfmlCreator
from Service.api.export_program.table_descriptions.registry import make_registry
from Service.tables.web.ocd import WebOcdArticle
from Service.api.export_program.util import CreateProgramApiRequest
from settings import Config
from pathlib import Path
import subprocess
from Service import db
import threading
import time


class Creator:

    def _translate_export_path(self):
        if self.params.export_path == "TEST_ENV":
            return Config.EXPORT_DATA_PATH_TEST_ENV
        return Config.EXPORT_DATA_PATH_DEFAULT

    def __init__(self, *,
                 params: CreateProgramApiRequest):
        self.thread_id = threading.get_ident()

        """ create a new loguru logger instance for creator-logs and write to STDOUT and FILE"""
        from Service.util import template_logger
        self.logger = template_logger.new_loguru_logger()

        self.logger.add(sink=sys.stdout, level=0)

        self.params = params
        self.export_path: Path = self._translate_export_path() / self.params.program_name

        self.logger.add(sink=self.export_path / "datenmacher.logs", level=0, mode="w+")
        self.logger.info("Init parameters")

        self.connection = db.session.connection()
        self.articles: list[WebOcdArticle] = self._get_articles()
        self.articles_numbers = [a.article_nr for a in self.articles]
        self.programs = list(set([a.sql_db_program for a in self.articles]))

        self.import_plaintext_path: Path = Config.IMPORT_PLAINTEXT_PATH

        self.logger.info(f"export_path: {self.export_path}")
        self.logger.info(f"import_plaintext_path: {self.import_plaintext_path}")

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
            command = Config.CREATE_EBASE_EXE
            param = str(self.export_path)
            subprocess.Popen([command, param])
        self.logger.info("DONE.")

    def export_registry(self):
        depend_programs = [] if self.params.export_odb else self.programs
        registry_file = self.export_path / f"kn_{self.params.program_name}_DE_2.cfg"
        registry_string = make_registry(self.params.program_name,
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
            program_id=self.params.program_id,
            logger=self.logger
        )

    def build_oam_creator(self):
        return OamCreator(
            web_program_name=self.params.web_program_name,
            articlenumbers=self.articles_numbers,
            programs=self.programs,
            connection=self.connection,
            program_path=self.export_path,
            program_name=self.params.program_name,
            exports_odb=self.params.export_odb,
            logger=self.logger
        )

    def build_oas_creator(self):
        return OasCreator(
            articles=self.articles,
            program_name=self.params.program_name,
            program_path=self.export_path,
            logger=self.logger
        )

    def build_go_creator(self):
        return GoCreator(
            articlenumbers=self.articles_numbers,
            program_path=self.export_path,
            program_name=self.params.program_name,
            connection=self.connection,
            programs=self.programs,
            logger=self.logger
        )

    def build_ofml_creator(self):
        return OfmlCreator(
            program_path=self.export_path,
            program_name=self.params.program_name,
            logger=self.logger
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
            oam=oam_creator.tables,
            logger=self.logger
        )
