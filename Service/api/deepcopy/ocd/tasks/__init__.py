from celery import shared_task

from Service.api.deepcopy.ocd.tasks.tasks import merge_article_with_deepcopy,merge_article_with_deepcopy_as


@shared_task(ignore_result=False, name="merge article")
def celery_task_merge_article_with_deepcopy(*, article: str, program: str, merge_with: str):
    return merge_article_with_deepcopy(article=article, program=program, merge_with=merge_with)


@shared_task(ignore_result=False, name="merge article as")
def celery_task_merge_article_with_deepcopy_as(*, article: str, program: str, merge_as: str, merge_with: str):
    return merge_article_with_deepcopy_as(article, program, merge_as, merge_with)
