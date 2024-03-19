import time

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


def check_exists(row: dict[str, object], keys: list[str], into_table: str, cursor):
    where_clause = " AND ".join([f"{k} = %s" for k in keys])
    sql_check = f"SELECT 1 FROM {into_table} WHERE {where_clause}"
    where_values = [row[key] for key in keys]
    cursor.execute(sql_check, where_values)
    """ fetchone() throws "Unread result found" error sometimes, so we use fetchall() """
    exists = bool(cursor.fetchall())
    return exists


def make_insert_statement(*, row: dict, into_table: str):
    columns = ', '.join(row.keys())
    values_template = ', '.join(['%s'] * len(row))
    return f"INSERT INTO {into_table} ({columns}) VALUES ({values_template})"


def merge_row(*, row: dict, into_table: str, web_program_name: str, cursor, keys):
    # del row["db_key"]
    # row["web_filter"] = 0
    # row["web_program_name"] = web_program_name
    exists = check_exists(row, keys, into_table, cursor)

    if exists:
        return 0

    # columns = ', '.join(row.keys())
    # values_template = ', '.join(['%s'] * len(row))
    values = [str(_) for _ in row.values()]

    sql_insert = make_insert_statement(row=row, into_table=into_table) # f"INSERT INTO {into_table} ({columns}) VALUES ({values_template})"
    print("sql_insert", sql_insert, "::", values)
    cursor.execute(sql_insert, values)
    return 1


def merge_rows_into_table_based_on(keys: list[str],
                                   new_rows: list[dict],
                                   into_table: str,
                                   web_program_name: str,
                                   connection,
                                   bulk_mode: bool = False):
    print(f"merge_rows_into_table_based_on :: {keys} = {len(new_rows)} ==> {into_table}")
    insertion_count = 0
    with connection.cursor(dictionary=True) as c:
        if bulk_mode:
            bulk_mode_check_duplicate_idx = 0
            first_row = new_rows[bulk_mode_check_duplicate_idx]
            # print("check exists", into_table, keys, ":::", first_row)
            exists = check_exists(first_row, keys, into_table, c)
            # print("-->", exists)
            sql_insert = make_insert_statement(row=first_row, into_table=into_table)
            # print("sql_insert", sql_insert)
            data = [tuple(_.values()) for _ in new_rows]
            c.executemany(sql_insert, data)
            insertion_count = len(data)
        else:
            for row in new_rows:
                insertion_count += merge_row(row=row, into_table=into_table, web_program_name=web_program_name, keys=keys, cursor=c)
    print("insertion_count:", insertion_count)
    return insertion_count


def make_merge_return_object(*, message, time_start, status):
    return {
        "status": status,
        "message": message,
        "time": round(time.perf_counter() - time_start, 2)
    }


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


MERGE_KEYS_BULK_MODE = {
        "ocd_version": ["format_version", "web_program_name"],
        "ocd_article": ["article_nr", "sql_db_program", "web_program_name"],
        "ocd_artshorttext": ["textnr", "sql_db_program", "web_program_name"],
        "ocd_artlongtext": ["textnr", "line_nr", "sql_db_program", "web_program_name"],
        "ocd_artbase": ["article_nr", "sql_db_program", "web_program_name"],
        "ocd_codescheme": ["scheme_id", "sql_db_program", "web_program_name"],
        "ocd_packaging": ["article_nr", "sql_db_program", "web_program_name"],
        "ocd_articletaxes": ["article_nr", "sql_db_program", "web_program_name"],
        "ocd_taxscheme": ["tax_id", "sql_db_program", "web_program_name"],
        "ocd_price": ["article_nr", "sql_db_program", "web_program_name"],
        "ocd_pricetext": ["textnr", "sql_db_program", "web_program_name"],
        "ocd_rounding": ["id", "sql_db_program", "web_program_name"],
        "ocd_propertyclass": ["article_nr", "prop_class", "sql_db_program", "web_program_name"],
        "ocd_property": ["prop_class", "sql_db_program", "web_program_name"],
        "ocd_propertytext": ["textnr", "sql_db_program", "web_program_name"],
        "ocd_propclasstext": ["textnr", "sql_db_program", "web_program_name"],
        "ocd_prophinttext": ["textnr", "sql_db_program", "web_program_name"],
        "ocd_propertyvalue": ["prop_class", "sql_db_program", "web_program_name"],
        "ocd_propvaluetext": ["textnr", "sql_db_program", "web_program_name"],
        "ocd_relationobj": ["rel_obj", "sql_db_program", "web_program_name"],
        "ocd_relation": ["rel_name", "sql_db_program", "web_program_name"],
        "optproperty_dat": ["prop_class", "sql_db_program", "web_program_name"],
        "optpropvalue_txt": ["textnr", "sql_db_program", "web_program_name"],
    }
