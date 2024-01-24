from Service.tables import *


class OcdArtbase(Base):
    __tablename__ = 'ocd_artbase'
    __table_args__ = (
        Index('idx_article_nr', 'article_nr'),
        Index('ix_ocd_artbase_csv_index', 'index')
    )

    db_key: int = Column(Integer, primary_key=True)
    index: int = Column(BigInteger)
    article_nr: str = Column(Text)
    prop_class: str = Column(Text)
    property: str = Column(Text)
    prop_value: str = Column(Text)
    sql_db_program: str = Column(Text)
    sql_db_timestamp_modified: float = Column(Float(asdecimal=True))
    sql_db_timestamp_read: str = Column(Text)


class OcdArticle(Base):
    __tablename__ = 'ocd_article'
    __table_args__ = (
        db.Index('idx_article_nr', 'article_nr'),
        db.Index('ix_ocd_article_csv_index', 'index')
    )

    db_key: int = db.Column(Integer, primary_key=True)
    index: int = db.Column(BigInteger)
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


class OcdArticletaxes(Base):
    __tablename__ = 'ocd_articletaxes'
    __table_args__ = (
        Index('idx_article_nr', 'article_nr'),
        Index('ix_ocd_articletaxes_csv_index', 'index')
    )

    db_key: int = Column(Integer, primary_key=True)
    index: int = Column(BigInteger)
    article_nr: str = Column(Text)
    tax_id: str = Column(Text)
    date_from: str = Column(Text)
    date_to: str = Column(Text)
    sql_db_program: str = Column(Text)
    sql_db_timestamp_modified: int = Column(Float(asdecimal=True))
    sql_db_timestamp_read: str = Column(Text)


