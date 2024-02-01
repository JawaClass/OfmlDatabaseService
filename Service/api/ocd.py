from flask import Blueprint, jsonify, abort, request
from sqlalchemy import text, func
from ..tables.ocd import OcdArticle, OcdPrice, OcdArtlongtext
from .handler import handle_table
from .. import db
import pandas as pd
from Service.api.program_creation.creator import ProgramCreator


bp = Blueprint("ocd", __name__, url_prefix="/ocd")


@bp.route('/programs')
def all_programs():
    res = OcdArticle.query.with_entities(OcdArticle.sql_db_program).distinct().all()
    res = [_[0] for _ in res]
    return jsonify(res)


@bp.route('/longtext_and_price/<article_nr>/<program>')
def longtext_and_price(article_nr: str, program: str):
    # print("longtext_and_price")
    price_item = OcdPrice.query.filter(
        OcdPrice.article_nr == article_nr.upper(),
        OcdPrice.sql_db_program == program.lower(),
        OcdPrice.price_type == "S",
        OcdPrice.price_level == "B",
    ).first()
    # print("price_item", price_item.article_nr, price_item.price)

    article_item = OcdArticle.query.filter(
        OcdArticle.article_nr == article_nr.upper(),
        func.upper(OcdArticle.sql_db_program) == program.upper(),
    ).first()

    longtext_item = OcdArtlongtext.query.filter(
        OcdArtlongtext.textnr == article_item.long_textnr,
        func.upper(OcdArtlongtext.language) == "DE",
        OcdArtlongtext.sql_db_program == program.upper(),
    ).all()

    # print("article_item", article_item.article_nr, article_item.long_textnr)
    # for _ in longtext_item:
    #     print("longtext_item", _.textnr, _.language, _.text)

    return jsonify(
        {
            "price": float(price_item.price),
            "longtext": [_.text for _ in longtext_item]
        }
    )


@bp.route('/table/<program>/<table_name>')
def table(program, table_name):
    if not str(table_name).startswith("ocd_"):
        abort(404, description=f"Table {table_name} not part of OCD.")
    return handle_table(program, table_name)


@bp.route('/article_compact', methods=['POST', "GET"])
def article_compact():
    """
    expects JSON list as body, eg. ["TLTN16880A", "TLTN18880A", "TLTN20880A"]
    """
    print("article_info called!")

    if request.method == 'POST':
        articles = request.get_json()
    elif request.method == 'GET':
        articles = request.args.get("articles").split(",") #"B4TAX248840A".split() #"S6AP1000A TLATRTL08800B2 TLTN16880A TLTN18880A Q3HO1SE".split()
        print("article_compact", articles)
    else:
        return abort(404)

    print("articles::::", articles)

    if not articles:
        return jsonify([])

    assert type(articles) is list

    query = """
    SELECT ocd_article.article_nr, ocd_article.series, ocd_article.sql_db_program, ocd_artshorttext.text
    FROM ocd_article
    LEFT JOIN ocd_artshorttext
    ON ocd_article.short_textnr = ocd_artshorttext.textnr AND ocd_article.sql_db_program = ocd_artshorttext.sql_db_program
    WHERE ocd_article.article_nr IN ({})
    AND UPPER(ocd_artshorttext.language) = "DE"
    ;
    """
    params = [f":p{i}" for i in list(range(len(articles)))]
    placeholders = ', '.join(params)
    bind_params = {f"{p[1:]}": a for a, p in zip(articles, params)}
    query = query.format(placeholders)

    res = db.session.execute(
        text(query),
        bind_params
    ).fetchall()

    for _ in res:
        print(_)
    return jsonify([
        {
            "article_nr": _[0],
            "series": _[1],
            "sql_db_program": _[2],
            "ocd_artshorttext": _[3]
        }
        for _ in res])
    #
    # if not res:
    #     return jsonify([])
    #
    # # Create a DataFrame
    # df = pd.DataFrame(res, columns=['article_nr', 'series', 'sql_db_program', 'shorttext', 'prop_class'])
    #
    # def formatted_rows(r: pd.DataFrame) -> dict[str, str | int]:
    #
    #     def format_article(article_df: pd.DataFrame):
    #         return article_df
    #
    #     return r.groupby("article_nr").apply(lambda a: format_article(a)).apply(lambda a: a.to_dict(), axis=1).to_list()
    #
    # nested_grouped_data = df.groupby('sql_db_program') \
    #     .apply(lambda x:
    #            x.groupby('prop_class').apply(lambda y: formatted_rows(y)).to_dict()) \
    #     .to_dict()
    #
    # return jsonify(nested_grouped_data)


