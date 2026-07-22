
from celery.result import AsyncResult
from celery_tasks.celery_app import cel

async_result = AsyncResult(id='aa91e285-6bf0-4bc6-87df-60de31bfa838', app=cel)

if async_result.successful():
    result = async_result.get()
    print(result)
elif async_result.failed():
    print('执行失败')
elif async_result.status == 'PENDING':
    print('任务等待中被执行')
elif async_result.status == 'RETRY':
    print('任务异常被重新执行')
elif async_result.status == 'STARTED':
    print('任务开始执行')
elif async_result.status == 'REVOKED':
    print('任务被撤销')