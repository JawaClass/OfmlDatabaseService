from pydantic import BaseModel


class Text(BaseModel):
    textnr: str
    language: str
    line_nr: int
    line_fmt: str
    text: str
    db_key: int


class Article(BaseModel):
    article_nr: str
    art_type: str
    manufacturer: str
    series: str
    short_textnr: str
    long_textnr: str
    short_text: Text
    sql_db_program: str
    web_program_name: str
    web_filter: int
    db_key: int


class Artbase(BaseModel):
    prop_class: str
    property: str
    prop_value: str
    sql_db_program: str
    web_program_name: str
    web_filter: int
    db_key: int


class Property(BaseModel):
    prop_class: str
    property: str
    pos_prop: str
    prop_textnr: str
    rel_obj: int
    prop_type: str
    need_input: int
    add_values: int
    restrictable: int
    scope: str
    sql_db_program: str
    web_program_name: str
    web_filter: int
    db_key: int

