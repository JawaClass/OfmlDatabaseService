import re

from mysql.connector.cursor import MySQLCursor

QUERIES = """
--ocd_version-----------------------------------------------------------------------------------------------------
SELECT ocd_version_TEMP.*
FROM ocd_version_TEMP
ORDER BY format_version DESC
LIMIT 1
;
--ocd_article------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_article_TEMP_LOCAL_1
AS
SELECT *
FROM ocd_article_TEMP
WHERE article_nr IN ({placeholders})
;
INSERT INTO web_ocd_article (article_nr,art_type, manufacturer, series, short_textnr, long_textnr, rel_obj, fast_supply, discountable, order_unit, scheme_id, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                             article_nr, art_type, manufacturer, series, short_textnr, long_textnr, rel_obj, fast_supply, discountable, order_unit, scheme_id, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_article_TEMP_LOCAL_1
;
SELECT * FROM ocd_article_TEMP_LOCAL_1
;
--ocd_artshorttext------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_artshorttext_TEMP_LOCAL_1
AS
SELECT DISTINCT ocd_artshorttext_TEMP.*
FROM ocd_artshorttext_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.short_textnr = ocd_artshorttext_TEMP.textnr
;
SELECT * FROM ocd_artshorttext_TEMP_LOCAL_1
;
INSERT INTO web_ocd_artshorttext (textnr, language, line_nr, line_fmt, text, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                                  textnr, language, line_nr, line_fmt, text, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_artshorttext_TEMP_LOCAL_1
;
--ocd_artlongtext------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_artlongtext_TEMP_LOCAL_1
AS
SELECT DISTINCT ocd_artlongtext_TEMP.*
FROM ocd_artlongtext_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.long_textnr = ocd_artlongtext_TEMP.textnr
;
SELECT * FROM ocd_artlongtext_TEMP_LOCAL_1
;
INSERT INTO web_ocd_artlongtext (textnr, language, line_nr, line_fmt, text, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                                  textnr, language, line_nr, line_fmt, text, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_artlongtext_TEMP_LOCAL_1
;
--ocd_artbase------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_artbase_TEMP_LOCAL_1
AS
SELECT DISTINCT ocd_artbase_TEMP.*
FROM ocd_artbase_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.article_nr = ocd_artbase_TEMP.article_nr
;
SELECT * FROM ocd_artbase_TEMP_LOCAL_1
;
INSERT INTO web_ocd_artbase (article_nr, prop_class, property, prop_value, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                             article_nr, prop_class, property, prop_value, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_artbase_TEMP_LOCAL_1
; 
--ocd_codescheme------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_codescheme_TEMP_LOCAL_1
AS
SELECT DISTINCT ocd_codescheme_TEMP.*
FROM ocd_codescheme_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.scheme_id = ocd_codescheme_TEMP.scheme_id
;
SELECT * FROM ocd_codescheme_TEMP_LOCAL_1
;
INSERT INTO web_ocd_codescheme (scheme_id, scheme, varcode_sep, value_sep, visibility, invisible_char, unselect_char, trim, mo_sep, mo_bracket, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                                scheme_id, scheme, varcode_sep, value_sep, visibility, invisible_char, unselect_char, trim, mo_sep, mo_bracket, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_codescheme_TEMP_LOCAL_1
; 
--ocd_packaging------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_packaging_TEMP_LOCAL_1
AS
SELECT DISTINCT ocd_packaging_TEMP.*
FROM ocd_packaging_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.article_nr = ocd_packaging_TEMP.article_nr
;
SELECT * FROM ocd_packaging_TEMP_LOCAL_1 
;
INSERT INTO web_ocd_packaging (article_nr, var_cond, width, height, depth, measure_unit, volume, volume_unit, tara_weight, net_weight,  weight_unit, items_per_unit, pack_units, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                               article_nr, var_cond, width, height, depth, measure_unit, volume, volume_unit, tara_weight, net_weight,  weight_unit, items_per_unit, pack_units, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_packaging_TEMP_LOCAL_1
; 
--ocd_articletaxes------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_articletaxes_TEMP_LOCAL_1
AS
SELECT DISTINCT ocd_articletaxes_TEMP.*
FROM ocd_articletaxes_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.article_nr = ocd_articletaxes_TEMP.article_nr
;
SELECT * FROM ocd_articletaxes_TEMP_LOCAL_1
;
INSERT INTO web_ocd_articletaxes (article_nr, tax_id, date_from, date_to, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                               article_nr, tax_id, date_from, date_to, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_articletaxes_TEMP_LOCAL_1
; 
--ocd_taxscheme------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_taxscheme_TEMP_LOCAL_1
AS
SELECT DISTINCT ocd_taxscheme_TEMP.*
FROM ocd_taxscheme_TEMP
JOIN ocd_articletaxes_TEMP_LOCAL_1 ON ocd_articletaxes_TEMP_LOCAL_1.tax_id = ocd_taxscheme_TEMP.tax_id
;
SELECT * FROM ocd_taxscheme_TEMP_LOCAL_1
;
INSERT INTO web_ocd_taxscheme (tax_id, country, region, number, tax_type, tax_category, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                               tax_id, country, region, number, tax_type, tax_category, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_taxscheme_TEMP_LOCAL_1
; 
--ocd_price------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_price_TEMP_LOCAL_1
AS
SELECT DISTINCT ocd_price_TEMP.*
FROM ocd_price_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.article_nr = ocd_price_TEMP.article_nr
;
SELECT * FROM ocd_price_TEMP_LOCAL_1
;
INSERT INTO web_ocd_price (article_nr, var_cond, price_type, price_level, price_rule, price_textnr, price, is_fix, currency, date_from, date_to, scale_quantity, rounding_id, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                           article_nr, var_cond, price_type, price_level, price_rule, price_textnr, price, is_fix, currency, date_from, date_to, scale_quantity, rounding_id, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_price_TEMP_LOCAL_1
;
--ocd_pricetext------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_pricetext_TEMP_LOCAL_1
AS
SELECT ocd_pricetext_TEMP.*
FROM ocd_pricetext_TEMP
JOIN ocd_price_TEMP_LOCAL_1 ON ocd_price_TEMP_LOCAL_1.price_textnr = ocd_pricetext_TEMP.textnr
;
SELECT * FROM ocd_pricetext_TEMP_LOCAL_1
;
INSERT INTO web_ocd_pricetext (textnr, language, line_nr, line_fmt, text, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                               textnr, language, line_nr, line_fmt, text, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_pricetext_TEMP_LOCAL_1
;
--ocd_rounding------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_rounding_TEMP_LOCAL_1
AS
SELECT DISTINCT ocd_rounding_TEMP.*
FROM ocd_rounding_TEMP
JOIN ocd_price_TEMP_LOCAL_1 ON ocd_price_TEMP_LOCAL_1.rounding_id = ocd_rounding_TEMP.id
;
SELECT * FROM ocd_rounding_TEMP_LOCAL_1
;
INSERT INTO web_ocd_rounding (`id`, nr, `min`, `max`, `type` , `precision`, add_before, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                              `id`, nr, `min`, `max`, `type` , `precision`, add_before, sql_db_program, sql_db_timestamp_modified, NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_rounding_TEMP_LOCAL_1
;
--ocd_propertyclass------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_propertyclass_TEMP_LOCAL_1
AS
SELECT DISTINCT ocd_propertyclass_TEMP.*
FROM ocd_propertyclass_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.article_nr = ocd_propertyclass_TEMP.article_nr
;
SELECT * FROM ocd_propertyclass_TEMP_LOCAL_1
;
INSERT INTO web_ocd_propertyclass (`article_nr`, pos_class, `prop_class`, `textnr`, `rel_obj`, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                                   `article_nr`, pos_class, `prop_class`, `textnr`, `rel_obj`, sql_db_program, sql_db_timestamp_modified, NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_propertyclass_TEMP_LOCAL_1
;
--ocd_propclasstext------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_propclasstext_TEMP_LOCAL_1
AS
SELECT ocd_propclasstext_TEMP.*
FROM ocd_propclasstext_TEMP
JOIN ocd_propertyclass_TEMP ON ocd_propertyclass_TEMP.textnr = ocd_propclasstext_TEMP.textnr
;
SELECT * FROM ocd_propclasstext_TEMP_LOCAL_1
;
INSERT INTO web_ocd_propclasstext (textnr, language, line_nr, line_fmt, text, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                                   textnr, language, line_nr, line_fmt, text, sql_db_program, sql_db_timestamp_modified, NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_propclasstext_TEMP_LOCAL_1
;
--ocd_property------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_property_TEMP_LOCAL_1
SELECT DISTINCT ocd_property_TEMP.*
FROM ocd_property_TEMP
JOIN ocd_propertyclass_TEMP_LOCAL_1 ON ocd_propertyclass_TEMP_LOCAL_1.prop_class = ocd_property_TEMP.prop_class
;
SELECT * FROM ocd_property_TEMP_LOCAL_1
;
INSERT INTO web_ocd_property (prop_class, property, pos_prop, prop_textnr, rel_obj, prop_type, digits, dec_digits, need_input, add_values, restrictable, multi_option, scope, txt_control, hint_text_id, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                              prop_class, property, pos_prop, prop_textnr, rel_obj, prop_type, digits, dec_digits, need_input, add_values, restrictable, multi_option, scope, txt_control, hint_text_id, sql_db_program, sql_db_timestamp_modified, NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_property_TEMP_LOCAL_1
;
--ocd_propertytext------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_propertytext_TEMP_LOCAL_1
SELECT DISTINCT ocd_propertytext_TEMP.*
FROM ocd_propertytext_TEMP
JOIN ocd_property_TEMP_LOCAL_1 ON ocd_property_TEMP_LOCAL_1.prop_textnr = ocd_propertytext_TEMP.textnr AND ocd_property_TEMP_LOCAL_1.sql_db_program = ocd_propertytext_TEMP.sql_db_program
;
SELECT * FROM ocd_propertytext_TEMP_LOCAL_1
;
INSERT INTO web_ocd_propertytext (textnr, language, line_nr, line_fmt, text, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                                  textnr, language, line_nr, line_fmt, text, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_propertytext_TEMP_LOCAL_1
;
--ocd_prophinttext------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_prophinttext_TEMP_LOCAL_1
SELECT DISTINCT ocd_prophinttext_TEMP.*
FROM ocd_prophinttext_TEMP
JOIN ocd_property_TEMP_LOCAL_1 ON ocd_property_TEMP_LOCAL_1.hint_text_id = ocd_prophinttext_TEMP.textnr
;
SELECT * FROM ocd_prophinttext_TEMP_LOCAL_1
;
INSERT INTO web_ocd_prophinttext (textnr, language, line_nr, line_fmt, text, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                                  textnr, language, line_nr, line_fmt, text, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_prophinttext_TEMP_LOCAL_1
;
--ocd_propertyvalue------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_propertyvalue_TEMP_LOCAL_1
SELECT DISTINCT ocd_propertyvalue_TEMP.*
FROM ocd_propertyvalue_TEMP
JOIN ocd_property_TEMP_LOCAL_1 ON (ocd_property_TEMP_LOCAL_1.prop_class = ocd_propertyvalue_TEMP.prop_class
AND ocd_property_TEMP_LOCAL_1.property = ocd_propertyvalue_TEMP.property AND ocd_property_TEMP_LOCAL_1.sql_db_program = ocd_propertyvalue_TEMP.sql_db_program   )
;
SELECT * FROM ocd_propertyvalue_TEMP_LOCAL_1
;
INSERT INTO web_ocd_propertyvalue (prop_class, property, pos_pval, pval_textnr, rel_obj, is_default, suppress_txt, op_from, value_from, op_to, value_to, raster, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                                   prop_class, property, pos_pval, pval_textnr, rel_obj, is_default, suppress_txt, op_from, value_from, op_to, value_to, raster, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_propertyvalue_TEMP_LOCAL_1
;
--ocd_propvaluetext------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_propvaluetext_TEMP_LOCAL_1
SELECT DISTINCT ocd_propvaluetext_TEMP.*
FROM ocd_propvaluetext_TEMP
JOIN ocd_propertyvalue_TEMP_LOCAL_1 ON ocd_propertyvalue_TEMP_LOCAL_1.pval_textnr = ocd_propvaluetext_TEMP.textnr  
;
SELECT * FROM ocd_propvaluetext
;
INSERT INTO web_ocd_propvaluetext (textnr, language, line_nr, line_fmt, text, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                                   textnr, language, line_nr, line_fmt, text, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_propvaluetext_TEMP_LOCAL_1
;
--ocd_relationobj------------------------------------------------------------------------------------------------------
-- START: make ocd_relationobj_TEMP_LOCAL_1
-- create table by inserting entries from article
CREATE TEMPORARY TABLE ocd_relationobj_TEMP_LOCAL_1
SELECT DISTINCT ocd_relationobj_TEMP.*
FROM ocd_relationobj_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.rel_obj = ocd_relationobj_TEMP.rel_obj
;
-- insert entries from property 
INSERT INTO ocd_relationobj_TEMP_LOCAL_1
SELECT DISTINCT ocd_relationobj_TEMP.*
FROM ocd_relationobj_TEMP
JOIN ocd_property_TEMP_LOCAL_1 ON ocd_property_TEMP_LOCAL_1.rel_obj = ocd_relationobj_TEMP.rel_obj;
-- insert entries from values
INSERT INTO ocd_relationobj_TEMP_LOCAL_1
SELECT DISTINCT ocd_relationobj_TEMP.*
FROM ocd_relationobj_TEMP
JOIN ocd_propertyvalue_TEMP_LOCAL_1 ON ocd_propertyvalue_TEMP_LOCAL_1.rel_obj = ocd_relationobj_TEMP.rel_obj;
-- END: make ocd_relationobj_TEMP_LOCAL_1
SELECT DISTINCT * FROM ocd_relationobj_TEMP_LOCAL_1
;
INSERT INTO web_ocd_relationobj (rel_obj, position, rel_name, rel_type, rel_domain, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                                 rel_obj, position, rel_name, rel_type, rel_domain, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_relationobj_TEMP_LOCAL_1
;
--ocd_relation------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE ocd_relation_TEMP_LOCAL_1
SELECT DISTINCT ocd_relation_TEMP.*
FROM ocd_relation_TEMP
JOIN ocd_relationobj_TEMP_LOCAL_1 ON ocd_relationobj_TEMP_LOCAL_1.rel_name = ocd_relation_TEMP.rel_name
;
SELECT * FROM ocd_relation_TEMP_LOCAL_1
;
INSERT INTO web_ocd_relation (rel_name, rel_blocknr, rel_block, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                              rel_name, rel_blocknr, rel_block, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM ocd_relation_TEMP_LOCAL_1
;
--optproperty_dat------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE optproperty_dat_TEMP_LOCAL_1
SELECT DISTINCT optproperty_dat_TEMP.*
FROM optproperty_dat_TEMP
JOIN ocd_propertyclass_TEMP_LOCAL_1 ON optproperty_dat_TEMP.prop_class = ocd_propertyclass_TEMP_LOCAL_1.prop_class
;
SELECT * FROM optproperty_dat_TEMP_LOCAL_1
;
INSERT INTO web_optproperty_dat (prop_class, property, prop_textnr, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                                 prop_class, property, prop_textnr, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM optproperty_dat_TEMP_LOCAL_1
;
--optpropvalue_txt------------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE optpropvalue_txt_TEMP_LOCAL_1
SELECT DISTINCT optpropvalue_txt_TEMP.*
FROM optpropvalue_txt_TEMP
JOIN (SELECT DISTINCT optproperty_dat_TEMP_LOCAL_1.prop_textnr FROM optproperty_dat_TEMP_LOCAL_1) AS prop_text_numbers
ON optpropvalue_txt_TEMP.textnr = prop_text_numbers.prop_textnr
;
SELECT * FROM optpropvalue_txt_TEMP_LOCAL_1
;
INSERT INTO web_optpropvalue_txt (textnr, language, line_nr, line_fmt, text, sql_db_program, sql_db_timestamp_modified, db_key, sql_db_timestamp_read, web_program_name, web_filter)
SELECT                
                                  textnr, language, line_nr, line_fmt, text, sql_db_program, sql_db_timestamp_modified,   NULL, sql_db_timestamp_read, \"{web_program_name}\", 0
FROM optpropvalue_txt_TEMP_LOCAL_1
;
"""
# remove lines that start with -- (sql comments)
# and lines that only contain whitespace
QUERIES = re.sub(r"(\s*--.*?\n)|(\s*?\n)", '\n', QUERIES, flags=re.MULTILINE)

