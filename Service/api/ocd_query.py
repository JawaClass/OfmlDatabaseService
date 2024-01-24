import re

from mysql.connector.cursor import MySQLCursor

QUERIES = """
SELECT ocd_version_TEMP.*
FROM ocd_version_TEMP
ORDER BY format_version DESC
LIMIT 1
;
CREATE TEMPORARY TABLE ocd_article_TEMP_LOCAL_1
AS SELECT *
FROM ocd_article_TEMP
WHERE article_nr IN ({})
;
SELECT * FROM ocd_article_TEMP_LOCAL_1
;
SELECT DISTINCT ocd_artshorttext_TEMP.*
FROM ocd_artshorttext_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.short_textnr = ocd_artshorttext_TEMP.textnr
;
SELECT DISTINCT ocd_artlongtext_TEMP.*
FROM ocd_artlongtext_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.long_textnr = ocd_artlongtext_TEMP.textnr
;
SELECT DISTINCT ocd_artbase_TEMP.*
FROM ocd_artbase_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.article_nr = ocd_artbase_TEMP.article_nr
;
SELECT DISTINCT ocd_codescheme_TEMP.*
FROM ocd_codescheme_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.scheme_id = ocd_codescheme_TEMP.scheme_id
;
SELECT DISTINCT ocd_packaging_TEMP.*
FROM ocd_packaging_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.article_nr = ocd_packaging_TEMP.article_nr
;
CREATE TEMPORARY TABLE ocd_articletaxes_TEMP_LOCAL_1
AS SELECT DISTINCT ocd_articletaxes_TEMP.*
FROM ocd_articletaxes_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.article_nr = ocd_articletaxes_TEMP.article_nr
;
SELECT * FROM ocd_articletaxes_TEMP_LOCAL_1
;
SELECT DISTINCT ocd_taxscheme_TEMP.*
FROM ocd_taxscheme_TEMP
JOIN ocd_articletaxes_TEMP_LOCAL_1 ON ocd_articletaxes_TEMP_LOCAL_1.tax_id = ocd_taxscheme_TEMP.tax_id
;
CREATE TEMPORARY TABLE ocd_price_TEMP_LOCAL_1
AS SELECT DISTINCT ocd_price_TEMP.*
FROM ocd_price_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.article_nr = ocd_price_TEMP.article_nr
;
SELECT * FROM ocd_price_TEMP_LOCAL_1
;
SELECT ocd_pricetext_TEMP.*
FROM ocd_pricetext_TEMP
JOIN ocd_price_TEMP_LOCAL_1 ON ocd_price_TEMP_LOCAL_1.price_textnr = ocd_pricetext_TEMP.textnr
;
SELECT DISTINCT ocd_rounding_TEMP.*
FROM ocd_rounding_TEMP
JOIN ocd_price_TEMP_LOCAL_1 ON ocd_price_TEMP_LOCAL_1.rounding_id = ocd_rounding_TEMP.id
;
CREATE TEMPORARY TABLE ocd_propertyclass_TEMP_LOCAL_1
AS SELECT DISTINCT ocd_propertyclass_TEMP.*
FROM ocd_propertyclass_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.article_nr = ocd_propertyclass_TEMP.article_nr
;
SELECT * FROM ocd_propertyclass_TEMP_LOCAL_1
;
SELECT ocd_propclasstext_TEMP.*
FROM ocd_propclasstext_TEMP
JOIN ocd_propertyclass_TEMP ON ocd_propertyclass_TEMP.textnr = ocd_propclasstext_TEMP.textnr
;
CREATE TEMPORARY TABLE ocd_property_TEMP_LOCAL_1
SELECT DISTINCT ocd_property_TEMP.*
FROM ocd_property_TEMP
JOIN ocd_propertyclass_TEMP_LOCAL_1 ON ocd_propertyclass_TEMP_LOCAL_1.prop_class = ocd_property_TEMP.prop_class
;
SELECT * FROM ocd_property_TEMP_LOCAL_1
;
SELECT DISTINCT ocd_propertytext_TEMP.*
FROM ocd_propertytext_TEMP
JOIN ocd_property_TEMP_LOCAL_1 ON ocd_property_TEMP_LOCAL_1.prop_textnr = ocd_propertytext_TEMP.textnr AND ocd_property_TEMP_LOCAL_1.sql_db_program = ocd_propertytext_TEMP.sql_db_program
;
SELECT DISTINCT ocd_prophinttext_TEMP.*
FROM ocd_prophinttext_TEMP
JOIN ocd_property_TEMP_LOCAL_1 ON ocd_property_TEMP_LOCAL_1.hint_text_id = ocd_prophinttext_TEMP.textnr
;
CREATE TEMPORARY TABLE ocd_propertyvalue_TEMP_LOCAL_1
SELECT DISTINCT ocd_propertyvalue_TEMP.*
FROM ocd_propertyvalue_TEMP
JOIN ocd_property_TEMP_LOCAL_1 ON (ocd_property_TEMP_LOCAL_1.prop_class = ocd_propertyvalue_TEMP.prop_class
AND ocd_property_TEMP_LOCAL_1.property = ocd_propertyvalue_TEMP.property AND ocd_property_TEMP_LOCAL_1.sql_db_program = ocd_propertyvalue_TEMP.sql_db_program   )
;
SELECT * FROM ocd_propertyvalue_TEMP_LOCAL_1
;
SELECT DISTINCT ocd_propvaluetext_TEMP.*
FROM ocd_propvaluetext_TEMP
JOIN ocd_propertyvalue_TEMP_LOCAL_1 ON ocd_propertyvalue_TEMP_LOCAL_1.pval_textnr = ocd_propvaluetext_TEMP.textnr  
;






-- START: make ocd_relationobj_TEMP_LOCAL_1

-- create table by inserting entries from article
CREATE TEMPORARY TABLE ocd_relationobj_TEMP_LOCAL_1
SELECT DISTINCT ocd_relationobj_TEMP.*
FROM ocd_relationobj_TEMP
JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.rel_obj = ocd_relationobj_TEMP.rel_obj
;
-- insert entries from property 
-- TODO: duplicates
INSERT INTO ocd_relationobj_TEMP_LOCAL_1
SELECT DISTINCT ocd_relationobj_TEMP.*
FROM ocd_relationobj_TEMP
JOIN ocd_property_TEMP_LOCAL_1 ON ocd_property_TEMP_LOCAL_1.rel_obj = ocd_relationobj_TEMP.rel_obj;


-- insert entries from values
-- TODO: duplicates
INSERT INTO ocd_relationobj_TEMP_LOCAL_1
SELECT DISTINCT ocd_relationobj_TEMP.*
FROM ocd_relationobj_TEMP
JOIN ocd_propertyvalue_TEMP_LOCAL_1 ON ocd_propertyvalue_TEMP_LOCAL_1.rel_obj = ocd_relationobj_TEMP.rel_obj;


-- END: make ocd_relationobj_TEMP_LOCAL_1








SELECT DISTINCT * FROM ocd_relationobj_TEMP_LOCAL_1
;
SELECT DISTINCT ocd_relation_TEMP.*
FROM ocd_relation_TEMP
JOIN ocd_relationobj_TEMP_LOCAL_1 ON ocd_relationobj_TEMP_LOCAL_1.rel_name = ocd_relation_TEMP.rel_name
;




CREATE TEMPORARY TABLE optproperty_dat_TEMP_LOCAL_1
SELECT DISTINCT optproperty_dat_TEMP.*
FROM optproperty_dat_TEMP
JOIN ocd_propertyclass_TEMP_LOCAL_1 ON optproperty_dat_TEMP.prop_class = ocd_propertyclass_TEMP_LOCAL_1.prop_class
;

SELECT * FROM optproperty_dat_TEMP_LOCAL_1
;



SELECT DISTINCT optpropvalue_txt_TEMP.*
FROM optpropvalue_txt_TEMP
JOIN (SELECT DISTINCT optproperty_dat_TEMP_LOCAL_1.prop_textnr FROM optproperty_dat_TEMP_LOCAL_1) AS prop_text_numbers
ON optpropvalue_txt_TEMP.textnr = prop_text_numbers.prop_textnr
;


"""
# remove lines that start with -- (sql comments)
# and lines that only contain whitespace
QUERIES = re.sub(r'\s*--.*?\n', '\n', QUERIES, flags=re.MULTILINE)

