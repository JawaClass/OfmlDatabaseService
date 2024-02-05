from datetime import datetime

from Service.tables import *


class WebProgram(Base):

    __tablename__ = 'web_program'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    creation_date = db.Column(db.DateTime, default=datetime.now)
    edit_date = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    is_public = db.Column(db.Boolean(), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('web_user.id'), nullable=False)
    article_input = db.Column(db.Text, nullable=False)


class WebOcdArtbase(Base):
    __tablename__ = 'web_ocd_artbase'
    __table_args__ = (
        Index('idx_article_nr', 'article_nr'),
    )

    db_key: int = Column(Integer, primary_key=True)
    article_nr: str = Column(Text)
    prop_class: str = Column(Text)
    property: str = Column(Text)
    prop_value: str = Column(Text)
    sql_db_program: str = Column(Text)
    sql_db_timestamp_modified: float = Column(Float(asdecimal=True))
    sql_db_timestamp_read: str = Column(Text)

    web_program_name: str = db.Column(Text)
    web_filter: int = db.Column(SmallInteger)


class WebOcdArticle(Base):
    __tablename__ = 'web_ocd_article'

    db_key: int = db.Column(Integer, primary_key=True)
    article_nr = db.Column(Text)
    art_type: str = db.Column(Text)
    manufacturer: str = db.Column(Text)
    series: str = db.Column(Text)
    short_textnr: str = db.Column(Text)
    long_textnr: str = db.Column(Text)
    rel_obj: int = db.Column(BigInteger)
    fast_supply: int = db.Column(Integer)
    discountable: int = db.Column(SmallInteger)
    order_unit: int = db.Column(Text)
    scheme_id: str = db.Column(Text)
    sql_db_program: str = db.Column(Text)
    sql_db_timestamp_modified: float = db.Column(Float(asdecimal=True))
    sql_db_timestamp_read: str = db.Column(Text)

    web_program_name: str = db.Column(Text)
    web_filter: int = db.Column(SmallInteger)


class WebOcdArtlongtext(Base):
    __tablename__ = 'web_ocd_artlongtext'
    __table_args__ = (
        Index('idx_textnr', 'textnr'),
    )

    db_key: int = Column(Integer, primary_key=True)
    textnr: str = Column(Text)
    language: str = Column(Text)
    line_nr: SmallInteger = Column(SmallInteger)
    line_fmt = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)

    web_program_name: str = db.Column(Text)
    web_filter: int = db.Column(SmallInteger)


class WebOcdArtshorttext(Base):
    __tablename__ = 'web_ocd_artshorttext'
    __table_args__ = (
        Index('idx_textnr', 'textnr'),
    )

    db_key = Column(Integer, primary_key=True)
    textnr = Column(Text)
    language = Column(Text)
    line_nr = Column(SmallInteger)
    line_fmt = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)

    web_program_name: str = db.Column(Text)
    web_filter: int = db.Column(SmallInteger)


class WebOcdPrice(Base):
    __tablename__ = 'web_ocd_price'
    __table_args__ = (
        Index('idx_article_nr', 'article_nr'),
    )

    db_key = Column(Integer, primary_key=True)
    article_nr = Column(Text)
    var_cond = Column(Text)
    price_type = Column(Text)
    price_level = Column(Text)
    price_rule = Column(Text)
    price_textnr = Column(Text)
    price = Column(Float(asdecimal=True))
    is_fix = Column(SmallInteger)
    currency = Column(Text)
    date_from = Column(Text)
    date_to = Column(Text)
    scale_quantity = Column(Integer)
    rounding_id = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)

    web_program_name: str = db.Column(Text)
    web_filter: int = db.Column(SmallInteger)


class OcdProperty(Base):
    __tablename__ = 'web_ocd_property'
    __table_args__ = (
        Index('idx_prop_class', 'prop_class'),
    )

    db_key = Column(Integer, primary_key=True)
    prop_class = Column(Text)
    property = Column(Text)
    pos_prop = Column(Integer)
    prop_textnr = Column(Text)
    rel_obj = Column(BigInteger)
    prop_type = Column(Text)
    digits = Column(Integer)
    dec_digits = Column(SmallInteger)
    need_input = Column(SmallInteger)
    add_values = Column(SmallInteger)
    restrictable = Column(SmallInteger)
    multi_option = Column(SmallInteger)
    scope = Column(Text)
    txt_control = Column(Text)
    hint_text_id = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)

    web_program_name: str = db.Column(Text)
    web_filter: int = db.Column(SmallInteger)


class WebOcdPropertyclass(Base):
    __tablename__ = 'web_ocd_propertyclass'
    __table_args__ = (
        Index('idx_article_nr', 'article_nr'),
    )

    db_key = Column(Integer, primary_key=True)
    article_nr = Column(Text)
    pos_class = Column(Integer)
    prop_class = Column(Text)
    textnr = Column(Text)
    rel_obj = Column(BigInteger)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)

    web_program_name: str = db.Column(Text)
    web_filter: int = db.Column(SmallInteger)


class WebOcdPropertytext(Base):
    __tablename__ = 'web_ocd_propertytext'
    __table_args__ = (
        Index('idx_textnr', 'textnr'),
    )

    db_key = Column(Integer, primary_key=True)
    textnr = Column(Text)
    language = Column(Text)
    line_nr = Column(SmallInteger)
    line_fmt = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)

    web_program_name: str = db.Column(Text)
    web_filter: int = db.Column(SmallInteger)


class WebOcdPropertyvalue(Base):
    __tablename__ = 'web_ocd_propertyvalue'
    __table_args__ = (
        Index('idx_prop_class_property', 'prop_class', 'property'),
    )

    db_key = Column(Integer, primary_key=True)
    prop_class = Column(Text)
    property = Column(Text)
    pos_pval = Column(Integer)
    pval_textnr = Column(Text)
    rel_obj = Column(BigInteger)
    is_default = Column(SmallInteger)
    suppress_txt = Column(SmallInteger)
    op_from = Column(Text)
    value_from = Column(Text)
    op_to = Column(Text)
    value_to = Column(Text)
    raster = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)

    web_program_name: str = db.Column(Text)
    web_filter: int = db.Column(SmallInteger)


class WebOcdPropvaluetext(Base):
    __tablename__ = 'web_ocd_propvaluetext'

    db_key = Column(Integer, primary_key=True)
    textnr = Column(Text)
    language = Column(Text)
    line_nr = Column(SmallInteger)
    line_fmt = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)

    web_program_name: str = db.Column(Text)
    web_filter: int = db.Column(SmallInteger)


class WebOcdPropClasstext(Base):
    __tablename__ = 'web_ocd_propclasstext'

    db_key = Column(Integer, primary_key=True)
    textnr = Column(Text)
    language = Column(Text)
    line_nr = Column(SmallInteger)
    line_fmt = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)

    web_program_name: str = db.Column(Text)
    web_filter: int = db.Column(SmallInteger)