TABLES = """
    ocd_version
    ocd_article
	ocd_artshorttext
	ocd_artlongtext
	ocd_artbase
    ocd_codescheme 
	ocd_packaging 
	ocd_articletaxes 
    ocd_taxscheme  
    ocd_price
    ocd_pricetext 
    ocd_rounding 
    ocd_propertyclass 
    ocd_propclasstext 
    ocd_property
    ocd_propertytext 
    ocd_prophinttext 
    ocd_propertyvalue 
    ocd_propvaluetext 
    ocd_relationobj 
    ocd_relation

    optproperty_dat
    optpropvalue_txt
    """.split()


def _querie_tables(articles: list, cursor: MySQLCursor, web_program_name: str, fetch: bool):
    print("_querie_tables")
    global QUERIES
    placeholders = ', '.join(['%s'] * len(articles))
    c: MySQLCursor
    operation = QUERIES.format(placeholders=placeholders, web_program_name=web_program_name)
    print("operation")
    print(operation)
    cursor_generator = cursor.execute(
                operation=operation,
                params=articles,
                multi=True
            )

    # if not fetch:
    #     return
    print("_querie_tables cursor_generator = ", cursor_generator)
    for i, c in enumerate(cursor_generator):
        print(c.statement[0:30])
        if c.statement.startswith("SELECT"):
            table_name_idx = 4 if c.statement.startswith("SELECT DISTINCT") else 3
            table_name = c.statement.split()[table_name_idx].replace("_TEMP_LOCAL_1", "").replace("_TEMP", "")
            # yield c.fetchall(), table_name
        elif c.statement.startswith("INSERT INTO"):
            print("Statement...................")
            print(c.statement)
            print(".")


