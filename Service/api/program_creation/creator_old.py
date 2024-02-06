import _csv
import csv
import re
import shutil
import time
from pathlib import Path
import pandas as pd
from Service import db
from Service.api.program_creation import TableDict
from Service.api.program_creation.go import GoCreator
from Service.api.program_creation.oam import OamCreator
from Service.api.program_creation.ocd import OcdCreator
from Service.api.program_creation.oas import OasCreator
from Service.api.program_creation.odb import OdbCreator
from Service.api.program_creation.ofml import OfmlCreator
from Service.api.program_creation.util import remove_columns
from Service.tables.oam import OamArticle2ofml, OamProperty2mat, OamArticle2odbparams
from Service.tables.go import GoArticles, GoProperties, GoTypes, GoDeSr
from Service.tables.odb import Odb2d, Odb3d, Funcs, Layer, Attpt, Oppattpt, Stdattpt
from sqlalchemy.engine.base import Connection
from Service.api import table_descriptions
from settings import Config
from loguru import logger


class ProgramCreator:
    @property
    def ocd(self):
        return self.ocd_creator.tables

    @property
    def oam(self):
        return self.oam_creator.tables

    @property
    def oas(self):
        return self.oas_creator.tables

    @property
    def go(self):
        return self.go_creator.tables

    @property
    def ofml(self):
        return self.ofml_creator.tables

    @property
    def odb(self):
        return self.odb_creator.tables

    def make_program_path(self, delete_folder_if_exists=True):
        base_path = Path(Config.CREATE_OFML_EXPORT_PATH)

        if delete_folder_if_exists:
            if (base_path / self.program_name).exists():
                shutil.rmtree((base_path / self.program_name), ignore_errors=True)
                time.sleep(0.1)

        folder_name = (self.program_name
                       if not (base_path / self.program_name).exists()
                       else f"{self.program_name}_{time.time()}")

        program_path = base_path / folder_name
        program_path.mkdir()
        self.export_program_path = program_path
        self.export_program_path_windows = Path(r"B:\ofml_development\Tools\ofml_datenmacher") / folder_name

    def __init__(self, body):
        self.logs = []
        logger.add(lambda msg: self.logs.append(msg))
        logger.debug("ProgramCreator START")
        self.body = body
        self.program_name = body["programName"]
        self.program_id = body["programID"]
        self.articlenumbers = [_["articleNr"] for _ in body["articleItems"]]
        self.programs = list(set([_["program"] for _ in body["articleItems"]]))
        self.exports: {} = body["exports"]
        logger.debug("read parameters")

        self.import_plaintext_path: Path = Config.IMPORT_PLAINTEXT_PATH
        self.export_program_path: None | Path = None
        self.export_program_path_windows: None | Path = None
        self.article_items = self.body["articleItems"]
        self.property_items = self.body["propertyItems"]

        self.depend_programs = self.programs if self.exports["odb"] else []
        self.make_program_path()

        self.ocd_creator = OcdCreator(
            program_path=self.export_program_path
        )
        self.oam_creator = OamCreator(
            articlenumbers=self.articlenumbers,
            programs=self.programs,
            connection=db.session.connection(),
            program_path=self.export_program_path,
            program_name=self.program_name,
            exports_odb=self.exports["odb"]
        )
        self.oas_creator = OasCreator(
            article_items=self.article_items,
            program_name=self.program_name,
            program_path=self.export_program_path
        )
        self.ofml_creator = OfmlCreator(
            program_path=self.export_program_path,
            program_name=self.program_name
        )
        self.go_creator = GoCreator(
            articlenumbers=self.articlenumbers,
            program_path=self.export_program_path,
            program_name=self.program_name,
            connection=db.session.connection(),
            programs=self.programs
        )
        self.oam_creator.load()
        for creator in [
            self.ocd_creator,
            # self.oam_creator,
            self.oas_creator,
            self.go_creator,
            self.ofml_creator
        ]:
            creator.load()
            creator.update()

        assert self.oam_creator.tables

        self.odb_creator = OdbCreator(
            article_items=self.article_items,
            program_path=self.export_program_path,
            program_name=self.program_name,
            connection=db.session.connection(),
            programs=self.programs,
            import_plaintext_path=self.import_plaintext_path,
            oam=self.oam_creator.tables
        )
        if self.exports["odb"]:
            self.odb_creator.load()
            self.odb_creator.update()

        self.oam_creator.update()

        self.update_article_nr()
        self.export_all()

        logger.debug("ProgramCreator DONE")
        log_file = self.export_program_path / f"{self.program_name}.logs"
        log_file.write_text("".join(self.logs))

    def export_all(self):
        logger.debug("export :: BEGIN")
        assert self.export_program_path
        parts = [
            self.ocd_creator,
            self.oam_creator,
            self.oas_creator,
            self.go_creator,
            self.ofml_creator,
        ]
        if self.export_odb:
            parts.append(self.odb_creator)
        for creator in parts:
            creator.export()

        registry_file = self.export_program_path / f"kn_{self.program_name}_DE_2.cfg"
        registry_file.write_text(
            table_descriptions.registry.make_registry(self.program_name,
                                                      self.program_id,
                                                      depend_programs=self.depend_programs),
            encoding="cp1252"
        )
        logger.debug("export :: DONE")
    #
    # def update_article_nr(self):
    #     for article_item in self.article_items:
    #         article_nr = article_item["articleNr"]
    #         replacement = article_item["articleNrAlias"]
    #
    #         self.ocd["ocd_article"].loc[lambda x: x["article_nr"] == article_nr, "article_nr"] = replacement
    #         self.ocd["ocd_artbase"].loc[lambda x: x["article_nr"] == article_nr, "article_nr"] = replacement
    #         self.ocd["ocd_propertyclass"].loc[lambda x: x["article_nr"] == article_nr, "article_nr"] = replacement
    #         self.ocd["ocd_price"].loc[lambda x: x["article_nr"] == article_nr, "article_nr"] = replacement
    #         self.ocd["ocd_articletaxes"].loc[lambda x: x["article_nr"] == article_nr, "article_nr"] = replacement
    #         self.ocd["ocd_packaging"].loc[lambda x: x["article_nr"] == article_nr, "article_nr"] = replacement
    #
    #         self.oam["oam_article2ofml"].loc[lambda x: x["article"] == article_nr, "article"] = replacement
    #         self.oam["oam_article2odbparams"].loc[lambda x: x["article"] == article_nr, "article"] = replacement
    #         self.oam["oam_property2mat"].loc[lambda x: x["article"] == article_nr, "article"] = replacement
    #
    #         self.oas["article"].loc[lambda x: x["p1"] == article_nr, "p1"] = replacement
    #         self.oas["structure"].loc[lambda x: x["p1"] == article_nr, "p1"] = replacement
    #         self.oas["text"].loc[lambda x: x["p1"] == article_nr, "p1"] = replacement
    #         self.oas["resource"].loc[lambda x: x["p1"] == article_nr, "p1"] = replacement
    #
    #         self.go["go_articles"].loc[lambda x: x["article_nr"] == article_nr, "article_nr"] = replacement





