import subprocess

import pandas as pd
from loguru import logger
from Service.api import table_descriptions
from Service.api.program_creation.create_interface import CreateInterface
from Service.api.program_creation.util import export_ofml_part, remove_columns
from settings import Config


class OfmlCreator(CreateInterface):

    def __init__(self, program_name, program_path):
        self.program_name = program_name
        self.tables = {}
        self.program_path = program_path
        self.path = program_path / "2"

    def load(self):
        logger.debug("make_ofml_tables")
        self.tables["epdfproductdb"] = pd.DataFrame(
            data=["@SafePropertyNames;;1".split(";")],
            columns="type;args;value".split(";")
        )
        self.tables["plelement"] = pd.DataFrame(
            data=["@UseOAM;;1".split(";")],
            columns="type;args;value".split(";")
        )

    def update(self):
        ...

    def export(self):
        remove_columns(self.tables)
        export_ofml_part(program_name=self.program_name,
                         export_path=self.path,
                         tables=self.tables,
                         inp_descr_content=table_descriptions.ofml.INP_DESCR,
                         inp_descr_filename="ofml.inp_descr")

    def build_ebase(self):
        print("ofml build ebase!!")
        tables_folder = self.path
        inp_descr_filepath = tables_folder / "ofml.inp_descr"
        ebase_filepath = tables_folder / "ofml.ebase"
        command = f"{Config.CREATE_EBASE_EXE} -d {tables_folder} {inp_descr_filepath} {ebase_filepath}"
        print("ofml command", command)
        subprocess.run(command)
