import re
import shutil
from pathlib import Path
import pandas as pd
from loguru import logger
from sqlalchemy.engine.base import Connection
from Service.api.export_program import Tables
from Service.api.export_program.create_interface import CreateInterface
from Service.api.export_program.util import export_ofml_part, unify_column_linkages, remove_columns, \
    build_ebase_command, execute_build_ebase_command
from Service.tables.odb import Funcs, Layer, Attpt, Oppattpt, Odb2d, Stdattpt, Odb3d
from Service.api.export_program.table_descriptions.odb import INP_DESCR


class OdbCreator(CreateInterface):

    def __init__(self, *,
                 program_name,
                 connection,
                 oam,
                 programs,
                 import_plaintext_path,
                 program_path):
        self.program_name = program_name
        self.tables = {}
        self.connection = connection
        self.oam = oam
        self.programs = programs
        self.import_plaintext_path = import_plaintext_path
        self.program_path = program_path
        self.path = self.program_path / "2"

    def _copy_odb_graphic_files(self):
        logger.debug("copy_odb_graphic_files ::BEGIN")

        self.path.mkdir(parents=True, exist_ok=True)

        def graphic_or_none(field: str, graphics_pattern: re.Pattern):
            match = re.search(graphics_pattern, field)
            if match:
                return match.group(1)
            return None

        graphics_pattern_3d = re.compile(r"\"(.+)\".+imp")
        graphics_pattern_2d = re.compile(r"\"(.+)\".+egms")

        copied_tracker: set[Path] = set()

        def copy_graphic_file(field: str, file_ext: list[str]):
            fields = field.split("::")
            program_name = fields[2].lower()
            file_name = fields[3].lower()
            logger.debug("copy file")
            graphics_root_folder = self.import_plaintext_path / program_name / "2"
            for file_ext in file_ext:
                graphics_path = graphics_root_folder / f"{file_name}.{file_ext}"
                if graphics_path in copied_tracker:
                    continue
                copied_tracker.add(graphics_path)
                graphics_path_exists = graphics_path.exists()
                if not graphics_path_exists:
                    logger.warning(
                        f"Referenced Graphics file '{graphics_path}' not found in path"
                        f"'{graphics_root_folder}' referenced in '{field}'."
                    )
                    continue

                graphics_path_dst = self.path / f"{file_name}_{program_name}.{file_ext}"  # TODO: (not sure) program_name shoudl come from self.odb["odb2d"]["sql_db_program"]
                logger.debug(f"copy {graphics_path} ... {graphics_path_dst}")
                shutil.copyfile(src=graphics_path, dst=graphics_path_dst)

        graphics_3d = (
            pd.Series(
                self.tables["odb3d"]["ctor"].apply(lambda x: graphic_or_none(x, graphics_pattern_3d)).dropna().unique())
        )
        graphics_3d.apply(lambda x: copy_graphic_file(x, ["dwg", "geo"]))

        graphics_2d = (
            pd.Series(
                self.tables["odb2d"]["ctor"].apply(lambda x: graphic_or_none(x, graphics_pattern_2d)).dropna().unique())
        )
        graphics_2d.apply(lambda x: copy_graphic_file(x, ["egms", "dwg"]))
        logger.debug("copy_odb_graphic_files ::DONE")

    def load(self):

        assert len(self.oam)

        odb_loader = OdbLoader(self.connection)
        for idx, row in self.oam["oam_article2ofml"].iterrows():
            if len(row["odb_name"].strip()):
                load_2d_success = odb_loader.load_odb2d_object(odb_name_path=row["odb_name"])
                load_3d_success = odb_loader.load_odb3d_object(odb_name_path=row["odb_name"])
                if not (load_2d_success and load_3d_success):
                    logger.warning(
                        f"odb_loader.load_ :: Did not complete successful for both"
                        f"2D ({load_2d_success}) and 3D ({load_3d_success}). Replace oam mapping with AnyArticle. "
                    )

                    self.oam["oam_article2ofml"].loc[idx, ["ofml_type", "odb_name", "params"]] = (
                        "::ofml::xoi::xOiDummyArticle", "", ""
                    )
            else:
                logger.info(f"odb_loader.load_ :: IGNORE because odb_name is empty :: {row.to_dict()}")
        odb_loader.load_other_tables_from_programs(self.programs)

        self.tables = odb_loader.odb

    def _odb_funcs_make_properties_safe(self):
        unsafe_property_pattern = re.compile(r"\$\{([_a-zA-Z][_a-zA-Z0-9]*?__.+?):-.+?\}")
        self.tables["funcs"]["body"] = (
            self.tables["funcs"]["body"].apply(
                lambda body: unsafe_property_pattern.sub(lambda match: match.group().replace("__", "_"), body)
            )
        )

    def update(self):
        if self.tables.get("odb2d", None) is not None and self.tables.get("odb3d", None) is not None:
            self._odb_funcs_make_properties_safe()
            self._copy_odb_graphic_files()
            self._unify_links()

    def _unify_links(self):
        odb_links = {
            "attpt": ["odb_name"],
            "funcs": ["name"],
            "layer": ["layer_name"],
            "odb2d": ["odb_name"],
            "odb3d": ["odb_name"],
            "oppattpt": ["odb_name"],
            "stdattpt": ["odb_name"]
        }

        def replace_tokens_in_expression(expression: str, program: str):
            """
              unify linkages that are part of expression
            """
            token_pattern = re.compile(r"(?:(?<= |-)|(?<=^))([_a-zA-Z][_a-zA-Z0-9]+)")

            def replace_token_maybe(match):
                token = match.group()
                if not self.tables["funcs"].loc[lambda x: (x["name"] == token) & (x["sql_db_program"] == program)].empty:
                    return f"{token}_{program.upper()}"
                else:
                    return token

            return token_pattern.sub(replace_token_maybe, expression)

        for table, columns in {
            "odb2d": ["visible", "x_offs", "y_offs", "rot", "x_scale", "y_scale", "ctor"],
            "odb3d": ["visible", "x_offs", "y_offs", "z_offs", "x_rot", "y_rot", "z_rot", "mat", "ctor"],
            "funcs": ["body"]
        }.items():
            for column in columns:
                self.tables[table][column] = (
                    self.tables[table].apply(
                        lambda row: replace_tokens_in_expression(row[column], row["sql_db_program"]),
                        axis=1)
                )

        def replace_odb3d_layer(field: str, program: str, layer_pattern: re.Pattern):
            match = layer_pattern.search(field)
            if match:
                layer = match.group(1)
                field = field.replace(layer, f"{layer}_{program.upper()}")
            return field

        odb_layer_pattern = re.compile(r"\"(.+)\"\s+layer")
        self.tables["odb3d"]["attrib"] = (
            self.tables["odb3d"].apply(
                lambda row: replace_odb3d_layer(row["attrib"], row["sql_db_program"], odb_layer_pattern),
                axis=1)
        )

        def replace_odb_path_name(field: str, ctor_pattern: re.Pattern):
            """
            replace odb_path to current program and add suffix to odb_name
            """
            match = ctor_pattern.search(field)
            if match:
                print("replace_odb_path_name::", field, "groups::", match.groups(), len(match.groups()))
                odb_graphic_program = match.group(1).lower()
                odb_graphic_name = match.group(2)
                param = match.group(3).strip()
                field = f"\"::kn::{self.program_name}::{odb_graphic_name}_{odb_graphic_program}\" {param}"
            return field

        odb3d_ctor_pattern = re.compile(r"\"::kn::(.+?)::(.+)\"(.+imp)")
        self.tables["odb3d"]["ctor"] = (
            self.tables["odb3d"].apply(
                lambda row: replace_odb_path_name(row["ctor"], odb3d_ctor_pattern),
                axis=1)
        )

        odb2d_ctor_pattern = re.compile(r"\"::kn::(.+?)::(.+)\"(.+egms)")
        self.tables["odb2d"]["ctor"] = (
            self.tables["odb2d"].apply(
                lambda row: replace_odb_path_name(row["ctor"], odb2d_ctor_pattern),
                axis=1)
        )

        unify_column_linkages(odb_links, self.tables)

    def export(self):
        remove_columns(self.tables)
        export_ofml_part(program_name=self.program_name,
                         export_path=self.path,
                         tables=self.tables,
                         inp_descr_content=INP_DESCR,
                         inp_descr_filename="odb.inp_descr")

    def build_ebase(self):
        command = build_ebase_command(tables_folder=self.path,
                                      inp_descr_filepath=self.path / "odb.inp_descr",
                                      ebase_filepath=self.path / f"odb.ebase")
        execute_build_ebase_command(command)