# CREATE TEMPORARY TABLE ocd_relationobj_TEMP_LOCAL_1
# SELECT ocd_relationobj_TEMP.*
# FROM ocd_relationobj_TEMP
# JOIN ocd_article_TEMP_LOCAL_1 ON ocd_article_TEMP_LOCAL_1.rel_obj = ocd_relationobj_TEMP.rel_obj
# LEFT JOIN ocd_property_TEMP_LOCAL_1 ON ocd_property_TEMP_LOCAL_1.rel_obj = ocd_relationobj_TEMP.rel_obj
# LEFT JOIN ocd_propertyvalue_TEMP_LOCAL_1 ON ocd_propertyvalue_TEMP_LOCAL_1.rel_obj = ocd_relationobj_TEMP.rel_obj
# ;


# relationobj ::: 1;2;000000000000151673_BASIC4;3;P

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


def _querie_tables(articles: list, cursor: MySQLCursor):
    global QUERIES
    placeholders = ', '.join(['%s'] * len(articles))
    c: MySQLCursor
    for i, c in enumerate(cursor.execute(QUERIES.format(placeholders), articles, multi=True)):
        if c.statement.startswith("SELECT"):
            table_name_idx = 4 if c.statement.startswith("SELECT DISTINCT") else 3
            table_name = c.statement.split()[table_name_idx].replace("_TEMP_LOCAL_1", "").replace("_TEMP", "")
            yield c.fetchall(), table_name


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


def execute(articles: list, cursor: MySQLCursor, programs: list = None):
    """
    if not program string list is given we fetch all programs where articles is present
    if programs is given we search articles in only these given programs
    """
    if programs is None:
        programs = _get_programs(articles, cursor)
    _create_temporary_tables(programs, cursor)
    return _querie_tables(articles, cursor)