class OcdArtlongtext(Base):
    __tablename__ = 'ocd_artlongtext'
    __table_args__ = (
        Index('idx_textnr', 'textnr'),
        Index('ix_ocd_artlongtext_csv_index', 'index')
    )

    db_key: int = Column(Integer, primary_key=True)
    index: int = Column(BigInteger)
    textnr: str = Column(Text)
    language: str = Column(Text)
    line_nr: SmallInteger = Column(SmallInteger)
    line_fmt = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdArtshorttext(Base):
    __tablename__ = 'ocd_artshorttext'
    __table_args__ = (
        Index('idx_textnr', 'textnr'),
        Index('ix_ocd_artshorttext_csv_index', 'index')
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    textnr = Column(Text)
    language = Column(Text)
    line_nr = Column(SmallInteger)
    line_fmt = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdCodescheme(Base):
    __tablename__ = 'ocd_codescheme'
    __table_args__ = (
        Index('ix_ocd_codescheme_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    scheme_id = Column(Text)
    scheme = Column(Text)
    varcode_sep = Column(Text)
    value_sep = Column(Text)
    visibility = Column(Text)
    invisible_char = Column(Text)
    unselect_char = Column(Text)
    trim = Column(SmallInteger)
    mo_sep = Column(Text)
    mo_bracket = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdIdentificationCsv(Base):
    __tablename__ = 'ocd_identification_csv'
    __table_args__ = (
        Index('ix_ocd_identification_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    article_nr = Column(Text)
    ident_type = Column(Text)
    variant_code = Column(Text)
    ident_nr = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdPackaging(Base):
    __tablename__ = 'ocd_packaging'
    __table_args__ = (
        Index('idx_article_nr', 'article_nr'),
        Index('ix_ocd_packaging_csv_index', 'index')
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    article_nr = Column(Text)
    var_cond = Column(Text)
    width = Column(Text)
    height = Column(Text)
    depth = Column(Text)
    measure_unit = Column(Text)
    volume = Column(Text)
    volume_unit = Column(Text)
    tara_weight = Column(Text)
    net_weight = Column(Text)
    weight_unit = Column(Text)
    items_per_unit = Column(Text)
    pack_units = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdPrice(Base):
    __tablename__ = 'ocd_price'
    __table_args__ = (
        Index('idx_article_nr', 'article_nr'),
        Index('ix_ocd_price_csv_index', 'index')
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
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


class OcdPricetext(Base):
    __tablename__ = 'ocd_pricetext'
    __table_args__ = (
        Index('idx_textnr', 'textnr'),
        Index('ix_ocd_pricetext_csv_index', 'index')
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    textnr = Column(Text)
    language = Column(Text)
    line_nr = Column(SmallInteger)
    line_fmt = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdPropclasstext(Base):
    __tablename__ = 'ocd_propclasstext'
    __table_args__ = (
        Index('idx_textnr', 'textnr'),
        Index('ix_ocd_propclasstext_csv_index', 'index')
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    textnr = Column(Text)
    language = Column(Text)
    line_nr = Column(SmallInteger)
    line_fmt = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdProperty(Base):
    __tablename__ = 'ocd_property'
    __table_args__ = (
        Index('idx_prop_class', 'prop_class'),
        Index('ix_ocd_property_csv_index', 'index')
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
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


class OcdPropertyclass(Base):
    __tablename__ = 'ocd_propertyclass'
    __table_args__ = (
        Index('idx_article_nr', 'article_nr'),
        Index('ix_ocd_propertyclass_csv_index', 'index')
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    article_nr = Column(Text)
    pos_class = Column(Integer)
    prop_class = Column(Text)
    textnr = Column(Text)
    rel_obj = Column(BigInteger)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdPropertytext(Base):
    __tablename__ = 'ocd_propertytext'
    __table_args__ = (
        Index('idx_textnr', 'textnr'),
        Index('ix_ocd_propertytext_csv_index', 'index')
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    textnr = Column(Text)
    language = Column(Text)
    line_nr = Column(SmallInteger)
    line_fmt = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdPropertyvalue(Base):
    __tablename__ = 'ocd_propertyvalue'
    __table_args__ = (
        Index('idx_prop_class_property', 'prop_class', 'property'),
        Index('ix_ocd_propertyvalue_csv_index', 'index')
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
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


class OcdProphinttext(Base):
    __tablename__ = 'ocd_prophinttext'
    __table_args__ = (
        Index('idx_textnr', 'textnr'),
        Index('ix_ocd_prophinttext_csv_index', 'index')
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    textnr = Column(Text)
    language = Column(Text)
    line_nr = Column(SmallInteger)
    line_fmt = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdPropvaluetext(Base):
    __tablename__ = 'ocd_propvaluetext'
    __table_args__ = (
        Index('ix_ocd_propvaluetext_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    textnr = Column(Text)
    language = Column(Text)
    line_nr = Column(SmallInteger)
    line_fmt = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdRelation(Base):
    __tablename__ = 'ocd_relation'
    __table_args__ = (
        Index('idx_rel_name', 'rel_name'),
        Index('ix_ocd_relation_csv_index', 'index')
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    rel_name = Column(Text)
    rel_blocknr = Column(Integer)
    rel_block = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdRelationobj(Base):
    __tablename__ = 'ocd_relationobj'
    __table_args__ = (
        Index('idx_rel_obj', 'rel_obj'),
        Index('ix_ocd_relationobj_csv_index', 'index')
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    rel_obj = Column(BigInteger)
    position = Column(Integer)
    rel_name = Column(Text)
    rel_type = Column(Text)
    rel_domain = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdRounding(Base):
    __tablename__ = 'ocd_rounding'
    __table_args__ = (
        Index('idx_id', 'id'),
        Index('ix_ocd_rounding_csv_index', 'index')
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    nr = Column(Integer)
    min = Column(Text)
    max = Column(Text)
    type = Column(Text)
    precision = Column(Float(asdecimal=True))
    add_before = Column(Float(asdecimal=True))
    add_after = Column(Float(asdecimal=True))
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdSetCsv(Base):
    __tablename__ = 'ocd_set_csv'
    __table_args__ = (
        Index('ix_ocd_set_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    set_nr = Column(Text)
    pos_comp = Column(BigInteger)
    article_nr = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdTaxscheme(Base):
    __tablename__ = 'ocd_taxscheme'
    __table_args__ = (
        Index('ix_ocd_taxscheme_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    tax_id = Column(Text)
    country = Column(Text)
    region = Column(Text)
    number = Column(Integer)
    tax_type = Column(Text)
    tax_category = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdUsermessageCsv(Base):
    __tablename__ = 'ocd_usermessage_csv'
    __table_args__ = (
        Index('ix_ocd_usermessage_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    textnr = Column(Text)
    language = Column(Text)
    line_nr = Column(SmallInteger)
    line_fmt = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OcdVersion(Base):
    __tablename__ = 'ocd_version'
    __table_args__ = (
        Index('ix_ocd_version_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    format_version = Column(Text)
    rel_coding = Column(Text)
    data_version = Column(Text)
    date_from = Column(Text)
    date_to = Column(Text)
    region = Column(Text)
    varcond_var = Column(Text)
    placeholder_on = Column(SmallInteger)
    tables = Column(Text)
    comment = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)



class OptpropertyDat(Base):
    __tablename__ = 'optproperty_dat'
    __table_args__ = (
        Index('ix_optproperty_dat_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    prop_class = Column(Text)
    property = Column(Text)
    prop_textnr = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OptpropvalueTxt(Base):
    __tablename__ = 'optpropvalue_txt'
    __table_args__ = (
        Index('ix_optpropvalue_txt_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    textnr = Column(Text)
    language = Column(Text)
    line_nr = Column(SmallInteger)
    line_fmt = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)
