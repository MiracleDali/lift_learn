
from celery.result import AsyncResult
from celery_task import cel

async_result = AsyncResult(id='95417128-41f0-44ff-aa95-f3cf31bbcc01', app=cel)

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