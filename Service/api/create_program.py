import time
from pathlib import Path
import pandas as pd
from .. import db
from .db import yield_all_tables
from ..tables import OamArticle2ofml, OamProperty2mat, OamArticle2odbparams, GoArticles, GoProperties, GoTypes
from sqlalchemy.engine.base import Connection
from . import table_descriptions
from settings import Config
TableDict = dict[str, dict[str, pd.DataFrame]]


class ProgramCreator:

    def __init__(self, body):

        print("ProgramCreator START")
        self.body = body
        self.program_name = body["programName"]
        self.program_id = body["programID"]

        self.articlenumbers = [_["articleNr"] for _ in body["articleItems"]]
        self.programs = list(set([_["program"] for _ in body["articleItems"]]))

        self.export_program_path = None

        self.article_items = self.body["articleItems"]
        self.property_items = self.body["propertyItems"]
        self.tables: TableDict = {
            "ocd": {},
            "oam": {},
            "oas": {},
            "go": {},
            "oap": {},
        }
        self.ocd = self.tables["ocd"]
        self.oam = self.tables["oam"]
        self.oas = self.tables["oas"]
        self.go = self.tables["go"]

        self.load_ocd_tables()

        self.update_shorttext()
        self.update_artbase()
        self.update_properties()
        self.update_prices()
        self.update_longtext()
        self.update_article()

        self.unify_linking_keys()

        self.load_oam_tables()

        self.make_oas_tables()

        self.load_go_tables()
        self.update_go_tables()

        self.update_article_nr()

        self.remove_columns()

        self.export()

    @staticmethod
    def _get_encoding(table_name: str):
        return "cp1252" if table_name.endswith("text") or table_name.endswith("txt") else None

    def update_article(self):
        self.ocd["ocd_article"]["series"] = self.program_id

    def export(self):
        base_path = Path(Config.CREATE_OFML_EXPORT_PATH)

        if not (base_path / self.program_name).exists():
            program_path = base_path / self.program_name
        else:
            program_path = base_path / f"{self.program_name}_{time.time()}"

        program_path.mkdir()
        self.export_program_path = str(program_path)

        # export ocd
        ocd_path = program_path / "DE" / "2" / "db"
        ocd_path.mkdir(parents=True, exist_ok=True)
        for table_name in self.ocd:
            df = self.ocd[table_name]
            file_name = f"{table_name}.csv"
            encoding = self._get_encoding(table_name)
            df.to_csv(ocd_path / file_name, header=False, index=False, index_label=False, sep=";", encoding=encoding)

        (ocd_path / "pdata.inp_descr").write_text(table_descriptions.ocd.INP_DESCR)

        # export oam
        oam_path = program_path / "DE" / "2" / "oam"
        oam_path.mkdir(parents=True, exist_ok=True)
        for table_name in self.oam:
            df = self.oam[table_name]
            file_name = f"{table_name}.csv"
            df.to_csv(oam_path / file_name, header=False, index=False, index_label=False, sep=";")

        (oam_path / "oam.inp_descr").write_text(table_descriptions.oam.INP_DESCR)

        # export oas
        oam_path = program_path / "DE" / "2" / "cat"
        oam_path.mkdir(parents=True, exist_ok=True)
        for table_name in self.oas:
            df = self.oas[table_name]
            file_name = f"{table_name}.csv"
            encoding = self._get_encoding(table_name)
            df.to_csv(oam_path / file_name, header=False, index=False, index_label=False, sep=";", encoding=encoding)

        # export go
        go_path = program_path / "2"
        go_path.mkdir(parents=True, exist_ok=True)
        for table_name in self.go:
            df = self.go[table_name]
            file_name = f"{table_name}.csv"
            df.to_csv(go_path / file_name, header=False, index=False, index_label=False, sep=";")

        (go_path / "mt.inp_descr").write_text(table_descriptions.go.INP_DESCR)

        # export registry
        (program_path / f"kn_{self.program_name}_DE_2.cfg").write_text(
            table_descriptions.registry.make_registry(self.program_name, self.program_id, self.programs),
            encoding="cp1252"
            )

    def unify_linking_keys(self):
        """
        make links between tables unique per program
        """

        links = {
            "ocd_artbase": ["prop_class"],
            "ocd_article": ["short_textnr", "long_textnr", "rel_obj", "scheme_id"],
            "ocd_articletaxes": ["tax_id"],
            "ocd_artlongtext": ["textnr"],
            "ocd_artshorttext": ["textnr"],
            "ocd_codescheme": ["scheme_id"],
            "ocd_price": ["rounding_id"],
            "ocd_pricetext": ["textnr"],
            "ocd_propclasstext": ["textnr"],
            "ocd_property": ["prop_textnr", "hint_text_id", "prop_class"],
            "ocd_propertyclass": ["textnr", "prop_class"],
            "ocd_propertytext": ["textnr"],
            "ocd_propertyvalue": ["pval_textnr", "rel_obj", "prop_class"],
            "ocd_prophinttext": ["textnr"],
            "ocd_propvaluetext": ["textnr"],
            "ocd_relation": ["rel_name"],
            "ocd_relationobj": ["rel_obj", "rel_name"],
            "ocd_rounding": ["id"],
            "ocd_taxscheme": ["tax_id"],

            "optproperty_dat": ["prop_class", "prop_textnr"],
            "optpropvalue_txt": ["textnr"],
        }

        class HashMaker:
            def __init__(self):
                self.hashes = {}

            def get(self, input_string: str) -> int:

                if (stored_hash := self.hashes.get(input_string, None)) is not None:
                    return stored_hash

                self.hashes[input_string] = 1 + len(self.hashes)
                return self.hashes[input_string]

        hash_maker = HashMaker()

        for table_name in links:

            if self.ocd[table_name].empty:
                continue

            linking_columns = links[table_name]

            self.ocd[table_name][linking_columns] = self.ocd[table_name][linking_columns]

            def update_link(column: pd.Series):
                """
                apply the new links at column values where it's not an empty string / 0
                """
                assert type(column) is pd.Series

                dtype_ = column.dtype
                is_string = pd.api.types.is_string_dtype(dtype_)
                idx = column.loc[column.astype(bool)].index

                if is_string:
                    column[idx] = (
                            column[idx] +
                            (self.ocd[table_name]["sql_db_program"][idx].apply(lambda x: f"_{x.upper()}"))
                    )
                else:
                    column[idx] = (
                            column[idx].astype("string").fillna("") +
                            self.ocd[table_name]["sql_db_program"][idx]
                    ).apply(hash_maker.get).astype(dtype_)
                return column

            self.ocd[table_name][linking_columns] = self.ocd[table_name][linking_columns].apply(update_link, axis=0)

    def remove_columns(self):
        for ofml_part in self.tables:
            self._remove_columns(self.tables[ofml_part])

    @staticmethod
    def _remove_columns(ofml_part):
        drop_columns = ["sql_db_program", "sql_db_timestamp_modified", "sql_db_timestamp_read", "db_key", "index"]

        for table_name in ofml_part:
            if "sql_db_program" not in ofml_part[table_name].columns:
                print("INFO - no sql_db_program:::", table_name)
                continue

            if ofml_part[table_name].empty:
                print("INFO - EMPTY_TABLE:::", table_name)

            ofml_part[table_name].drop(
                columns=drop_columns,
                inplace=True)

    def load_ocd_tables(self):
        print("load_ocd_tables..................")
        for _ in yield_all_tables(self.articlenumbers, self.programs):
            table_name = _["table"]
            # print("table_name", table_name)
            table_content = _["content"]
            self.ocd[table_name] = pd.DataFrame(table_content)

        # update ocd_version
        table_names = [_.replace("ocd_", "") for _ in list(self.ocd.keys())]
        self.ocd["ocd_version"].loc[
            0,
            "tables"] = ",".join(table_names)

    def update_properties(self):
        print("update_properties", len(self.property_items))
        for program in self.property_items:
            print("program:", program)
            for p_class in self.property_items[program]:
                print(" pClass", p_class)
                for prop_item in self.property_items[program][p_class]:
                    print("  ", prop_item)
                    should_deactivate = not bool(prop_item["active"])
                    property_ = prop_item["property"]
                    if should_deactivate:
                        print("Deactivate Property!", property_)

                        self.ocd["ocd_property"].loc[
                            lambda x: (x["prop_class"] == p_class) &
                                      (x["property"] == property_) &
                                      (x["sql_db_program"] == program),
                            "scope"
                        ] = "G"

                    # delete values
                    value_items = prop_item["values"]
                    for value_item in value_items:
                        print(value_item)
                        should_delete = not bool(value_item["active"])
                        if should_delete:
                            value = value_item["value"]
                            to_delete = self.ocd["ocd_propertyvalue"].loc[
                                lambda x: (x["prop_class"] == p_class) &
                                          (x["property"] == property_) &
                                          (x["value_from"] == value) &
                                          (x["sql_db_program"] == program)
                            ].index
                            self.ocd["ocd_propertyvalue"].drop(to_delete, inplace=True)

    def update_artbase(self):
        """
        iterate over all article_items
        - if artbase was changed on client purge all
          entries and insert new one
        """
        for article_item in self.article_items:
            article_nr = article_item["articleNr"]
            artbase = article_item["artbaseItems"]
            program = article_item["program"]
            artbase_changed = bool(artbase)

            if artbase_changed:
                # print("ARTBASE changed", article_nr, len(artbase))
                # purge this articles artbase
                to_delete = self.ocd["ocd_artbase"].loc[lambda x: x["article_nr"] == article_nr].index
                self.ocd["ocd_artbase"].drop(to_delete, inplace=True)
                assert self.ocd["ocd_artbase"].loc[lambda x: x["article_nr"] == article_nr].empty
                for item in artbase:
                    # print(item)
                    # add row
                    self.ocd["ocd_artbase"].loc[-1] = {
                        "article_nr": article_nr,
                        "prop_class": item["pClass"],
                        "property": item["property"],
                        "prop_value": item["value"],
                        "sql_db_program": program,
                    }

                    self.ocd["ocd_artbase"].index += 1
                    self.ocd["ocd_artbase"] = self.ocd["ocd_artbase"].sort_index()

        # print(self.ocd["ocd_artbase"].to_string())

    def update_prices(self):
        # self.ocd["ocd_price"]
        for article_item in self.article_items:

            price = article_item["price"]
            if price is None:
                continue
            print("update price", price, type(price))
            print(article_item)
            article_nr = article_item["articleNr"]
            # print("update_prices", price, article_nr)
            self.ocd["ocd_price"].loc[
                lambda x: (x["article_nr"] == article_nr) & (x["price_type"] == "S") & (x["price_level"] == "B"),
                "price"] = price

    def update_shorttext(self):
        # TODO: if no shorttext exists yet we dont create it
        """
        iterate over all article_items
        - set the shorttext of the given item in the
          ocd_artshorttext Dataframe table
        """
        for article_item in self.article_items:
            article_nr = article_item["articleNr"]
            shorttext_ids = pd.merge(
                self.ocd["ocd_article"].loc[lambda x: x["article_nr"] == article_nr],
                self.ocd["ocd_artshorttext"].loc[lambda x: x["language"] == "de"],
                left_on="short_textnr",
                right_on="textnr"
            )["short_textnr"]

            self.ocd["ocd_artshorttext"].loc[
                lambda x: x["textnr"].isin(shorttext_ids) & (x["language"] == "de"), "text"
            ] = article_item["shorttext"]

    def update_longtext(self):
        # TODO: if no longtext exists yet we dont create it
        df_data = []
        for article_item in self.article_items:
            article_nr = article_item["articleNr"]
            long_text = article_item["longText"]
            program = article_item["program"]
            if long_text is None:
                continue

            longtext_ids = pd.merge(
                self.ocd["ocd_article"].loc[lambda x: x["article_nr"] == article_nr],
                self.ocd["ocd_artlongtext"].loc[lambda x: x["language"] == "de"],
                left_on="long_textnr",
                right_on="textnr"
            )["long_textnr"]

            to_removed_df = self.ocd["ocd_artlongtext"].loc[lambda x: x["textnr"].isin(longtext_ids)]
            self.ocd["ocd_artlongtext"] = self.ocd["ocd_artlongtext"].drop(to_removed_df.index)

            text_nr = article_nr
            df_data += [[None, text_nr, "de", index + 1, "\\", text_line, program] for index, text_line in enumerate(long_text)]
            # change the long_textnr to link to newly created text entries
            self.ocd["ocd_article"].loc[lambda x: x["article_nr"] == article_nr, "long_textnr"] = article_nr

        long_text_df = pd.DataFrame(
            data=df_data,
            columns=["index", "textnr", "language", "line_nr", "line_fmt", "text", "sql_db_program"]
        )

        self.ocd["ocd_artlongtext"] = pd.concat([self.ocd["ocd_artlongtext"], long_text_df]).reset_index(drop=True)

        print("artlong DF::::")
        print(self.ocd["ocd_artlongtext"].to_string())

    def update_article_nr(self):
        for article_item in self.article_items:
            article_nr = article_item["articleNr"]
            replacement = article_item["articleNrAlias"]

            self.ocd["ocd_article"].loc[lambda x: x["article_nr"] == article_nr, "article_nr"] = replacement
            self.ocd["ocd_artbase"].loc[lambda x: x["article_nr"] == article_nr, "article_nr"] = replacement
            self.ocd["ocd_propertyclass"].loc[lambda x: x["article_nr"] == article_nr, "article_nr"] = replacement
            self.ocd["ocd_price"].loc[lambda x: x["article_nr"] == article_nr, "article_nr"] = replacement
            self.ocd["ocd_articletaxes"].loc[lambda x: x["article_nr"] == article_nr, "article_nr"] = replacement
            self.ocd["ocd_packaging"].loc[lambda x: x["article_nr"] == article_nr, "article_nr"] = replacement

            self.oam["oam_article2ofml"].loc[lambda x: x["article"] == article_nr, "article"] = replacement
            self.oam["oam_article2odbparams"].loc[lambda x: x["article"] == article_nr, "article"] = replacement
            self.oam["oam_property2mat"].loc[lambda x: x["article"] == article_nr, "article"] = replacement

            self.oas["article"].loc[lambda x: x["p1"] == article_nr, "p1"] = replacement
            self.oas["structure"].loc[lambda x: x["p1"] == article_nr, "p1"] = replacement
            self.oas["text"].loc[lambda x: x["p1"] == article_nr, "p1"] = replacement
            self.oas["resource"].loc[lambda x: x["p1"] == article_nr, "p1"] = replacement

            self.go["go_articles"].loc[lambda x: x["article_nr"] == article_nr, "article_nr"] = replacement

    def load_oam_tables(self):
        con: Connection = db.session.connection()
        self.oam["oam_article2ofml"] = pd.read_sql(
            OamArticle2ofml.query.filter(
                OamArticle2ofml.article.in_(self.articlenumbers),
                OamArticle2ofml.sql_db_program.in_(self.programs)
            ).statement,
            con)

        # apply any article rows on missing oam entries
        missing_oam = set(self.articlenumbers) - set(self.oam["oam_article2ofml"]["article"].tolist())
        any_articles_df = pd.DataFrame(columns="article ofml_type odb_name params".split(),
                                       data=[f"{_};::ofml::xoi::xOiAnyArticle;;".split(";") for _ in missing_oam])
        self.oam["oam_article2ofml"] = pd.concat([
            self.oam["oam_article2ofml"],
            any_articles_df
        ])

        self.oam["oam_article2odbparams"] = pd.read_sql(
            OamArticle2odbparams.query.filter(
                OamArticle2odbparams.article.in_(self.articlenumbers),
                OamArticle2odbparams.sql_db_program.in_(self.programs)
            ).statement,
            con)
        self.oam["oam_property2mat"] = pd.read_sql(
            OamProperty2mat.query.filter(
                OamProperty2mat.article.in_(self.articlenumbers),
                OamProperty2mat.sql_db_program.in_(self.programs)
            ).statement,
            con)

    def update_go_tables(self):
        self.go["go_articles"]["program"] = self.program_name

    def load_go_tables(self):
        con: Connection = db.session.connection()
        self.go["go_articles"] = pd.read_sql(
            GoArticles.query.filter(
                GoArticles.article_nr.in_(self.articlenumbers),
                GoArticles.sql_db_program.in_(self.programs)
            ).statement,
            con)

        self.go["go_properties"] = pd.read_sql(
            GoProperties.query.filter(
                GoProperties.key.in_(self.go["go_articles"]["prm_key"].tolist()),
                GoProperties.sql_db_program.in_(self.programs)
            ).statement,
            con)

        self.go["go_types"] = pd.read_sql(
            GoTypes.query.filter(
                GoTypes.id.in_(self.go["go_articles"]["id"].tolist()),
                GoTypes.sql_db_program.in_(self.programs)
            ).statement,
            con)

        self.go["go_types"] = self.go["go_types"].loc[lambda x: (x["mode"] & 8) == 0]

    def make_oas_tables(self):
        article_rows = [
            "@FOLDER;default;0;;S;15;".split(";")
        ]

        structure_rows = [
            "@FOLDER;default;1;F;".split(";")
        ]

        text_rows = [
            f"@FOLDER;default;de;{self.program_name}".split(";")
        ]

        resource_rows = [
            "@FOLDER;default;;IT;".split(";")
        ]

        for article_item in self.article_items:
            article_nr = article_item["articleNr"]
            shorttext = article_item["shorttext"]

            article_rows.append(f"{article_nr};default;0;;S;15;::kn::{self.program_name}".split(";"))
            structure_rows.append(f"{article_nr};default;2;A;".split(";"))
            text_rows.append(f"{article_nr};default;de;{shorttext}".split(";"))
            resource_rows.append(f"{article_nr};default;;IT;".split(";"))

        self.oas["article"] = pd.DataFrame(columns="p1 p2 p3 p4 p5 p6 p7".split(), data=article_rows)
        self.oas["structure"] = pd.DataFrame(columns="p1 p2 p3 p4 p5".split(), data=structure_rows)
        self.oas["text"] = pd.DataFrame(columns="p1 p2 p3 p4".split(), data=text_rows)
        self.oas["resource"] = pd.DataFrame(columns="p1 p2 p3 p4 p5".split(), data=resource_rows)
