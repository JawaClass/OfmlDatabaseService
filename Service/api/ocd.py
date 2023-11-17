from flask import Blueprint, jsonify, abort, request
from sqlalchemy import text

from ..tables import OcdArticle
from .handler import handle_table, prepare_json
from .. import db
import pandas as pd

bp = Blueprint("ocd", __name__, url_prefix="/ocd")


@bp.route('/programs')
def programs():
    res = OcdArticle.query.with_entities(OcdArticle.sql_db_program).distinct().all()
    res = [_[0] for _ in res]
    return jsonify(res)


@bp.route('/table/<program>/<table_name>/<column>/<value>')
@bp.route('/table/<program>/<table_name>')
def table(program, table_name, column=None, value=None):
    if not str(table_name).startswith("ocd_"):
        abort(404, description=f"Table {table_name} not part of OCD.")
    return handle_table(program, table_name, column, value)


@bp.route('/article_compact', methods=['POST', "GET"])
def article_compact():
    """
    expects JSON list as body, eg. ["TLTN16880A", "TLTN18880A", "TLTN20880A"]
    """
    print("article_info called!")

    if request.method == 'POST':
        articles = request.get_json()
    elif request.method == 'GET':
        articles = "S6AP1000A TLATRTL08800B2 TLTN16880A TLTN18880A Q3HO1SE".split()

    else:
        return abort(404)

    assert type(articles) is list

    query = """
    SELECT ocd_article.article_nr, ocd_article.series, ocd_article.sql_db_program, ocd_artshorttext.text, ocd_propertyclass.prop_class
    FROM ocd_article
    LEFT JOIN (SELECT * FROM ocd_artshorttext WHERE UPPER(ocd_artshorttext.language) = "DE") ocd_artshorttext
    ON ocd_article.short_textnr = ocd_artshorttext.textnr
    JOIN ocd_propertyclass ON (ocd_propertyclass.article_nr = ocd_article.article_nr AND ocd_propertyclass.sql_db_program = ocd_article.sql_db_program)
    WHERE ocd_article.article_nr IN ({})
    ;
    """

    placeholders = ', '.join(list(map(lambda a: f":{a}", articles)))
    query = query.format(placeholders)
    bind_params = {f"{a}": a for a in articles}

    res = db.session.execute(
        text(query),
        bind_params
    ).fetchall()

    for row in res:
        print(row)
    # Create a DataFrame
    df = pd.DataFrame(res, columns=['article_nr', 'series', 'sql_db_program', 'shorttext', 'prop_class'])

    def formatted_rows(r: pd.DataFrame) -> dict[str, str | int]:
        return r.apply(lambda a: a.to_dict(), axis=1).to_list()

    nested_grouped_data = df.groupby('sql_db_program') \
        .apply(lambda x:
               x.groupby('prop_class').apply(lambda y: formatted_rows(y)).to_dict()) \
        .to_dict()

    return jsonify(nested_grouped_data)


@bp.route('/props_compact/<program>/<prop_class>', methods=["GET"])
def props_compact(program, prop_class):
    """
    expects JSON list as body, eg. ["TLTN16880A", "TLTN18880A", "TLTN20880A"]
    """

    print("props_compact called!")
    print("program =", program)
    print("prop_class =", prop_class)

    query = f"""
SELECT simple_ocd_property.property, simple_ocd_property.text, simple_ocd_propertyvalue.value_from, simple_ocd_propertyvalue.text
FROM
(SELECT ocd_propertyvalue.prop_class, ocd_propertyvalue.property, ocd_propertyvalue.value_from, ocd_propvaluetext.text
FROM ocd_propertyvalue
LEFT JOIN (SELECT * FROM ocd_propvaluetext WHERE UPPER(ocd_propvaluetext.language) = "DE") ocd_propvaluetext ON ocd_propertyvalue.pval_textnr = ocd_propvaluetext.textnr
WHERE ocd_propertyvalue.sql_db_program = "{program}"
AND ocd_propertyvalue.prop_class = "{prop_class}"
AND ocd_propvaluetext.sql_db_program = "{program}") simple_ocd_propertyvalue
,
(SELECT ocd_property.prop_class, ocd_property.property, ocd_propertytext.text, ocd_property.scope
FROM ocd_property
LEFT JOIN (SELECT * FROM ocd_propertytext WHERE UPPER(ocd_propertytext.language) = "DE") ocd_propertytext ON ocd_property.prop_textnr = ocd_propertytext.textnr
WHERE ocd_property.scope = "C" 
AND ocd_property.sql_db_program = "{program}"
AND ocd_property.prop_class = "{prop_class}"
AND ocd_propertytext.sql_db_program = "{program}") simple_ocd_property
WHERE simple_ocd_property.prop_class = simple_ocd_propertyvalue.prop_class
AND simple_ocd_property.property = simple_ocd_propertyvalue.property
;
    """.format(program=program, prop_class=prop_class)

    res = db.session.execute(
        text(query),

    ).fetchall()

    df: pd.DataFrame = pd.DataFrame(res, columns=['property', 'property_text', 'value', 'value_text'])

    def make_group(group_df: pd.DataFrame):
        """
        group_df: dataframe with specified columns describing 1 property and its values
        """
        def make_value(x: pd.DataFrame):

            x.reset_index(inplace=True, drop=True)
            assert x.shape[0] == 1

            v = x.iloc[0]["value"]
            t = x.iloc[0]["value_text"]
            return {
                "v": v,
                "text": t
            }

        property_name = group_df['property'].iloc[0]
        property_text = group_df['property_text'].iloc[0]
        values: pd.DataFrame = group_df.groupby("value").apply(make_value)#.T
        values.reset_index(drop=True, inplace=True)

        print("values for ", property_name)
        print(values.values.tolist())

        return {
            "property_name": property_name,
            'prop_text': property_text,
            'values': values.values.tolist()# values.to_dict()#.to_list()

        }

    return jsonify(list(df.groupby("property").apply(make_group).to_dict().values()))
