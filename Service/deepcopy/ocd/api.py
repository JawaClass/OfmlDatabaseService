from timeit import timeit
import Service.mysql.db as db
from flask import Blueprint
from . import quey
from Service.tables.utility import get_model_class_by_table_name
import time

from ...tables.web.ocd import WebOcdArticle

bp = Blueprint("deepcopy_ocd", __name__, url_prefix="/deepcopy/ocd")

# params: program_name: str, articles: list[(article_nr, program)]
# copy ocd from

# http://localhost:5000/deepcopy/ocd/deepcopy


@bp.route('/deepcopy_delete/<string:name>', methods=["GET"])
def delete_deepcopy(name: str):
    op = f"""
DELETE FROM web_ocd_artbase             WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_article             WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_articletaxes        WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_artlongtext         WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_artshorttext        WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_codescheme          WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_identification      WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_identification_csv  WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_packaging           WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_price               WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_pricetext           WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_propclasstext       WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_property            WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_propertyclass       WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_propertytext        WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_propertyvalue       WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_prophinttext        WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_propvaluetext       WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_relation            WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_relationobj         WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_rounding            WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_set_csv             WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_taxscheme           WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_usermessage         WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_usermessage_csv     WHERE web_program_name = \"{name}\";
DELETE FROM web_ocd_version             WHERE web_program_name = \"{name}\";
DELETE FROM web_optproperty_dat         WHERE web_program_name = \"{name}\";
DELETE FROM web_optpropvalue_txt        WHERE web_program_name = \"{name}\";  
    """
    print(op)
    connection = db.new_connection()
    c = connection.cursor()
    for result in c.execute(operation=op, multi=True):
        pass # print("result", result)
    connection.commit()
    c.close()
    connection.close()
    return "deleted"


@bp.route('/deepcopy', methods=["GET"])
def deepcopy():
    start = time.perf_counter()
    # param: articlenumbers_and_programs: list[(str, str, )]
    articlenumbers_and_programs = [
        ("TLTN16880A", "talos"),
        ("TLESBF1440W1", "talos"),
        ("TLESBF164050W1", "talos"),
        ("TLESBF1640W", "talos"),
        ("TLESBF1640W1", "talos"),
        ("Q3HO1SE", "quick3"),
        ("PNESBFI30W", "screens"),
        ("S6SLV108750A", "s6"),
        ("S6AP6120B2", "s6"),
        ("S6AP6323F1", "s6"),
        ("S6AP6600A", "s6"),
        ("S6AP6600B2", "s6"),
        ("S6AP6800A", "s6"),
        ("WPAPTN", "workplace"),
        ("WPAPPBEE", "workplace"),
        ("WPAPPBEF", "workplace"),
        ("WPAPPDB", "workplace"),
        ("WPAPPFR", "workplace"),
        ("WPAPPN", "workplace"),
        ("WPAPPRA", "workplace"),
        ("OTDBG1218", "activet"),
        ("S8ETGEIV11003RB2", "s8"),
        ("S8ETGEIV11004LA", "s8"),
        ("S8ETGEIV11004LB2", "s8"),
        ("S8GTV11KR6455A1", "s8"),
        ("S8GTV11KR6456A", "s8"),
        ("S8GTV11KR6456A1", "s8"),
        ("S8SF04", "locker"),
        ("S8SF08", "locker"),
        ("S8SFM08", "locker"),
        ("S8ZAKL20", "locker"),
        ("S8ZAKL200", "locker"),
        ("S8ZBAB", "locker"),
    ]
    program_name = "test"
    connection = db.new_connection()
    c = connection.cursor(dictionary=True)

    print("/deepcopy ::", articlenumbers_and_programs)

    tables = quey.deepcopy(articlenumbers_and_programs, c, program_name, fetch=True)
    # consume...
    connection.commit()
    c.close()
    connection.close()
    t_seconds = time.perf_counter() - start
    print("perCounter", t_seconds)
    return f"ok ({t_seconds}s)"


@bp.route('/test', methods=["GET"])
# @timeit
def test():
    inst = WebOcdArticle.by_program("talos")
    print("inst", inst)
    return "ok"