class OdbLoader:

    def __init__(self, con: Connection):
        self.con = con
        self.odb: Tables = {}

    def load_other_tables_from_programs(self, programs: [str]):
        for cls in [Funcs, Layer, Attpt, Oppattpt, Stdattpt]:
            self._load_table_from_programs(cls, programs)

    def _load_table_from_programs(self, cls, programs: [str]):
        self.odb[cls.__tablename__] = pd.read_sql(
            cls.query.filter(
                cls.sql_db_program.in_(programs)
            ).statement,
            self.con)

    def load_odb2d_object(self, odb_name_path: str):
        logger.debug(f"load_odb2d_object:: {odb_name_path}")
        return self._load_odb_object(odb_name_path, Odb2d)

    def load_odb3d_object(self, odb_name_path: str):
        logger.debug(f"load_odb3d_object:: {odb_name_path}")
        return self._load_odb_object(odb_name_path, Odb3d)

    def _load_odb_object(self, odb_name_path: str, cls: Odb3d | Odb2d) -> bool:
        """
        returns True if load successful
        returns False otherwise
        """
        program, odb_name = odb_name_path.split("::")[2:4]
        logger.debug(f"_load_odb_object:: {odb_name_path} :program={program} :odb_name={odb_name}")

        odb_start_row: cls = cls.query.filter(
            cls.odb_name == odb_name,
            cls.sql_db_program == program
        ).first()
        if odb_start_row is None:
            logger.warning(f"_load_odb_object:: {odb_name_path} :program={program} :odb_name={odb_name} not found.")
            return False

        start_idx = odb_start_row.db_key
        odb_end_row: cls = cls.query.filter(
            cls.odb_name != "",
            cls.sql_db_program == program,
            cls.db_key > odb_start_row.db_key
        ).first()

        if odb_end_row is None:
            print("odb_end_row is None")
            # get last row if end-row is not indicated by follow-up object (not yet tested)
            odb_end_row: cls = cls.query.filter(
                cls.sql_db_program == program,
                cls.db_key >= odb_start_row.db_key
            ).order_by(cls.db_key.desc()).first()
            print("now::", odb_end_row)
            end_idx = odb_end_row.db_key
        else:
            end_idx = odb_end_row.db_key - 1

        df = pd.read_sql(cls.query.filter(
            cls.sql_db_program == program,
            cls.db_key >= start_idx,
            cls.db_key <= end_idx,
        ).statement, self.con)

        if cls.__tablename__ not in self.odb:
            self.odb[cls.__tablename__] = df
        else:
            # keep odb objects unique
            if self.odb[cls.__tablename__].loc[lambda x: x["odb_name"] == odb_name].empty:
                # TODO: FutureWarning: The behavior of DataFrame concatenation with empty or all-NA entries is deprecated. In a future version, this will no longer exclude empty or all-NA columns when determining the result dtypes. To retain the old behavior, exclude the relevant entries before the concat operation.
                #   self.odb[cls.__tablename__] = pd.concat([self.odb[cls.__tablename__], df]).reset_index(drop=True)
                if df.empty:
                    print("df EMPTY !!!!", odb_name_path, cls)
                    input("________")
                self.odb[cls.__tablename__] = pd.concat([self.odb[cls.__tablename__], df]).reset_index(drop=True)
        return True
