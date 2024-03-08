"""Initialize Flask app."""
import copy
import sys

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.extension import SQLAlchemy as SQLAlchemyFlask
from flask_cors import CORS
from Service.util import template_logger

db: SQLAlchemyFlask = SQLAlchemy()


def create_app():
    """Construct the core application."""

    app = Flask(__name__.split('.')[0])

    # important so jsonify keeps the order we want
    app.json.sort_keys = False
    from settings import Config
    app.config.from_object(Config)

    CORS(app, origins=['*'])

    from Service.api.ofml import oap
    from Service.api.ofml import ocd
    from Service.api.ofml import oam
    from Service.api.ofml import go
    #from Service.api import ocd_special
    from Service.api.ofml import oas
    from Service.api.deepcopy.ocd import api as deepcopy_ocd_api
    from Service.api.ofml import misc
    from Service.api.export_program import api
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
    from Service.api.web_ofml.api import user
    from Service.api.web_ofml.api import web_ocd
    from Service.api.web_ofml.api import web_ocd_batch
    app.register_blueprint(user.bp)
    app.register_blueprint(web_ocd.bp)
    app.register_blueprint(web_ocd_batch.bp)

    # Initialize Database Plugin
    db.init_app(app)

    with app.app_context():
        """
        Create tables that do not exist in the database by calling
        ``metadata.create_all()`` for all or some bind keys.
        This does not update existing tables, use a migration library for that.
        """
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
        return "Ofml Database Service is running."

    return app
