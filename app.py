from flask import Flask, stream_with_context, Response, request, jsonify, session
from flask_session import Session
import json
import db
import time
from flask_cors import CORS

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'your_secret_key'
#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
SESSION_TYPE = "redis"
app.config.from_object(__name__)
Session(app)
CORS(app)

@app.route('/')
def hello():
    response = jsonify({'HELLO': 'WORLD'})
    return response

@app.route('/ocd/all_tables/', defaults={'stream': True}, methods=['POST'])
@app.route('/ocd/all_tables/<int:stream>', methods=['POST'])
def ocd_all_tables(stream):
    print("fetch ocd_all_tables", stream)
    data = request.get_json()
    assert type(data) is list
    result = db.yield_all_tables(articlenumbers=data)
    print("type result", type(result))
    if stream:
        @stream_with_context
        def generate():
            for _ in result:
                yield json.dumps(_)
        return generate()
    else:
        return Response(json.dumps(list(result)), content_type='application/json;charset=utf-8', status=200)


@app.route('/ocd/article_data', methods=['POST'])
def article_info():
    """
    expects JSON list as body, eg. ["TLTN16880A", "TLTN18880A", "TLTN20880A"]
    """
    print("article_info called!")
    data = request.get_json()
    assert type(data) is list
    return jsonify(db.article_table(articlenumbers=data))
    
@app.route('/stream', methods=['GET'])
def stream_test():
    @stream_with_context
    def stream():
        for i in range(5):
            print("stream yields", i, time.time())
            yield json.dumps(i)
    return Response(stream(), mimetype='text/event-stream') 

@app.route('/no_stream', methods=['GET'])
def no_stream():
    return json.dumps(list(range(1000)))

@app.route('/progress')
def progress():
    print("/progress called", "session:", session.items())
    def progress_func():
        x = 0
        while x < 100:
            time.sleep(1)
            x = x + 10
            yield 'data:' + str(x) + "\n\n"
    return Response(progress_func(), mimetype='text/event-stream')

@app.route('/post_articlenumbers_to_session', methods=['POST'])
def post_articlenumbers_to_session():
    session["articlesnumbers"] = ["a1", "a2", "a3"]
    print("SET articlenumbers to session:", session.items(), session)
    return jsonify()


@app.route("/set")
def set():
    session["ok"] = "value"
    print("set", session["ok"])
    return "ok", 200


@app.route("/get")
def get():
    value = session.get("ok", "NO VALUE!")
    print("get", value)
    return value, 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
