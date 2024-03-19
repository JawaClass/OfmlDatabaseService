"""Initialize Flask app."""
import time
from pprint import pprint

from celery import Celery
from celery.app.control import Inspect
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.extension import SQLAlchemy as SQLAlchemyFlask
from flask_cors import CORS

from Service.api.tasks.celery_app import celery_init_app
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

    """ celery """
    celery_init_app(app)

    from Service.api.ofml import oap
    from Service.api.ofml import ocd
    from Service.api.ofml import oam
    from Service.api.ofml import go
    from Service.api.ofml import oas
    from Service.api.deepcopy.ocd import api as deepcopy_ocd_api
    from Service.api.ofml import misc
    from Service.api.export_program import api

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
    from Service.api.tasks.tasks import add_together, say_hello

    @app.get("/add")
    def get_add_together() -> dict[str, object]:
        print("start_add")

        result = add_together.delay(5, 3)
        return {"result_id": result.id}

    @app.get("/hello")
    def get_say_hello() -> dict[str, object]:
        result: AsyncResult = say_hello.delay()

        time.sleep(0.5)
        print("ready ? ", result.id, result.ready(), AsyncResult(result.id).ready(), AsyncResult("0d7b01a8-d713-406b-8131-5ac72b741100").ready())

        return {"result_id": result.id}

    from celery.result import AsyncResult

    @app.get("/result/<result_id>")
    def task_result(result_id: str):
        result: AsyncResult = AsyncResult(result_id)
        return {
            "result_id": result.id,
            "status": {
                "ready": result.ready(),
                "successful": result.successful(),
                "value": result.result if result.ready() else None,
                "date_done": result.date_done
            }
        }, 200

    @app.post("/tasks")
    def get_celery_tasks():
        task_ids = request.json

        def make_task_status(task_id: str):

            result: AsyncResult = AsyncResult(task_id)
            assert result.id == task_id, "???"

            def get_result_object(result):
                if result.ready():
                    task_result_object = result.result

                    if isinstance(task_result_object, Exception):
                        task_result_object = str(task_result_object)
                    return task_result_object
                return None

            return {
                "task_id": result.id,
                "ready": result.ready(),
                "successful": result.successful(),
                "value": get_result_object(result),
                "date_done": result.date_done.strftime("%H:%M:%S") if result.date_done else None
            }

        return [make_task_status(task_id) for task_id in task_ids], 200

    return app
