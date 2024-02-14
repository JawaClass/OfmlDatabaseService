from pydantic import BaseModel

from Service.tables.ocd import OcdArticle
from Service.tables.web.ocd import WebOcdArticle
from Service import db as flask_db


class MergeAsRequest(BaseModel):
    article: str
    program: str
    merge_with: str
    merge_as: str


class DeepcopyRequest(BaseModel):
    name: str
    owner_id: int
    is_public: bool
    article_input: str
    articlenumbers_and_programs: list[tuple[str, str]]


def check_web_article_exists(*, web_program_name, program, article):
    return bool(
        flask_db.session.query(WebOcdArticle.query.filter(
            WebOcdArticle.web_program_name == web_program_name,
            WebOcdArticle.sql_db_program == program,
            WebOcdArticle.article_nr == article
        ).exists()).scalar()
    )


def check_article_exists(*, program, article):
    return bool(
        flask_db.session.query(OcdArticle.query.filter(
            OcdArticle.sql_db_program == program,
            OcdArticle.article_nr == article
        ).exists()).scalar()
    )


WEB_OCD_TABLES = f"""
    web_ocd_artbase           
    web_ocd_article           
    web_ocd_articletaxes      
    web_ocd_artlongtext       
    web_ocd_artshorttext      
    web_ocd_codescheme        
    web_ocd_identification    
    web_ocd_identification_csv
    web_ocd_packaging         
    web_ocd_price             
    web_ocd_pricetext         
    web_ocd_propclasstext     
    web_ocd_property          
    web_ocd_propertyclass     
    web_ocd_propertytext      
    web_ocd_propertyvalue     
    web_ocd_prophinttext      
    web_ocd_propvaluetext     
    web_ocd_relation          
    web_ocd_relationobj       
    web_ocd_rounding          
    web_ocd_set_csv           
    web_ocd_taxscheme         
    web_ocd_usermessage       
    web_ocd_usermessage_csv   
    web_ocd_version           
    web_optproperty_dat       
    web_optpropvalue_txt      
        """.split()


def make_delete_statement(web_program_name: str):
    return "\n".join([f"DELETE FROM  {table} WHERE web_program_name = \"{web_program_name}\"; " for table in WEB_OCD_TABLES])


def make_select_statement(web_program_name: str):
    return "\n".join([f"SELECT * FROM  {table} WHERE web_program_name = \"{web_program_name}\" AND (web_filter = 0 OR web_filter IS NULL);" for table in WEB_OCD_TABLES])


MERGE_KEYS = {
        "ocd_version": ["format_version", "web_program_name"],
        "ocd_article": ["article_nr", "sql_db_program", "web_program_name"],
        "ocd_artshorttext": ["textnr", "sql_db_program", "web_program_name"],
        "ocd_artlongtext": ["textnr", "line_nr", "sql_db_program", "web_program_name"],
        "ocd_artbase": ["article_nr", "prop_class", "property", "prop_value", "sql_db_program", "web_program_name"],
        "ocd_codescheme": ["scheme_id", "sql_db_program", "web_program_name"],
        "ocd_packaging": ["article_nr", "sql_db_program", "web_program_name"],
        "ocd_articletaxes": ["article_nr", "sql_db_program", "web_program_name"],
        "ocd_taxscheme": ["tax_id", "sql_db_program", "web_program_name"],
        "ocd_price": ["article_nr", "var_cond", "price_type", "price_level", "sql_db_program", "web_program_name"],
        "ocd_pricetext": ["textnr", "sql_db_program", "web_program_name"],
        "ocd_rounding": ["id", "sql_db_program", "web_program_name"],
        "ocd_propertyclass": ["article_nr", "prop_class", "sql_db_program", "web_program_name"],
        "ocd_property": ["prop_class", "property", "sql_db_program", "web_program_name"],
        "ocd_propertytext": ["textnr", "sql_db_program", "web_program_name"],
        "ocd_propclasstext": ["textnr", "sql_db_program", "web_program_name"],
        "ocd_prophinttext": ["textnr", "sql_db_program", "web_program_name"],
        "ocd_propertyvalue": ["prop_class", "property", "value_from", "sql_db_program", "web_program_name"],
        "ocd_propvaluetext": ["textnr", "sql_db_program", "web_program_name"],
        "ocd_relationobj": ["rel_obj", "position", "rel_name", "rel_type", "rel_domain", "sql_db_program", "web_program_name"],
        "ocd_relation": ["rel_name", "rel_blocknr", "sql_db_program", "web_program_name"],
        "optproperty_dat": ["prop_class", "property", "sql_db_program", "web_program_name"],
        "optpropvalue_txt": ["textnr", "sql_db_program", "web_program_name"],
    }
