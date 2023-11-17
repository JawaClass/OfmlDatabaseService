"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__)

    # important so jsonify keeps the order we want
    app.json.sort_keys = False

    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="mysql+mysqlconnector://root:@pdf2obs01/ofml"
    )

    CORS(app, origins=[
        "http://0.0.0.0:4201", "http://localhost:4201", "http://127.0.0.1:4201", "http://172.22.15.238:4201",
        "http://0.0.0.0:4200", "http://localhost:4200", "http://127.0.0.1:4200", "http://172.22.15.238:4200",
    ])

    from Service.api import oap
    from Service.api import ocd
    from Service.api import oam
    from Service.api import go
    from Service.api import ocd_special
    from Service.api import oas
    app.register_blueprint(ocd_special.bp)
    app.register_blueprint(ocd.bp)
    app.register_blueprint(oas.bp)
    app.register_blueprint(oam.bp)
    app.register_blueprint(oap.bp)
    app.register_blueprint(go.bp)

    # Initialize Database Plugin
    db.init_app(app)

    @app.route("/")
    def hello():
        return "hello (app is running)"

    return app
