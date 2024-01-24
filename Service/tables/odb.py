from Service.tables import *


class Attpt(Base):
    __tablename__ = 'attpt'

    db_key = Column(Integer, primary_key=True)
    # index = Column(BigInteger)
    odb_name = Column(Text)
    name = Column(Text)
    select = Column(Text)
    text_idx = Column(Integer)
    x_pos = Column(Text)
    y_pos = Column(Text)
    z_pos = Column(Text)
    direction = Column(Text)
    rotation = Column(Text)
    mode = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class Funcs(Base):
    __tablename__ = 'funcs'

    db_key = Column(Integer, primary_key=True)
    # index = Column(BigInteger)
    name = Column(Text)
    body = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class Layer(Base):
    __tablename__ = 'layer'

    db_key = Column(Integer, primary_key=True)
    # index = Column(BigInteger)
    layer_name = Column(Text)
    attributes = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class Odb2d(Base):
    __tablename__ = 'odb2d'

    db_key = Column(Integer, primary_key=True)
    # index = Column(BigInteger)
    odb_name = Column(Text)
    level = Column(Integer)
    visible = Column(Text)
    x_offs = Column(Text)
    y_offs = Column(Text)
    rot = Column(Text)
    x_scale = Column(Text)
    y_scale = Column(Text)
    ctor = Column(Text)
    attrib = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class Odb3d(Base):
    __tablename__ = 'odb3d'

    db_key = Column(Integer, primary_key=True)
    # index = Column(BigInteger)
    odb_name = Column(Text)
    obj_name = Column(Text)
    visible = Column(Text)
    x_offs = Column(Text)
    y_offs = Column(Text)
    z_offs = Column(Text)
    x_rot = Column(Text)
    y_rot = Column(Text)
    z_rot = Column(Text)
    ctor = Column(Text)
    mat = Column(Text)
    attrib = Column(Text)
    link = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class Oppattpt(Base):
    __tablename__ = 'oppattpt'

    db_key = Column(Integer, primary_key=True)
    # index = Column(BigInteger)
    odb_name = Column(Text)
    select = Column(Text)
    opposite = Column(Text)
    direction = Column(Text)
    att_points = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class Stdattpt(Base):
    __tablename__ = 'stdattpt'

    db_key = Column(Integer, primary_key=True)
    # index = Column(BigInteger)
    odb_name = Column(Text)
    has_stdattpts = Column(SmallInteger)
    prep_stdattpts = Column(SmallInteger)
    stdattpts = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)
