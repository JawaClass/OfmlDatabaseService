from Service.tables import *


class OapAction(Base):
    __tablename__ = 'oap_action'
    __table_args__ = (
        Index('ix_oap_action_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    action = Column(Text)
    condition = Column(Text)
    type = Column(Text)
    parameter = Column(Text)
    objects = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapActionchoice(Base):
    __tablename__ = 'oap_actionchoice'
    __table_args__ = (
        Index('ix_oap_actionchoice_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    title = Column(Text)
    view_type = Column(Text)
    argument = Column(Text)
    list_id = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapActionlist(Base):
    __tablename__ = 'oap_actionlist'
    __table_args__ = (
        Index('ix_oap_actionlist_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    position = Column(Integer)
    condition = Column(Text)
    actions = Column(Text)
    text_id = Column(Text)
    image_id = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapArticle2type(Base):
    __tablename__ = 'oap_article2type'
    __table_args__ = (
        Index('ix_oap_article2type_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    manufacturer_id = Column(Text)
    series_id = Column(Text)
    article_id = Column(Text)
    var_type = Column(Text)
    variant = Column(Text)
    type_id = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapAttacharea(Base):
    __tablename__ = 'oap_attacharea'
    __table_args__ = (
        Index('ix_oap_attacharea_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    type_id = Column(Text)
    area_id = Column(Text)
    geo_type = Column(Text)
    geometry = Column(Text)
    cursor_pos = Column(Text)
    linked_areas = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapAttareamatch(Base):
    __tablename__ = 'oap_attareamatch'
    __table_args__ = (
        Index('ix_oap_attareamatch_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    active_id = Column(Text)
    passive_id = Column(Text)
    rot_axis = Column(Text)
    rotation = Column(Text)
    free_width_plus = Column(Text)
    free_width_minus = Column(Text)
    free_height_plus = Column(Text)
    free_height_minus = Column(Text)
    free_depth_plus = Column(Text)
    free_depth_minus = Column(Text)
    reverse_order = Column(SmallInteger)
    connect_type = Column(Text)
    translation_dof = Column(Text)
    rotation_dof = Column(Text)
    attach_actions = Column(Text)
    detach_actions = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapCreateobj(Base):
    __tablename__ = 'oap_createobj'
    __table_args__ = (
        Index('ix_oap_createobj_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    parent = Column(Text)
    art_spec_mode = Column(Text)
    package = Column(Text)
    article_id = Column(Text)
    var_code = Column(Text)
    pos_rot_mode = Column(Text)
    pos_rot_arg1 = Column(Text)
    pos_rot_arg2 = Column(Text)
    pos_rot_arg3 = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapDimchange(Base):
    __tablename__ = 'oap_dimchange'
    __table_args__ = (
        Index('ix_oap_dimchange_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    dimension = Column(Text)
    condition = Column(Text)
    separate = Column(Text)
    third_dim = Column(Text)
    property = Column(Text)
    multiplier = Column(Text)
    precision = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapExtmedia(Base):
    __tablename__ = 'oap_extmedia'
    __table_args__ = (
        Index('ix_oap_extmedia_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    type = Column(Text)
    media = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapImage(Base):
    __tablename__ = 'oap_image'
    __table_args__ = (
        Index('ix_oap_image_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    language = Column(Text)
    dpr = Column(SmallInteger)
    file = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapInteractor(Base):
    __tablename__ = 'oap_interactor'
    __table_args__ = (
        Index('ix_oap_interactor_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    interactor = Column(Text)
    condition = Column(Text)
    needs_plan_mode = Column(Text)
    actions = Column(Text)
    symbol_type = Column(Text)
    symbol_size = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapMessage(Base):
    __tablename__ = 'oap_message'
    __table_args__ = (
        Index('ix_oap_message_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    arg_type = Column(Text)
    argument = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapMetatype2type(Base):
    __tablename__ = 'oap_metatype2type'
    __table_args__ = (
        Index('ix_oap_metatype2type_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    manufacturer = Column(Text)
    series = Column(Text)
    metatype_id = Column(Text)
    var_type = Column(Text)
    variant = Column(Text)
    type_id = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)
    prop_var_code = Column(String(255))


class OapMethodcall(Base):
    __tablename__ = 'oap_methodcall'
    __table_args__ = (
        Index('ix_oap_methodcall_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    type = Column(Text)
    context = Column(Text)
    method = Column(Text)
    arguments = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapNumtripel(Base):
    __tablename__ = 'oap_numtripel'
    __table_args__ = (
        Index('ix_oap_numtripel_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    x = Column(Text)
    y = Column(Text)
    z = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapObject(Base):
    __tablename__ = 'oap_object'
    __table_args__ = (
        Index('ix_oap_object_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    category = Column(Text)
    argument1 = Column(Text)
    argument2 = Column(Text)
    argument3 = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapPropchange(Base):
    __tablename__ = 'oap_propchange'
    __table_args__ = (
        Index('ix_oap_propchange_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    type = Column(Text)
    property = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapPropedit(Base):
    __tablename__ = 'oap_propedit'
    __table_args__ = (
        Index('ix_oap_propedit_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    title = Column(Text)
    state_restr = Column(Text)
    properties = Column(Text)
    classes = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)
    staterestr = Column(String(255))


class OapPropedit2(Base):
    __tablename__ = 'oap_propedit2'
    __table_args__ = (
        Index('ix_oap_propedit2_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    title = Column(Text)
    properties = Column(Text)
    classes = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapPropeditclasses(Base):
    __tablename__ = 'oap_propeditclasses'
    __table_args__ = (
        Index('ix_oap_propeditclasses_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    prop_class = Column(Text)
    condition = Column(Text)
    state_restr = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapPropeditprops(Base):
    __tablename__ = 'oap_propeditprops'
    __table_args__ = (
        Index('ix_oap_propeditprops_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    property = Column(Text)
    condition = Column(Text)
    state_restr = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapSymboldisplay(Base):
    __tablename__ = 'oap_symboldisplay'
    __table_args__ = (
        Index('ix_oap_symboldisplay_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    interactor = Column(Text)
    offset_type = Column(Text)
    symbol_offset = Column(Text)
    direction = Column(Text)
    view_angle = Column(Text)
    orientation_x = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)
    hidden_mode = Column(String(255))


class OapText(Base):
    __tablename__ = 'oap_text'
    __table_args__ = (
        Index('ix_oap_text_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    language = Column(Text)
    text = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapTransformobj(Base):
    __tablename__ = 'oap_transformobj'
    __table_args__ = (
        Index('ix_oap_transformobj_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    id = Column(Text)
    type = Column(Text)
    argument1 = Column(Text)
    argument2 = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapType(Base):
    __tablename__ = 'oap_type'
    __table_args__ = (
        Index('ix_oap_type_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    type_id = Column(Text)
    general_info = Column(Text)
    prop_change_actions = Column(Text)
    active_att_areas = Column(Text)
    passive_att_areas = Column(Text)
    interactors = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OapVersion(Base):
    __tablename__ = 'oap_version'
    __table_args__ = (
        Index('ix_oap_version_csv_index', 'index'),
    )

    db_key: int = Column(Integer, primary_key=True)
    index: int = Column(BigInteger)
    format_version: str = Column(Text)
    sql_db_program: str = Column(Text)
    sql_db_timestamp_modified: float = Column(Float(asdecimal=True))
    sql_db_timestamp_read: str = Column(Text)