from celery import Celery, Task
from flask import Flask


def celery_init_app(flask_app: Flask) -> Celery:
    class FlaskTask(Task):
        def run(self, *args, **kwargs):
            pass

        def __call__(self, *args: object, **kwargs: object) -> object:
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    app = Celery("tasks",
                 task_cls=FlaskTask,
                 # backend="rpc://rabbit_user:rabbit_password@pdf2obs01",
                 backend="db+mysql+mysqlconnector://root:@pdf2obs01.kn.local/celery",
                 broker="amqp://rabbit_user:rabbit_password@pdf2obs01",

                 include=["Service.api.deepcopy.ocd.tasks"]
                 )

    app.set_default()
    flask_app.extensions["celery"] = app

    return app

"""
celery --app wsgi:celery_app worker --hostname 'worker@%h' --loglevel INFO --concurrency 5 --pool threads
"""

# from __future__ import absolute_import
#
# import time
# from random import random
#
# from celery import Celery
#
# # TODO: implement with flask https://flask.palletsprojects.com/en/2.3.x/patterns/celery/
# app = Celery(
#     "tasks",
#     backend="rpc://rabbit_user:rabbit_password@pdf2obs01",
#     broker="amqp://rabbit_user:rabbit_password@pdf2obs01",
#     # include=[
#     #     "my_tasks"
#     # ],
#     # broker_connection_retry_on_startup=True
# )
#
#
# @app.task()
# def add(x, y):
#     # time.sleep(random() * 10)
#     return x + y
#
#
# @app.task()
# def say_hello():
#     return "hello"
