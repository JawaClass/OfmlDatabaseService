"""
 Tables auto created with
    sqlacodegen:
        sqlacodegen mysql+mysqlconnector://root:@pdf2obs01/ofml
"""
from copy import copy
from sqlalchemy import BigInteger, Column, Float, Index, Integer, SmallInteger, String, Text

from . import db

Base = db.Model


def to_json(self):
    """
    returns a ordered json/dict of class by class attribute order
    """
    json = {}
    ordered_values = self.__class__.__dict__
    attributes = self.__dict__
    for k in ordered_values:
        if k in attributes and not k.startswith("_"):
            json[k] = attributes[k]
    return json


Base.to_json = lambda x: to_json(x)


class Art2aclassMap(Base):
    __tablename__ = 'art2aclass_map'
    __table_args__ = (
        Index('ix_art2aclass_map_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    article = Column(Text)
    aclass = Column(Text)
    params = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class Art2typeMap(Base):
    __tablename__ = 'art2type_map'
    __table_args__ = (
        Index('ix_art2type_map_csv_level_0', 'level_0'),
    )

    db_key = Column(Integer, primary_key=True)
    level_0 = Column(BigInteger)
    article = Column(Text)
    index = Column(Text)
    type = Column(Text)
    params = Column(Text)
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


class FarbenAeraTbl(Base):
    __tablename__ = 'farben_aera_tbl'
    __table_args__ = (
        Index('ix_farben_aera_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenApothekerTbl(Base):
    __tablename__ = 'farben_apotheker_tbl'
    __table_args__ = (
        Index('ix_farben_apotheker_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenAsStuehleTbl(Base):
    __tablename__ = 'farben_as_stuehle_tbl'
    __table_args__ = (
        Index('ix_farben_as_stuehle_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenAstra4Tbl(Base):
    __tablename__ = 'farben_astra_4_tbl'
    __table_args__ = (
        Index('ix_farben_astra_4_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenAstraDeltaTbl(Base):
    __tablename__ = 'farben_astra_delta_tbl'
    __table_args__ = (
        Index('ix_farben_astra_delta_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenBetaTbl(Base):
    __tablename__ = 'farben_beta_tbl'
    __table_args__ = (
        Index('ix_farben_beta_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenBtTbl(Base):
    __tablename__ = 'farben_bt_tbl'
    __table_args__ = (
        Index('ix_farben_bt_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenContainerTbl(Base):
    __tablename__ = 'farben_container_tbl'
    __table_args__ = (
        Index('ix_farben_container_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenContainerXTbl(Base):
    __tablename__ = 'farben_container_x_tbl'
    __table_args__ = (
        Index('ix_farben_container_x_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenContinentalTbl(Base):
    __tablename__ = 'farben_continental_tbl'
    __table_args__ = (
        Index('ix_farben_continental_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenDaimlerDcTbl(Base):
    __tablename__ = 'farben_daimler_dc_tbl'
    __table_args__ = (
        Index('ix_farben_daimler_dc_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenDoitD4Tbl(Base):
    __tablename__ = 'farben_doit_d4_tbl'
    __table_args__ = (
        Index('ix_farben_doit_d4_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenEBodenTbl(Base):
    __tablename__ = 'farben_e_boden_tbl'
    __table_args__ = (
        Index('ix_farben_e_boden_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenEconomyTbl(Base):
    __tablename__ = 'farben_economy_tbl'
    __table_args__ = (
        Index('ix_farben_economy_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenInside25Tbl(Base):
    __tablename__ = 'farben_inside25_tbl'
    __table_args__ = (
        Index('ix_farben_inside25_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenInside50Tbl(Base):
    __tablename__ = 'farben_inside50_tbl'
    __table_args__ = (
        Index('ix_farben_inside50_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenLamigaTbl(Base):
    __tablename__ = 'farben_lamiga_tbl'
    __table_args__ = (
        Index('ix_farben_lamiga_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenMemosTbl(Base):
    __tablename__ = 'farben_memos_tbl'
    __table_args__ = (
        Index('ix_farben_memos_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenMmTbl(Base):
    __tablename__ = 'farben_mm_tbl'
    __table_args__ = (
        Index('ix_farben_mm_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenMxTbl(Base):
    __tablename__ = 'farben_mx_tbl'
    __table_args__ = (
        Index('ix_farben_mx_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenMyTbl(Base):
    __tablename__ = 'farben_my_tbl'
    __table_args__ = (
        Index('ix_farben_my_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenNoTbl(Base):
    __tablename__ = 'farben_no_tbl'
    __table_args__ = (
        Index('ix_farben_no_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenOkTbl(Base):
    __tablename__ = 'farben_ok_tbl'
    __table_args__ = (
        Index('ix_farben_ok_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenOkayTbl(Base):
    __tablename__ = 'farben_okay_tbl'
    __table_args__ = (
        Index('ix_farben_okay_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenOptimaPlusTbl(Base):
    __tablename__ = 'farben_optima_plus_tbl'
    __table_args__ = (
        Index('ix_farben_optima_plus_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenPasoTbl(Base):
    __tablename__ = 'farben_paso_tbl'
    __table_args__ = (
        Index('ix_farben_paso_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenReelingTbl(Base):
    __tablename__ = 'farben_reeling_tbl'
    __table_args__ = (
        Index('ix_farben_reeling_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenS6SchrankTbl(Base):
    __tablename__ = 'farben_s6_schrank_tbl'
    __table_args__ = (
        Index('ix_farben_s6_schrank_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenS8MobileTbl(Base):
    __tablename__ = 'farben_s8_mobile_tbl'
    __table_args__ = (
        Index('ix_farben_s8_mobile_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenS8SchrankTbl(Base):
    __tablename__ = 'farben_s8_schrank_tbl'
    __table_args__ = (
        Index('ix_farben_s8_schrank_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenS9GehrungTbl(Base):
    __tablename__ = 'farben_s9_gehrung_tbl'
    __table_args__ = (
        Index('ix_farben_s9_gehrung_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenSiemensTbl(Base):
    __tablename__ = 'farben_siemens_tbl'
    __table_args__ = (
        Index('ix_farben_siemens_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenSummaTbl(Base):
    __tablename__ = 'farben_summa_tbl'
    __table_args__ = (
        Index('ix_farben_summa_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenTabletTbl(Base):
    __tablename__ = 'farben_tablet_tbl'
    __table_args__ = (
        Index('ix_farben_tablet_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenTalosTbl(Base):
    __tablename__ = 'farben_talos_tbl'
    __table_args__ = (
        Index('ix_farben_talos_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenTensaNTbl(Base):
    __tablename__ = 'farben_tensa_n_tbl'
    __table_args__ = (
        Index('ix_farben_tensa_n_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenTensaTbl(Base):
    __tablename__ = 'farben_tensa_tbl'
    __table_args__ = (
        Index('ix_farben_tensa_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenTisch01Tbl(Base):
    __tablename__ = 'farben_tisch01_tbl'
    __table_args__ = (
        Index('ix_farben_tisch01_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenTwsTbl(Base):
    __tablename__ = 'farben_tws_tbl'
    __table_args__ = (
        Index('ix_farben_tws_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenTwsTdf(Base):
    __tablename__ = 'farben_tws_tdf'
    __table_args__ = (
        Index('ix_farben_tws_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenUnosTbl(Base):
    __tablename__ = 'farben_unos_tbl'
    __table_args__ = (
        Index('ix_farben_unos_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class FarbenUoSchrankTbl(Base):
    __tablename__ = 'farben_uo_schrank_tbl'
    __table_args__ = (
        Index('ix_farben_uo_schrank_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewInside30PlTbl(Base):
    __tablename__ = 'gew_inside30_pl_tbl'
    __table_args__ = (
        Index('ix_gew_inside30_pl_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewKabelfuehrungTbl(Base):
    __tablename__ = 'gew_kabelfuehrung_tbl'
    __table_args__ = (
        Index('ix_gew_kabelfuehrung_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewKupplungskabelTbl(Base):
    __tablename__ = 'gew_kupplungskabel_tbl'
    __table_args__ = (
        Index('ix_gew_kupplungskabel_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewTbestueProfbTbl(Base):
    __tablename__ = 'gew_tbestue_profb_tbl'
    __table_args__ = (
        Index('ix_gew_tbestue_profb_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewTbestueckungTbl(Base):
    __tablename__ = 'gew_tbestueckung_tbl'
    __table_args__ = (
        Index('ix_gew_tbestueckung_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewTzufuehrkabelTbl(Base):
    __tablename__ = 'gew_tzufuehrkabel_tbl'
    __table_args__ = (
        Index('ix_gew_tzufuehrkabel_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpPlattenTbl(Base):
    __tablename__ = 'gew_wp_platten_tbl'
    __table_args__ = (
        Index('ix_gew_wp_platten_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpSeitenTbl(Base):
    __tablename__ = 'gew_wp_seiten_tbl'
    __table_args__ = (
        Index('ix_gew_wp_seiten_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpapgraPlarahTbl(Base):
    __tablename__ = 'gew_wpapgra_plarah_tbl'
    __table_args__ = (
        Index('ix_gew_wpapgra_plarah_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpaptdbPlaraTbl(Base):
    __tablename__ = 'gew_wpaptdb_plara_tbl'
    __table_args__ = (
        Index('ix_gew_wpaptdb_plara_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpaptdbPlattformTbl(Base):
    __tablename__ = 'gew_wpaptdb_plattform_tbl'
    __table_args__ = (
        Index('ix_gew_wpaptdb_plattform_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpaptdbSeitenTbl(Base):
    __tablename__ = 'gew_wpaptdb_seiten_tbl'
    __table_args__ = (
        Index('ix_gew_wpaptdb_seiten_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpaptnAdapterTbl(Base):
    __tablename__ = 'gew_wpaptn_adapter_tbl'
    __table_args__ = (
        Index('ix_gew_wpaptn_adapter_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpaptnPlFreiTbl(Base):
    __tablename__ = 'gew_wpaptn_pl_frei_tbl'
    __table_args__ = (
        Index('ix_gew_wpaptn_pl_frei_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpaptnPlaraTbl(Base):
    __tablename__ = 'gew_wpaptn_plara_tbl'
    __table_args__ = (
        Index('ix_gew_wpaptn_plara_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpaptnPlattfoTbl(Base):
    __tablename__ = 'gew_wpaptn_plattfo_tbl'
    __table_args__ = (
        Index('ix_gew_wpaptn_plattfo_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpaptnSeitenTbl(Base):
    __tablename__ = 'gew_wpaptn_seiten_tbl'
    __table_args__ = (
        Index('ix_gew_wpaptn_seiten_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpaptraPlattfTbl(Base):
    __tablename__ = 'gew_wpaptra_plattf_tbl'
    __table_args__ = (
        Index('ix_gew_wpaptra_plattf_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpaptraSeitenTbl(Base):
    __tablename__ = 'gew_wpaptra_seiten_tbl'
    __table_args__ = (
        Index('ix_gew_wpaptra_seiten_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpbgnPlarahTbl(Base):
    __tablename__ = 'gew_wpbgn_plarah_tbl'
    __table_args__ = (
        Index('ix_gew_wpbgn_plarah_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpbtbSeitenTbl(Base):
    __tablename__ = 'gew_wpbtb_seiten_tbl'
    __table_args__ = (
        Index('ix_gew_wpbtb_seiten_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpbtnPlattforTbl(Base):
    __tablename__ = 'gew_wpbtn_plattfor_tbl'
    __table_args__ = (
        Index('ix_gew_wpbtn_plattfor_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpbtnSeitenTbl(Base):
    __tablename__ = 'gew_wpbtn_seiten_tbl'
    __table_args__ = (
        Index('ix_gew_wpbtn_seiten_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWpltravTbl(Base):
    __tablename__ = 'gew_wpltrav_tbl'
    __table_args__ = (
        Index('ix_gew_wpltrav_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWptzdbgsblTbl(Base):
    __tablename__ = 'gew_wptzdbgsbl_tbl'
    __table_args__ = (
        Index('ix_gew_wptzdbgsbl_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWptzdbsblTbl(Base):
    __tablename__ = 'gew_wptzdbsbl_tbl'
    __table_args__ = (
        Index('ix_gew_wptzdbsbl_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWptzdbswTbl(Base):
    __tablename__ = 'gew_wptzdbsw_tbl'
    __table_args__ = (
        Index('ix_gew_wptzdbsw_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class GewWptzrwbldTbl(Base):
    __tablename__ = 'gew_wptzrwbld_tbl'
    __table_args__ = (
        Index('ix_gew_wptzrwbld_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
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


class KdGruppeRabattTbl(Base):
    __tablename__ = 'kd_gruppe_rabatt_tbl'
    __table_args__ = (
        Index('ix_kd_gruppe_rabatt_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class KdgruppeTbl(Base):
    __tablename__ = 'kdgruppe_tbl'
    __table_args__ = (
        Index('ix_kdgruppe_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class KundenTbl(Base):
    __tablename__ = 'kunden_tbl'
    __table_args__ = (
        Index('ix_kunden_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class MasseAusfr01Tbl(Base):
    __tablename__ = 'masse_ausfr_01_tbl'
    __table_args__ = (
        Index('ix_masse_ausfr_01_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class MasseFrKastenKtTbl(Base):
    __tablename__ = 'masse_fr_kasten_kt_tbl'
    __table_args__ = (
        Index('ix_masse_fr_kasten_kt_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class MaterialhauptgruppTbl(Base):
    __tablename__ = 'materialhauptgrupp_tbl'
    __table_args__ = (
        Index('ix_materialhauptgrupp_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OamArticle2odbparams(Base):
    __tablename__ = 'oam_article2odbparams'
    __table_args__ = (
        Index('ix_oam_article2odbparams_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
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
        Index('ix_oam_article2ofml_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
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
        Index('ix_oam_property2mat_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    article = Column(Text)
    property = Column(Text)
    prop_value = Column(Text)
    mat_layer = Column(Text)
    material = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


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


class OpenAkustikMatnrTbl(Base):
    __tablename__ = 'open_akustik_matnr_tbl'
    __table_args__ = (
        Index('ix_open_akustik_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OpenGestellMatnrTbl(Base):
    __tablename__ = 'open_gestell_matnr_tbl'
    __table_args__ = (
        Index('ix_open_gestell_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class OpenMg1MatnrTbl(Base):
    __tablename__ = 'open_mg1_matnr_tbl'
    __table_args__ = (
        Index('ix_open_mg1_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
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


class ParametersMap(Base):
    __tablename__ = 'parameters_map'
    __table_args__ = (
        Index('ix_parameters_map_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    class_ = Column('class', Text)
    params = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class Replacement(Base):
    __tablename__ = 'replacement'
    __table_args__ = (
        Index('ix_replacement_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    article_nr = Column(Text)
    manufacturer = Column(Text)
    series = Column(Text)
    replacement = Column(Text)
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


class SonderstoffW1Tbl(Base):
    __tablename__ = 'sonderstoff_w1_tbl'
    __table_args__ = (
        Index('ix_sonderstoff_w1_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


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


class StsUmst19MatnrTbl(Base):
    __tablename__ = 'sts_umst_19_matnr_tbl'
    __table_args__ = (
        Index('ix_sts_umst_19_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class TabArtnrTbl(Base):
    __tablename__ = 'tab_artnr_tbl'
    __table_args__ = (
        Index('ix_tab_artnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class TabEinheit2Tbl(Base):
    __tablename__ = 'tab_einheit2_tbl'
    __table_args__ = (
        Index('ix_tab_einheit2_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class TabEinheitAwg14Tbl(Base):
    __tablename__ = 'tab_einheit_awg14_tbl'
    __table_args__ = (
        Index('ix_tab_einheit_awg14_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class TabEinheitChOSichT(Base):
    __tablename__ = 'tab_einheit_ch_o_sich_t'
    __table_args__ = (
        Index('ix_tab_einheit_ch_o_sich_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class TabEinheitExternTbl(Base):
    __tablename__ = 'tab_einheit_extern_tbl'
    __table_args__ = (
        Index('ix_tab_einheit_extern_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class TabModulAhm15KnTbl(Base):
    __tablename__ = 'tab_modul_ahm_15_kn_tbl'
    __table_args__ = (
        Index('ix_tab_modul_ahm_15_kn_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class TabModulAhm15Tbl(Base):
    __tablename__ = 'tab_modul_ahm_15_tbl'
    __table_args__ = (
        Index('ix_tab_modul_ahm_15_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class TabModulAhm25Tbl(Base):
    __tablename__ = 'tab_modul_ahm_25_tbl'
    __table_args__ = (
        Index('ix_tab_modul_ahm_25_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class TabModulAwg14Tbl(Base):
    __tablename__ = 'tab_modul_awg14_tbl'
    __table_args__ = (
        Index('ix_tab_modul_awg14_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class TabStdcheckExtNTbl(Base):
    __tablename__ = 'tab_stdcheck_ext_n_tbl'
    __table_args__ = (
        Index('ix_tab_stdcheck_ext_n_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class TabStdcheckExtTbl(Base):
    __tablename__ = 'tab_stdcheck_ext_tbl'
    __table_args__ = (
        Index('ix_tab_stdcheck_ext_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class TabStdcheckNTbl(Base):
    __tablename__ = 'tab_stdcheck_n_tbl'
    __table_args__ = (
        Index('ix_tab_stdcheck_n_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class TabStdcheckTbl(Base):
    __tablename__ = 'tab_stdcheck_tbl'
    __table_args__ = (
        Index('ix_tab_stdcheck_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
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


class Vb3741MatnrTbl(Base):
    __tablename__ = 'vb_3741_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_3741_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class Vb3791MatnrTbl(Base):
    __tablename__ = 'vb_3791_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_3791_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbAa5Ad5MatnrTbl(Base):
    __tablename__ = 'vb_aa5_ad5_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_aa5_ad5_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbAa5Ad5MatnrTdf(Base):
    __tablename__ = 'vb_aa5_ad5_matnr_tdf'
    __table_args__ = (
        Index('ix_vb_aa5_ad5_matnr_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbAdapterMatnrTbl(Base):
    __tablename__ = 'vb_adapter_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_adapter_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbAl41MatnrTbl(Base):
    __tablename__ = 'vb_al41_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_al41_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbAl42MatnrTbl(Base):
    __tablename__ = 'vb_al42_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_al42_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbAl43MatnrTbl(Base):
    __tablename__ = 'vb_al43_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_al43_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbAnzSt2MatnrTbl(Base):
    __tablename__ = 'vb_anz_st_2_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_anz_st_2_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbAnzSt2MatnrTdf(Base):
    __tablename__ = 'vb_anz_st_2_matnr_tdf'
    __table_args__ = (
        Index('ix_vb_anz_st_2_matnr_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbAnzSt3MatnrTbl(Base):
    __tablename__ = 'vb_anz_st_3_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_anz_st_3_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbAnzSt3MatnrTdf(Base):
    __tablename__ = 'vb_anz_st_3_matnr_tdf'
    __table_args__ = (
        Index('ix_vb_anz_st_3_matnr_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbArmlehneMatnrTbl(Base):
    __tablename__ = 'vb_armlehne_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_armlehne_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbAusfraesungLsTbl(Base):
    __tablename__ = 'vb_ausfraesung_ls_tbl'
    __table_args__ = (
        Index('ix_vb_ausfraesung_ls_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbAusfraesungLsTdf(Base):
    __tablename__ = 'vb_ausfraesung_ls_tdf'
    __table_args__ = (
        Index('ix_vb_ausfraesung_ls_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbB4BenchGm95Tbl(Base):
    __tablename__ = 'vb_b4_bench_gm95_tbl'
    __table_args__ = (
        Index('ix_vb_b4_bench_gm95_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbB4BenchKw0Tbl(Base):
    __tablename__ = 'vb_b4_bench_kw0_tbl'
    __table_args__ = (
        Index('ix_vb_b4_bench_kw0_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbB4GehrungsfussTbl(Base):
    __tablename__ = 'vb_b4_gehrungsfuss_tbl'
    __table_args__ = (
        Index('ix_vb_b4_gehrungsfuss_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbB4GehrungsfussTdf(Base):
    __tablename__ = 'vb_b4_gehrungsfuss_tdf'
    __table_args__ = (
        Index('ix_vb_b4_gehrungsfuss_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbB4d4BenchPav0Tbl(Base):
    __tablename__ = 'vb_b4d4_bench_pav0_tbl'
    __table_args__ = (
        Index('ix_vb_b4d4_bench_pav0_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbContAkfTbl(Base):
    __tablename__ = 'vb_cont_akf_tbl'
    __table_args__ = (
        Index('ix_vb_cont_akf_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbContAkfTdf(Base):
    __tablename__ = 'vb_cont_akf_tdf'
    __table_args__ = (
        Index('ix_vb_cont_akf_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbD4BenchGm98Tbl(Base):
    __tablename__ = 'vb_d4_bench_gm98_tbl'
    __table_args__ = (
        Index('ix_vb_d4_bench_gm98_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbDaempfungMatnrTbl(Base):
    __tablename__ = 'vb_daempfung_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_daempfung_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbDaempfungMatnrTdf(Base):
    __tablename__ = 'vb_daempfung_matnr_tdf'
    __table_args__ = (
        Index('ix_vb_daempfung_matnr_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbDekorein1MatnrTbl(Base):
    __tablename__ = 'vb_dekorein1_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_dekorein1_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbEVerbMatnrTbl(Base):
    __tablename__ = 'vb_e_verb_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_e_verb_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbEVerbMatnrTdf(Base):
    __tablename__ = 'vb_e_verb_matnr_tdf'
    __table_args__ = (
        Index('ix_vb_e_verb_matnr_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbElektroE35MatTbl(Base):
    __tablename__ = 'vb_elektro_e35_mat_tbl'
    __table_args__ = (
        Index('ix_vb_elektro_e35_mat_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbElektroExMatnTbl(Base):
    __tablename__ = 'vb_elektro_ex_matn_tbl'
    __table_args__ = (
        Index('ix_vb_elektro_ex_matn_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbElektroExMatnTdf(Base):
    __tablename__ = 'vb_elektro_ex_matn_tdf'
    __table_args__ = (
        Index('ix_vb_elektro_ex_matn_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbEvkMatnrTbl(Base):
    __tablename__ = 'vb_evk_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_evk_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbEvkMatnrTdf(Base):
    __tablename__ = 'vb_evk_matnr_tdf'
    __table_args__ = (
        Index('ix_vb_evk_matnr_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbFenixMatnrTbl(Base):
    __tablename__ = 'vb_fenix_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_fenix_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbFenixMatnrTdf(Base):
    __tablename__ = 'vb_fenix_matnr_tdf'
    __table_args__ = (
        Index('ix_vb_fenix_matnr_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGGewiS6600tTbl(Base):
    __tablename__ = 'vb_g_gewi_s6_600t_tbl'
    __table_args__ = (
        Index('ix_vb_g_gewi_s6_600t_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGasfed10MatnrTbl(Base):
    __tablename__ = 'vb_gasfed_10_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gasfed_10_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGasfed12MatnrTbl(Base):
    __tablename__ = 'vb_gasfed_12_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gasfed_12_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGasfed13MatnrTbl(Base):
    __tablename__ = 'vb_gasfed_13_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gasfed_13_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGasfeder0MatnrTbl(Base):
    __tablename__ = 'vb_gasfeder0_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gasfeder0_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGasfeder3MatnrTbl(Base):
    __tablename__ = 'vb_gasfeder3_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gasfeder3_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGasfeder4MatnrTbl(Base):
    __tablename__ = 'vb_gasfeder4_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gasfeder4_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGasfeder5MatnrTbl(Base):
    __tablename__ = 'vb_gasfeder5_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gasfeder5_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGasfeder6MatnrTbl(Base):
    __tablename__ = 'vb_gasfeder6_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gasfeder6_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGasfeder7MatnrTbl(Base):
    __tablename__ = 'vb_gasfeder7_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gasfeder7_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGasfeder8MatnrTbl(Base):
    __tablename__ = 'vb_gasfeder8_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gasfeder8_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGasfeder9MatnrTbl(Base):
    __tablename__ = 'vb_gasfeder9_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gasfeder9_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGasfederMatnrTbl(Base):
    __tablename__ = 'vb_gasfeder_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gasfeder_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGfg23MatnrTbl(Base):
    __tablename__ = 'vb_gfg23_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gfg23_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGfs20MatnrTbl(Base):
    __tablename__ = 'vb_gfs20_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gfs20_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGfussGf1MatnrTbl(Base):
    __tablename__ = 'vb_gfuss_gf1_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gfuss_gf1_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGfussGf2MatnrTbl(Base):
    __tablename__ = 'vb_gfuss_gf2_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gfuss_gf2_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGfussGf3MatnrTbl(Base):
    __tablename__ = 'vb_gfuss_gf3_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gfuss_gf3_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGl22MatnrTbl(Base):
    __tablename__ = 'vb_gl22_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gl22_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGl23MatnrTbl(Base):
    __tablename__ = 'vb_gl23_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gl23_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGl24MatnrTbl(Base):
    __tablename__ = 'vb_gl24_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gl24_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGr5S6MatnrTbl(Base):
    __tablename__ = 'vb_gr5_s6_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gr5_s6_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGr5S8MatnrTbl(Base):
    __tablename__ = 'vb_gr5_s8_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_gr5_s8_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGr5S8MatnrTdf(Base):
    __tablename__ = 'vb_gr5_s8_matnr_tdf'
    __table_args__ = (
        Index('ix_vb_gr5_s8_matnr_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbGv2Lifes2Tbl(Base):
    __tablename__ = 'vb_gv2_lifes2_tbl'
    __table_args__ = (
        Index('ix_vb_gv2_lifes2_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbHeTbl(Base):
    __tablename__ = 'vb_he_tbl'
    __table_args__ = (
        Index('ix_vb_he_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbKabelwkw2MatnrTbl(Base):
    __tablename__ = 'vb_kabelwkw2_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_kabelwkw2_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbKabelwkw4MatnrTbl(Base):
    __tablename__ = 'vb_kabelwkw4_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_kabelwkw4_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbKabelwkw6MatnrTbl(Base):
    __tablename__ = 'vb_kabelwkw6_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_kabelwkw6_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbKlb1MatnrTbl(Base):
    __tablename__ = 'vb_klb1_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_klb1_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbKlbMatnrTbl(Base):
    __tablename__ = 'vb_klb_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_klb_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbKleiderbuMatnrTbl(Base):
    __tablename__ = 'vb_kleiderbu_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_kleiderbu_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbKlemmadKa2MatTbl(Base):
    __tablename__ = 'vb_klemmad_ka2_mat_tbl'
    __table_args__ = (
        Index('ix_vb_klemmad_ka2_mat_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbKlemmadKa2MatTdf(Base):
    __tablename__ = 'vb_klemmad_ka2_mat_tdf'
    __table_args__ = (
        Index('ix_vb_klemmad_ka2_mat_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbKlemmadKa3MatTbl(Base):
    __tablename__ = 'vb_klemmad_ka3_mat_tbl'
    __table_args__ = (
        Index('ix_vb_klemmad_ka3_mat_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbKlemmadKa3MatTdf(Base):
    __tablename__ = 'vb_klemmad_ka3_mat_tdf'
    __table_args__ = (
        Index('ix_vb_klemmad_ka3_mat_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbKo2MatnrTbl(Base):
    __tablename__ = 'vb_ko2_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_ko2_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbKonfKw7Kw8Tbl(Base):
    __tablename__ = 'vb_konf_kw7_kw8_tbl'
    __table_args__ = (
        Index('ix_vb_konf_kw7_kw8_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbLadefeld0MatnrTbl(Base):
    __tablename__ = 'vb_ladefeld0_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_ladefeld0_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbLfDemontMatnrTbl(Base):
    __tablename__ = 'vb_lf_demont_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_lf_demont_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbLfDemontMatnrTdf(Base):
    __tablename__ = 'vb_lf_demont_matnr_tdf'
    __table_args__ = (
        Index('ix_vb_lf_demont_matnr_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbLfDemontTbTbl(Base):
    __tablename__ = 'vb_lf_demont_tb_tbl'
    __table_args__ = (
        Index('ix_vb_lf_demont_tb_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbLfDemontTbTdf(Base):
    __tablename__ = 'vb_lf_demont_tb_tdf'
    __table_args__ = (
        Index('ix_vb_lf_demont_tb_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbLfDemontTlTbl(Base):
    __tablename__ = 'vb_lf_demont_tl_tbl'
    __table_args__ = (
        Index('ix_vb_lf_demont_tl_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbLfDemontTlTdf(Base):
    __tablename__ = 'vb_lf_demont_tl_tdf'
    __table_args__ = (
        Index('ix_vb_lf_demont_tl_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbLsBench4aKw1Tbl(Base):
    __tablename__ = 'vb_ls_bench_4a_kw1_tbl'
    __table_args__ = (
        Index('ix_vb_ls_bench_4a_kw1_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbLsBench4aKw1Tdf(Base):
    __tablename__ = 'vb_ls_bench_4a_kw1_tdf'
    __table_args__ = (
        Index('ix_vb_ls_bench_4a_kw1_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbMatnrEbodenTbl(Base):
    __tablename__ = 'vb_matnr_eboden_tbl'
    __table_args__ = (
        Index('ix_vb_matnr_eboden_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbMatnrEbodenTdf(Base):
    __tablename__ = 'vb_matnr_eboden_tdf'
    __table_args__ = (
        Index('ix_vb_matnr_eboden_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbMatnrFfmTbl(Base):
    __tablename__ = 'vb_matnr_ffm_tbl'
    __table_args__ = (
        Index('ix_vb_matnr_ffm_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbMatnrHRahm2Tbl(Base):
    __tablename__ = 'vb_matnr_h_rahm_2_tbl'
    __table_args__ = (
        Index('ix_vb_matnr_h_rahm_2_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbMatnrHRahmTbl(Base):
    __tablename__ = 'vb_matnr_h_rahm_tbl'
    __table_args__ = (
        Index('ix_vb_matnr_h_rahm_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbMatnrNetzNeuTbl(Base):
    __tablename__ = 'vb_matnr_netz_neu_tbl'
    __table_args__ = (
        Index('ix_vb_matnr_netz_neu_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbMatnrPaneelvorTbl(Base):
    __tablename__ = 'vb_matnr_paneelvor_tbl'
    __table_args__ = (
        Index('ix_vb_matnr_paneelvor_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbMatnrPaneelvorTdf(Base):
    __tablename__ = 'vb_matnr_paneelvor_tdf'
    __table_args__ = (
        Index('ix_vb_matnr_paneelvor_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbMatnrPlattenstTbl(Base):
    __tablename__ = 'vb_matnr_plattenst_tbl'
    __table_args__ = (
        Index('ix_vb_matnr_plattenst_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbMatnrPlattenstTdf(Base):
    __tablename__ = 'vb_matnr_plattenst_tdf'
    __table_args__ = (
        Index('ix_vb_matnr_plattenst_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbMatnrRolgTbl(Base):
    __tablename__ = 'vb_matnr_rolg_tbl'
    __table_args__ = (
        Index('ix_vb_matnr_rolg_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbMatnrSg16RuecTbl(Base):
    __tablename__ = 'vb_matnr_sg16_ruec_tbl'
    __table_args__ = (
        Index('ix_vb_matnr_sg16_ruec_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbMatwaTbVbcontTbl(Base):
    __tablename__ = 'vb_matwa_tb_vbcont_tbl'
    __table_args__ = (
        Index('ix_vb_matwa_tb_vbcont_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbMittelwandTbl(Base):
    __tablename__ = 'vb_mittelwand_tbl'
    __table_args__ = (
        Index('ix_vb_mittelwand_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbNeKleiderbuegeTbl(Base):
    __tablename__ = 'vb_ne_kleiderbuege_tbl'
    __table_args__ = (
        Index('ix_vb_ne_kleiderbuege_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbNotKw1Tbl(Base):
    __tablename__ = 'vb_not_kw1_tbl'
    __table_args__ = (
        Index('ix_vb_not_kw1_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbObflS8ApoTbl(Base):
    __tablename__ = 'vb_obfl_s8_apo_tbl'
    __table_args__ = (
        Index('ix_vb_obfl_s8_apo_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbObflS8Tbl(Base):
    __tablename__ = 'vb_obfl_s8_tbl'
    __table_args__ = (
        Index('ix_vb_obfl_s8_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbObflTbl(Base):
    __tablename__ = 'vb_obfl_tbl'
    __table_args__ = (
        Index('ix_vb_obfl_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbObflTcontXTbl(Base):
    __tablename__ = 'vb_obfl_tcont_x_tbl'
    __table_args__ = (
        Index('ix_vb_obfl_tcont_x_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbObflTdf(Base):
    __tablename__ = 'vb_obfl_tdf'
    __table_args__ = (
        Index('ix_vb_obfl_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbObg12MatnrTbl(Base):
    __tablename__ = 'vb_obg1_2_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_obg1_2_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbOpeKabelMatnrTbl(Base):
    __tablename__ = 'vb_ope_kabel_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_ope_kabel_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbOpenAl34Tbl(Base):
    __tablename__ = 'vb_open_al34_tbl'
    __table_args__ = (
        Index('ix_vb_open_al34_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbOpenEckGeoTbl(Base):
    __tablename__ = 'vb_open_eck_geo_tbl'
    __table_args__ = (
        Index('ix_vb_open_eck_geo_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbOpenF103AlTbl(Base):
    __tablename__ = 'vb_open_f103_al_tbl'
    __table_args__ = (
        Index('ix_vb_open_f103_al_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbOpenF103AmTbl(Base):
    __tablename__ = 'vb_open_f103_am_tbl'
    __table_args__ = (
        Index('ix_vb_open_f103_am_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbOpenF103KsTbl(Base):
    __tablename__ = 'vb_open_f103_ks_tbl'
    __table_args__ = (
        Index('ix_vb_open_f103_ks_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbOpenF103SmeTbl(Base):
    __tablename__ = 'vb_open_f103_sme_tbl'
    __table_args__ = (
        Index('ix_vb_open_f103_sme_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbOpenGl1Tbl(Base):
    __tablename__ = 'vb_open_gl1_tbl'
    __table_args__ = (
        Index('ix_vb_open_gl1_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbOpenGl24Tbl(Base):
    __tablename__ = 'vb_open_gl24_tbl'
    __table_args__ = (
        Index('ix_vb_open_gl24_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbOpenHv32MatnrTbl(Base):
    __tablename__ = 'vb_open_hv32_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_open_hv32_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbOpenMittelwandTbl(Base):
    __tablename__ = 'vb_open_mittelwand_tbl'
    __table_args__ = (
        Index('ix_vb_open_mittelwand_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbOpenPosAusfraTbl(Base):
    __tablename__ = 'vb_open_pos_ausfra_tbl'
    __table_args__ = (
        Index('ix_vb_open_pos_ausfra_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbPlDMessMatnrTbl(Base):
    __tablename__ = 'vb_pl_d_mess_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_pl_d_mess_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbPlGroessMatnrTbl(Base):
    __tablename__ = 'vb_pl_groess_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_pl_groess_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbProdukttypTbl(Base):
    __tablename__ = 'vb_produkttyp_tbl'
    __table_args__ = (
        Index('ix_vb_produkttyp_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbSb1Konf2MatnrTbl(Base):
    __tablename__ = 'vb_sb1_konf2_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_sb1_konf2_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbSb1KonfMatnrTbl(Base):
    __tablename__ = 'vb_sb1_konf_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_sb1_konf_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbSf76MatnrTbl(Base):
    __tablename__ = 'vb_sf76_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_sf76_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbSf76MatnrTdf(Base):
    __tablename__ = 'vb_sf76_matnr_tdf'
    __table_args__ = (
        Index('ix_vb_sf76_matnr_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbSg25MatnrTbl(Base):
    __tablename__ = 'vb_sg_25_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_sg_25_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbSg38MatnrTbl(Base):
    __tablename__ = 'vb_sg_38_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_sg_38_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbSk1MatnrTbl(Base):
    __tablename__ = 'vb_sk1_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_sk1_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbSkt6MatnrTbl(Base):
    __tablename__ = 'vb_skt6_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_skt6_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbSplStaerMatnrTbl(Base):
    __tablename__ = 'vb_spl_staer_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_spl_staer_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbStatWanrMatnrTbl(Base):
    __tablename__ = 'vb_stat_wanr_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_stat_wanr_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbStatWanrMatnrTdf(Base):
    __tablename__ = 'vb_stat_wanr_matnr_tdf'
    __table_args__ = (
        Index('ix_vb_stat_wanr_matnr_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbStiftbEboxLsTbl(Base):
    __tablename__ = 'vb_stiftb_ebox_ls_tbl'
    __table_args__ = (
        Index('ix_vb_stiftb_ebox_ls_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbStoffgr4649MatTbl(Base):
    __tablename__ = 'vb_stoffgr4649_mat_tbl'
    __table_args__ = (
        Index('ix_vb_stoffgr4649_mat_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbStoffgr4649MatTdf(Base):
    __tablename__ = 'vb_stoffgr4649_mat_tdf'
    __table_args__ = (
        Index('ix_vb_stoffgr4649_mat_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbStoffgr3MatnrTbl(Base):
    __tablename__ = 'vb_stoffgr_3_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_stoffgr_3_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbStv2MatnrTbl(Base):
    __tablename__ = 'vb_stv2_matnr_tbl'
    __table_args__ = (
        Index('ix_vb_stv2_matnr_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbTablar7vTbl(Base):
    __tablename__ = 'vb_tablar_7v_tbl'
    __table_args__ = (
        Index('ix_vb_tablar_7v_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbTbKonfKw0Tbl(Base):
    __tablename__ = 'vb_tb_konf_kw0_tbl'
    __table_args__ = (
        Index('ix_vb_tb_konf_kw0_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbTf16IaMatnTbl(Base):
    __tablename__ = 'vb_tf16_ia_matn_tbl'
    __table_args__ = (
        Index('ix_vb_tf16_ia_matn_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbTf16IaMatnTdf(Base):
    __tablename__ = 'vb_tf16_ia_matn_tdf'
    __table_args__ = (
        Index('ix_vb_tf16_ia_matn_tdf_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    akey = Column(Integer)
    name = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class VbTlKonfKw0Tbl(Base):
    __tablename__ = 'vb_tl_konf_kw0_tbl'
    __table_args__ = (
        Index('ix_vb_tl_konf_kw0_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class WpGewFussDesignTbl(Base):
    __tablename__ = 'wp_gew_fuss_design_tbl'
    __table_args__ = (
        Index('ix_wp_gew_fuss_design_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class WpGewKabelwannenTbl(Base):
    __tablename__ = 'wp_gew_kabelwannen_tbl'
    __table_args__ = (
        Index('ix_wp_gew_kabelwannen_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class WpGewKonsoleTbl(Base):
    __tablename__ = 'wp_gew_konsole_tbl'
    __table_args__ = (
        Index('ix_wp_gew_konsole_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class WpGewKwannBen2Tbl(Base):
    __tablename__ = 'wp_gew_kwann_ben_2_tbl'
    __table_args__ = (
        Index('ix_wp_gew_kwann_ben_2_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class WpGewKwannBenchTbl(Base):
    __tablename__ = 'wp_gew_kwann_bench_tbl'
    __table_args__ = (
        Index('ix_wp_gew_kwann_bench_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class WpGewTgstCoverTbl(Base):
    __tablename__ = 'wp_gew_tgst_cover_tbl'
    __table_args__ = (
        Index('ix_wp_gew_tgst_cover_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class WpGewTseitWangeTbl(Base):
    __tablename__ = 'wp_gew_tseit_wange_tbl'
    __table_args__ = (
        Index('ix_wp_gew_tseit_wange_tbl_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    line = Column(Text)
    name = Column(Text)
    value = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


class XoiSet(Base):
    __tablename__ = 'xoi_set'
    __table_args__ = (
        Index('ix_xoi_set_csv_index', 'index'),
    )

    db_key = Column(Integer, primary_key=True)
    index = Column(BigInteger)
    set_article = Column(Text)
    part_nr = Column(Integer)
    part_article = Column(Text)
    x_pos = Column(Text)
    y_pos = Column(Text)
    z_pos = Column(Text)
    y_rot = Column(Text)
    config_state = Column(Text)
    sql_db_program = Column(Text)
    sql_db_timestamp_modified = Column(Float(asdecimal=True))
    sql_db_timestamp_read = Column(Text)


TABLE_NAME_2_CLASS = {}
__locals = copy(locals())
for k, v in __locals.items():
    if hasattr(v, "__tablename__"):
        table_name = getattr(v, "__tablename__")
        TABLE_NAME_2_CLASS[table_name] = v