def _create_temp_table(table_name: str, programs: list, cursor: MySQLCursor):
    placeholders = ', '.join(['%s'] * len(programs))

    sql = f"""
    CREATE TEMPORARY TABLE {table_name}_TEMP
    AS SELECT *
    FROM {table_name}
    WHERE sql_db_program IN ({placeholders});
    """
    cursor.execute(sql, programs)


def _create_temporary_tables(programs: list, cursor: MySQLCursor):
    print("_create_temporary_tables")
    for table_name in TABLES:
        _create_temp_table(table_name, programs, cursor)


def _get_programs(articles: list, cursor: MySQLCursor):
    placeholders = ', '.join(['%s'] * len(articles))
    sql = f"""
    SELECT DISTINCT sql_db_program FROM ocd_article WHERE article_nr IN ({placeholders})
    """
    cursor.execute(sql, articles)
    result = list(map(lambda x: x['sql_db_program'], cursor.fetchall()))
    return result


# def execute(articles: list, cursor: MySQLCursor, programs: list = None):
#     """
#     if not program string list is given we fetch all programs where articles is present
#     if programs is given we search articles in only these given programs
#     """
#     if programs is None:
#         programs = _get_programs(articles, cursor)
#     _create_temporary_tables(programs, cursor)
#     return _querie_tables(articles, cursor)

def deepcopy(articles_and_programs: list[(str, str,)], cursor: MySQLCursor, web_program_name: str, fetch: bool):
    """
    articles: list of article;program tuples
    """
    print("deepcopy")
    articles = list(set([_[0] for _ in articles_and_programs]))
    programs = list(set([_[1] for _ in articles_and_programs]))
    _create_temporary_tables(programs, cursor)
    rt = _querie_tables(articles, cursor, web_program_name, fetch)
    # input(f"..... {rt}")
    return rt
