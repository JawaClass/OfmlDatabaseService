"""Initialize Flask app."""

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.extension import SQLAlchemy as SQLAlchemyFlask
from flask_cors import CORS

db: SQLAlchemyFlask = SQLAlchemy()


def create_app():
    """Construct the core application."""

    app = Flask(__name__)

    # important so jsonify keeps the order we want
    app.json.sort_keys = False
    from settings import Config
    app.config.from_object(Config)
    print("Config Path", Config.CREATE_OFML_EXPORT_PATH)

    CORS(app, origins=['*'])

    from Service.api import oap
    from Service.api import ocd
    from Service.api import oam
    from Service.api import go
    #from Service.api import ocd_special
    from Service.api import oas
    from Service.deepcopy.ocd import api as deepcopy_ocd_api
    from Service.api import misc
    from Service.api.program_creation import api
    #app.register_blueprint(ocd_special.bp)

    app.register_blueprint(deepcopy_ocd_api.bp)

    app.register_blueprint(ocd.bp)
    app.register_blueprint(oas.bp)
    app.register_blueprint(oam.bp)
    app.register_blueprint(oap.bp)
    app.register_blueprint(go.bp)
    app.register_blueprint(misc.bp)
    app.register_blueprint(api.bp)

    # web ofml
    from Service.web_ofml.api import session
    from Service.web_ofml.api import user
    from Service.web_ofml.api import article_item
    from Service.web_ofml.api import property_item
    from Service.web_ofml.api import web_ocd
    app.register_blueprint(session.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(article_item.bp)
    app.register_blueprint(property_item.bp)
    app.register_blueprint(web_ocd.bp)

    # Initialize Database Plugin
    db.init_app(app)
    from .web_ofml import models

    with app.app_context():
        db.create_all()

    @app.errorhandler(Exception)
    def handle_exception(e: Exception):
        error_name = str(type(e).__name__)
        error_message = str(e)
        print(f"ERROR :: handle_exception({error_name})")
        print(f"-> {error_message}")
        import sys
        import traceback
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)

        return jsonify({
            'error': error_name,
            'message': error_message,
        }), 400

    @app.route("/")
    def hello():
        return "hello (app is running)"

    return app
