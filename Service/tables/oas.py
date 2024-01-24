from Service.tables import *


class Structure(Base):
    __tablename__ = 'structure'
    __table_args__ = (
        Index('ix_structure_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    name = Column(Text)
    type = Column(Text)
    param3 = Column(Text)
    param4 = Column(Text)
    param5 = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class Article(Base):
    __tablename__ = 'article'
    __table_args__ = (
        Index('ix_article_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    name = Column(Text)
    type = Column(Text)
    param3 = Column(Text)
    param4 = Column(Text)
    param5 = Column(Text)
    param6 = Column(Text)
    program = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class Resource(Base):
    __tablename__ = 'resource'
    __table_args__ = (
        Index('ix_resource_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    name = Column(Text)
    type = Column(Text)
    param3 = Column(Text)
    param4 = Column(Text)
    resource_path = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class Text_(Base):
    __tablename__ = 'text'
    __table_args__ = (
        Index('ix_text_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    name = Column(Text)
    type = Column(Text)
    language = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)
