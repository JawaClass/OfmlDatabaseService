from Service.tables import *


class GoDeSr(Base):
    __tablename__ = 'go_de_sr'

    db_key = Column(Integer, primary_key=True)
    # index = Column(BigInteger)
    key = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoActions(Base):
    __tablename__ = 'go_actions'
    __table_args__ = (
        Index('ix_go_actions_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    own_key = Column(Text)
    foreign_key = Column(Text)
    direction = Column(Text)
    condition = Column(Text)
    action = Column(Text)
    param_1 = Column(Text)
    param_2 = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoArticles(Base):
    __tablename__ = 'go_articles'
    __table_args__ = (
        Index('ix_go_articles_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    manufacturer = Column(Text)
    program = Column(Text)
    article_nr = Column(Text)
    prm_key = Column(Text)
    chprm_key = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoAttpt(Base):
    __tablename__ = 'go_attpt'
    __table_args__ = (
        Index('ix_go_attpt_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    key = Column(Text)
    direction = Column(Text)
    condition = Column(Text)
    pos_x = Column(Text)
    pos_y = Column(Text)
    pos_z = Column(Text)
    rot_y = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoAttptgeo(Base):
    __tablename__ = 'go_attptgeo'
    __table_args__ = (
        Index('ix_go_attptgeo_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    key = Column(Text)
    id = Column(Text)
    pos_x = Column(Float)
    pos_y = Column(Float)
    pos_z = Column(Float)
    rot_dir = Column(Text)
    rot = Column(Float)
    type = Column(Text)
    arg1 = Column(Text)
    arg2 = Column(Text)
    arg3 = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoAttptsorder(Base):
    __tablename__ = 'go_attptsorder'
    __table_args__ = (
        Index('ix_go_attptsorder_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    key = Column(Text)
    id = Column(Text)
    plandir = Column(Text)
    number = Column(SmallInteger)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoChildmoving(Base):
    __tablename__ = 'go_childmoving'
    __table_args__ = (
        Index('ix_go_childmoving_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    key = Column(Text)
    condition = Column(Text)
    mode = Column(Text)
    command = Column(Text)
    parameter = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoChildprops(Base):
    __tablename__ = 'go_childprops'
    __table_args__ = (
        Index('ix_go_childprops_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    key = Column(Text)
    name = Column(Text)
    value = Column(Text)
    child_key = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoChildren(Base):
    __tablename__ = 'go_children'
    __table_args__ = (
        Index('ix_go_children_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    child_key = Column(Text)
    manufacturer = Column(Text)
    program = Column(Text)
    article_nr = Column(Text)
    variant = Column(Text)
    pos_x = Column(Text)
    pos_y = Column(Text)
    pos_z = Column(Text)
    rot_x = Column(Text)
    rot_y = Column(Text)
    rot_z = Column(Text)
    condition = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoClasses(Base):
    __tablename__ = 'go_classes'
    __table_args__ = (
        Index('ix_go_classes_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    class_ = Column('class', Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoFeedback(Base):
    __tablename__ = 'go_feedback'
    __table_args__ = (
        Index('ix_go_feedback_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    ch_artnr = Column(Text)
    attpt_key = Column(Text)
    condition = Column(Text)
    mode = Column(Text)
    command = Column(Text)
    parameter = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoFreenumeric(Base):
    __tablename__ = 'go_freenumeric'
    __table_args__ = (
        Index('ix_go_freenumeric_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    name = Column(Text)
    format = Column(Text)
    minimum = Column(Text)
    maximum = Column(Text)
    raster = Column(Text)
    expr = Column(Text)
    child = Column(Text)
    mode = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoInfo(Base):
    __tablename__ = 'go_info'
    __table_args__ = (
        Index('ix_go_info_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    key = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoInhproperties(Base):
    __tablename__ = 'go_inhproperties'
    __table_args__ = (
        Index('ix_go_inhproperties_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    pid = Column(Text)
    property = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoInteractors(Base):
    __tablename__ = 'go_interactors'
    __table_args__ = (
        Index('ix_go_interactors_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    type = Column(Text)
    key = Column(Text)
    condition = Column(Text)
    pos_x = Column(Text)
    pos_y = Column(Text)
    pos_z = Column(Text)
    image = Column(Text)
    hint = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoItemplates(Base):
    __tablename__ = 'go_itemplates'
    __table_args__ = (
        Index('ix_go_itemplates_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    template = Column(Text)
    condition = Column(Text)
    parameter = Column(Text)
    pos_x = Column(Text)
    pos_y = Column(Text)
    pos_z = Column(Text)
    rot_y = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoMetainfo(Base):
    __tablename__ = 'go_metainfo'
    __table_args__ = (
        Index('ix_go_metainfo_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    mode = Column(Text)
    width = Column(Text)
    height = Column(Text)
    depth = Column(Text)
    condition = Column(Text)
    value_1 = Column(Text)
    value_2 = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoNativeproperties(Base):
    __tablename__ = 'go_nativeproperties'
    __table_args__ = (
        Index('ix_go_nativeproperties_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    pid = Column(Text)
    mode = Column(Text)
    identifier = Column(Text)
    value1 = Column(Text)
    value2 = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoNoproperties(Base):
    __tablename__ = 'go_noproperties'
    __table_args__ = (
        Index('ix_go_noproperties_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    key = Column(Text)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoPropclasses(Base):
    __tablename__ = 'go_propclasses'
    __table_args__ = (
        Index('ix_go_propclasses_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    prop_name = Column(Text)
    prop_class = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoProperties(Base):
    __tablename__ = 'go_properties'
    __table_args__ = (
        Index('ix_go_properties_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    key = Column(Text)
    name = Column(Text)
    value = Column(Text)
    variant_code = Column(Text)
    variant_value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoProporder(Base):
    __tablename__ = 'go_proporder'
    __table_args__ = (
        Index('ix_go_proporder_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    value = Column(Text)
    number = Column(Integer)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoPropvalues(Base):
    __tablename__ = 'go_propvalues'
    __table_args__ = (
        Index('ix_go_propvalues_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    name = Column(Text)
    value = Column(Text)
    condition = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoResetnativeprops(Base):
    __tablename__ = 'go_resetnativeprops'
    __table_args__ = (
        Index('ix_go_resetnativeprops_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    key = Column(Text)
    trigger = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoSetup(Base):
    __tablename__ = 'go_setup'
    __table_args__ = (
        Index('ix_go_setup_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    key = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoTexts(Base):
    __tablename__ = 'go_texts'
    __table_args__ = (
        Index('ix_go_texts_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    key = Column(Text)
    language = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GoTypes(Base):
    __tablename__ = 'go_types'
    __table_args__ = (
        Index('ix_go_types_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    name = Column(Text)
    format = Column(Text)
    default = Column(Text)
    mode = Column(Integer)
    filter = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)