from pathlib import Path

import pandas as pd
from typing_extensions import Optional

from Service.api.program_creation.create_interface import CreateInterface
from Service.api.program_creation.util import export_ofml_part, remove_columns
from Service.tables.web.ocd import WebOcdArticle, WebOcdArtshorttext


class OasCreator(CreateInterface):

    def __init__(self, *,
                 articles: list[WebOcdArticle],
                 program_name: str,
                 program_path: Path):
        self.articles = articles
        self.program_name = program_name
        self.tables = {}
        self.path = program_path / "DE" / "2" / "cat"

    def _get_text(self, article: WebOcdArticle) -> Optional[str]:
        id(self)
        row: WebOcdArtshorttext = WebOcdArtshorttext.query.filter(
            WebOcdArtshorttext.web_program_name == article.web_program_name,
            WebOcdArtshorttext.textnr == article.short_textnr,
            WebOcdArtshorttext.language == "de"
        ).first()
        if row:
            return row.text
        return None

    def load(self):
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

        for article in self.articles:
            article_nr = article.article_nr
            text_or_none = self._get_text(article)
            if not text_or_none:
                text_or_none = ""
            shorttext = f"{text_or_none} -- {article.article_nr}"

            article_rows.append(f"{article_nr};default;0;;S;15;::kn::{self.program_name}".split(";"))
            structure_rows.append(f"{article_nr};default;2;A;".split(";"))
            text_rows.append(f"{article_nr};default;de;{shorttext}".split(";"))
            resource_rows.append(f"{article_nr};default;;IT;".split(";"))

        self.tables["article"] = pd.DataFrame(columns="p1 p2 p3 p4 p5 p6 p7".split(), data=article_rows)
        self.tables["structure"] = pd.DataFrame(columns="p1 p2 p3 p4 p5".split(), data=structure_rows)

        self.tables["text"] = pd.DataFrame(columns="p1 p2 p3 p4".split(), data=text_rows)
        self.tables["resource"] = pd.DataFrame(columns="p1 p2 p3 p4 p5".split(), data=resource_rows)

    def update(self):
        ...

    def export(self):
        remove_columns(self.tables)
        export_ofml_part(program_name=self.program_name,
                         export_path=self.path,
                         tables=self.tables)