@bp.route('/props_compact/<program>/<prop_class>', methods=["GET"])
def props_compact(program, prop_class):

    print("props_compact called!",  program, prop_class)

    query = f"""
SELECT simple_ocd_property.pos_prop, simple_ocd_property.prop_type, simple_ocd_property.property, simple_ocd_property.text, simple_ocd_propertyvalue.value_from, simple_ocd_propertyvalue.text, simple_ocd_property.prop_class, simple_ocd_property.sql_db_program
FROM
(SELECT ocd_propertyvalue.prop_class, ocd_propertyvalue.property, ocd_propertyvalue.value_from, ocd_propvaluetext.text
FROM ocd_propertyvalue
LEFT JOIN (SELECT * FROM ocd_propvaluetext WHERE UPPER(ocd_propvaluetext.language) = "DE") ocd_propvaluetext ON ocd_propertyvalue.pval_textnr = ocd_propvaluetext.textnr
WHERE ocd_propertyvalue.sql_db_program = "{program}"
AND ocd_propertyvalue.prop_class = "{prop_class}"
AND ocd_propvaluetext.sql_db_program = "{program}") simple_ocd_propertyvalue
,
(SELECT ocd_property.prop_class, ocd_property.property, ocd_propertytext.text, ocd_property.scope, ocd_property.sql_db_program, ocd_property.pos_prop, ocd_property.prop_type
FROM ocd_property
LEFT JOIN (SELECT * FROM ocd_propertytext WHERE UPPER(ocd_propertytext.language) = "DE") ocd_propertytext ON ocd_property.prop_textnr = ocd_propertytext.textnr
WHERE ocd_property.scope = "C" 
AND ocd_property.sql_db_program = "{program}"
AND ocd_property.prop_class = "{prop_class}"
AND ocd_propertytext.sql_db_program = "{program}"
) simple_ocd_property
WHERE simple_ocd_property.prop_class = simple_ocd_propertyvalue.prop_class
AND simple_ocd_property.property = simple_ocd_propertyvalue.property
ORDER BY simple_ocd_property.pos_prop
;
    """.format(program=program, prop_class=prop_class)

    res = db.session.execute(
        text(query),

    ).fetchall()

    if not res:
        return jsonify([])

    df: pd.DataFrame = pd.DataFrame(res, columns=["pos_prop", "prop_type", 'property', 'property_text', 'value', 'value_text', 'prop_class', 'program'])

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

        prop_type = group_df['prop_type'].iloc[0]
        pos_prop = int(group_df['pos_prop'].iloc[0])
        property_name = group_df['property'].iloc[0]
        property_text = group_df['property_text'].iloc[0]

        prop_class_ = group_df['prop_class'].iloc[0]
        program_ = group_df['program'].iloc[0]

        values: pd.DataFrame = group_df.groupby("value").apply(make_value)  # .T
        values.reset_index(drop=True, inplace=True)

        # print("values for ", property_name)
        # print(values.values.tolist())

        return {
            "pos_prop": pos_prop,
            "prop_type": prop_type,
            "property_name": property_name,
            'prop_text': property_text,
            "prop_class": prop_class_,
            "program": program_,
            'values': values.values.tolist(),
        }
    print(df.to_string())
    return jsonify(list(df.groupby("property", sort=False).apply(make_group).to_dict().values()))


@bp.route('/test_ts', methods=["GET"])
def test_ts():
    return jsonify({
        "name": "herbert",
        "gender": "d",
        "age": 54
    })


@bp.route('/create', methods=["POST"])
def create_program():

    body: dict = request.get_json()
    assert body

    program_creator = ProgramCreator(body)

    return jsonify({
        "export_path": str(program_creator.export_program_path_windows)
    })
