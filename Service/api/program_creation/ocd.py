import pandas as pd
from loguru import logger

from Service.api import table_descriptions
from Service.api.program_creation.create_interface import CreateInterface
from Service.api.program_creation.util import export_ofml_part, unify_column_linkages, remove_columns
from Service.tables.oam import OamArticle2odbparams, OamProperty2mat, OamArticle2ofml
from Service.api.db import yield_all_tables


class OcdCreator(CreateInterface):

    def __init__(self, articlenumbers, programs, connection, program_id, program_path, program_name, property_items, article_items): # con: Connection = db.session.connection()
        self.articlenumbers = articlenumbers
        self.programs = programs
        self.tables = {}
        self.connection = connection
        self.program_id = program_id
        self.program_path = program_path
        self.program_name = program_name
        self.property_items = property_items
        self.article_items = article_items
        self.path = self.program_path / "DE" / "2" / "db"

    def load(self):
        logger.debug("load_ocd_tables ::BEGIN")
        for _ in yield_all_tables(self.articlenumbers, self.programs):
            table_name = _["table"]
            # print("table_name", table_name)
            table_content = _["content"]
            self.tables[table_name] = pd.DataFrame(table_content)

        # update ocd_version
        table_names = [_.replace("ocd_", "") for _ in list(self.tables.keys())]
        self.tables["ocd_version"].loc[
            0,
            "tables"] = ",".join(table_names)
        logger.debug("load_ocd_tables ::DONE")

    def _update_shorttext(self):
        # TODO: if no shorttext exists yet we dont create it
        """
        iterate over all article_items
        - set the shorttext of the given item in the
          ocd_artshorttext Dataframe table
        """
        for article_item in self.article_items:
            article_nr = article_item["articleNr"]
            shorttext_ids = pd.merge(
                self.tables["ocd_article"].loc[lambda x: x["article_nr"] == article_nr],
                self.tables["ocd_artshorttext"].loc[lambda x: x["language"] == "de"],
                left_on="short_textnr",
                right_on="textnr"
            )["short_textnr"]

            self.tables["ocd_artshorttext"].loc[
                lambda x: x["textnr"].isin(shorttext_ids) & (x["language"] == "de"), "text"
            ] = article_item["shorttext"]

    def _update_longtext(self):
        # TODO: if no longtext exists yet we dont create it
        df_data = []
        for article_item in self.article_items:
            article_nr = article_item["articleNr"]
            long_text = article_item["longText"]
            program = article_item["program"]
            if long_text is None:
                continue

            longtext_ids = pd.merge(
                self.tables["ocd_article"].loc[lambda x: x["article_nr"] == article_nr],
                self.tables["ocd_artlongtext"].loc[lambda x: x["language"] == "de"],
                left_on="long_textnr",
                right_on="textnr"
            )["long_textnr"]

            to_removed_df = self.tables["ocd_artlongtext"].loc[lambda x: x["textnr"].isin(longtext_ids)]
            self.tables["ocd_artlongtext"] = self.tables["ocd_artlongtext"].drop(to_removed_df.index)

            text_nr = article_nr
            df_data += [[None, text_nr, "de", index + 1, "\\", text_line, program] for index, text_line in enumerate(long_text)]
            # change the long_textnr to link to newly created text entries
            self.tables["ocd_article"].loc[lambda x: x["article_nr"] == article_nr, "long_textnr"] = article_nr

        long_text_df = pd.DataFrame(
            data=df_data,
            columns=["index", "textnr", "language", "line_nr", "line_fmt", "text", "sql_db_program"]
        )

        self.tables["ocd_artlongtext"] = pd.concat([self.tables["ocd_artlongtext"], long_text_df]).reset_index(drop=True)

    def _update_prices(self):
        # self.ocd["ocd_price"]
        for article_item in self.article_items:

            price = article_item["price"]
            if price is None:
                continue
            # print("update price", price, type(price))
            # print(article_item)
            article_nr = article_item["articleNr"]
            # print("update_prices", price, article_nr)
            self.tables["ocd_price"].loc[
                lambda x: (x["article_nr"] == article_nr) & (x["price_type"] == "S") & (x["price_level"] == "B"),
                "price"] = price  # should be float

    def update(self):
        self._remove_farb_tabellen_relations()
        self._update_article()

        self._update_shorttext()
        self._update_artbase()
        self._update_properties()
        self._update_prices()
        self._update_longtext()
        self._unify_links()

    def _unify_links(self):
        ocd_links = {
            "ocd_artbase": ["prop_class"],
            "ocd_article": ["short_textnr", "long_textnr", "rel_obj", "scheme_id"],
            "ocd_articletaxes": ["tax_id"],
            "ocd_artlongtext": ["textnr"],
            "ocd_artshorttext": ["textnr"],
            "ocd_codescheme": ["scheme_id"],
            "ocd_price": ["rounding_id"],
            "ocd_pricetext": ["textnr"],
            "ocd_propclasstext": ["textnr"],
            "ocd_property": ["prop_textnr", "hint_text_id", "prop_class", "rel_obj"],
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

        unify_column_linkages(ocd_links, self.tables)

    def _update_artbase(self):
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
                to_delete = self.tables["ocd_artbase"].loc[lambda x: x["article_nr"] == article_nr].index
                self.tables["ocd_artbase"].drop(to_delete, inplace=True)
                assert self.tables["ocd_artbase"].loc[lambda x: x["article_nr"] == article_nr].empty
                for item in artbase:
                    # print(item)
                    # add row
                    self.tables["ocd_artbase"].loc[-1] = {
                        "article_nr": article_nr,
                        "prop_class": item["pClass"],
                        "property": item["property"],
                        "prop_value": item["value"],
                        "sql_db_program": program,
                    }

                    self.tables["ocd_artbase"].index += 1
                    self.tables["ocd_artbase"] = self.tables["ocd_artbase"].sort_index()

    def _update_article(self):
        self.tables["ocd_article"]["series"] = self.program_id

    def _update_properties(self):
        logger.debug(f"update_properties :: {len(self.property_items)}")
        for program in self.property_items:
            # print("program:", program)
            for p_class in self.property_items[program]:
                # print(" pClass", p_class)
                for prop_item in self.property_items[program][p_class]:
                    # print("  ", prop_item)
                    should_deactivate = not bool(prop_item["active"])
                    property_ = prop_item["property"]
                    if should_deactivate:
                        # print("Deactivate Property!", property_)

                        self.tables["ocd_property"].loc[
                            lambda x: (x["prop_class"] == p_class) &
                                      (x["property"] == property_) &
                                      (x["sql_db_program"] == program),
                            "scope"
                        ] = "RG"

                    # delete values
                    value_items = prop_item["values"]
                    for value_item in value_items:
                        # print(value_item)
                        should_delete = not bool(value_item["active"])
                        if should_delete:
                            value = value_item["value"]
                            to_delete = self.tables["ocd_propertyvalue"].loc[
                                lambda x: (x["prop_class"] == p_class) &
                                          (x["property"] == property_) &
                                          (x["value_from"] == value) &
                                          (x["sql_db_program"] == program)
                            ].index
                            self.tables["ocd_propertyvalue"].drop(to_delete, inplace=True)

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
        remove_columns(self.tables)
        export_ofml_part(program_name=self.program_name,
                         export_path=self.path,
                         tables=self.tables,
                         inp_descr_content=table_descriptions.ocd.INP_DESCR,
                         inp_descr_filename="pdata.inp_descr")

