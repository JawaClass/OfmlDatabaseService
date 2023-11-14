import json
import db
import time
from flask import Response, request, jsonify, session, abort, Blueprint

bp = Blueprint("ocd_special", __name__, url_prefix="/ocd/special")


@bp.route('/all_tables/set/', methods=['GET', 'POST'])
def stream_all_tables_set():
    print("ocd_all_tables_set", request.method)
    if request.method == 'POST':

        post_data = request.get_json()
        assert type(post_data) is list
        session['articlenumbers'] = post_data

    else:  # Test
        session['articlenumbers'] = ["TLTN16880A", ]

    return session['articlenumbers'], 200


@bp.route('/all_tables/get/', methods=['GET'])
def stream_all_tables_get():
    data = session.get('articlenumbers', None)

    if not data:
        abort(404, description="""
        No articlenumbers set.
        This is a Server Side Event.
        Apply the parameter with /ocd/all_tables/set/ first to set articlenumbers""")

    del session['articlenumbers']

    result = db.yield_all_tables(articlenumbers=data)

    def stream():
        for _ in result:
            yield json.dumps(_)

    return Response(stream(), mimetype='text/event-stream')


@bp.route('/article_data', methods=['POST'])
def article_info():
    """
    expects JSON list as body, eg. ["TLTN16880A", "TLTN18880A", "TLTN20880A"]
    """
    print("article_info called!")
    data = request.get_json()
    assert type(data) is list
    return jsonify(db.article_table(articlenumbers=data))


@bp.route('/stream', methods=['GET'])
def stream_test():
    def stream():
        for i in range(5):
            print("stream yields", i, time.time())
            yield json.dumps(i)

    return Response(stream(), mimetype='text/event-stream')


@bp.route('/no_stream', methods=['GET'])
def no_stream():
    return json.dumps(list(range(1000)))


@bp.route('/progress')
def progress():
    print("/progress called", "session:", session.items())

    def progress_func():
        x = 0
        while x < 100:
            time.sleep(1)
            x = x + 10
            yield 'data:' + str(x) + "\n\n"

    return Response(progress_func(), mimetype='text/event-stream')


@bp.route('/post_articlenumbers_to_session', methods=['POST'])
def post_articlenumbers_to_session():
    session["articlesnumbers"] = ["a1", "a2", "a3"]
    print("SET articlenumbers to session:", session.items(), session)
    return jsonify()


@bp.route("/set")
def set():
    session["ok"] = "value"
    print("set", session["ok"])
    return "ok", 200


@bp.route("/get")
def get():
    value = session.get("ok", "NO VALUE!")
    print("get", value)
    return value, 200
