from Service.tables import *


class OamArticle2odbparams(Base):
    __tablename__ = 'oam_article2odbparams'
    __table_args__ = (
        Index('ix_oam_article2odbparams_csv_index',  ),
    )

    db_key = Column(Integer, primary_key=True)
    #index = Column(BigInteger)
    article = Column(Text)
    vc_type = Column(Text)
    varcode = Column(Text)
    params = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OamArticle2ofml(Base):
    __tablename__ = 'oam_article2ofml'
    __table_args__ = (
        Index('ix_oam_article2ofml_csv_index', ),
    )

    db_key = Column(Integer, primary_key=True)
    #index = Column(BigInteger)
    article = Column(Text)
    ofml_type = Column(Text)
    odb_name = Column(Text)
    params = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OamProperty2mat(Base):
    __tablename__ = 'oam_property2mat'
    __table_args__ = (
        Index('ix_oam_property2mat_csv_index',),
    )

    db_key = Column(Integer, primary_key=True)
    #index = Column(BigInteger)
    article = Column(Text)
    property = Column(Text)
    prop_value = Column(Text)
    mat_layer = Column(Text)
    material = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)