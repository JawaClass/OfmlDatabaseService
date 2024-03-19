# import time
#
# from celery.result import AsyncResult
#
# from Service.api.tasks import longtime_add, get_status
#
#
# #r = celery.send_task('tasks.longtime_add', kwargs={'x': 1, 'y': 2})
# r: AsyncResult = longtime_add.delay(55, 20)
#
# print(r.id)
# while True:
#     status = get_status(r.id)
#     print(status)
#     # if status != "PENDING":
#     #     break
#     time.sleep(1)
# # # r = simple_app.send_task('tasks.longtime_add', kwargs={'x': 1, 'y': 2})
# # print("1")
# # result = longtime_add.delay(23, 42)
# # print("2")
# # result.wait()  # 65
# # print("3")
# # # print(result)
#
from celery import shared_task


@shared_task(ignore_result=False)
def add_together(a: int, b: int) -> int:
    return a + b


@shared_task()
def say_hello():
    # return "hello"
    return {
        "resultValue": "hello..."
    }