# from celery import Celery
#
#
# app = Celery(
#     "celery2",
#     backend="rpc://rabbit_user:rabbit_password@pdf2obs01",
#     broker="amqp://rabbit_user:rabbit_password@pdf2obs01",
#     include=[
#         #"Service.api.tasks.task",
#         # __name__
#         "Service.api.tasks"
#     ],
#     broker_connection_retry_on_startup=True
# )
#
# """
# start worker:
# celery -A Service.api.tasks worker
# """
#
#
# @app.task
# def add(x, y):
#     return x + y
#
#
# @app.task()
# def longtime_add(x, y):
#     print("longtime_add called with", x, y)
#     #time.sleep(6)
#     return x + y
#
#
# def get_status(task_id):
#     status = app.AsyncResult(task_id, app=app)
#     print("Invoking Method ")
#     return "Status of the Task " + str(status.state)
