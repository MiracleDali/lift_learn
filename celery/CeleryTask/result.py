"""
celery任务结果查询
"""

from celery.result import AsyncResult
from celery_task import cel

async_result = AsyncResult(id="07a2c2d2-6713-4cfc-a92e-847d0de775f0", app=cel)

if async_result.successful():
    result = async_result.get()
    print(result)
    # result.forget()    # 删除结果
elif async_result.failed():
    print('执行失败')
elif async_result.status == 'PENDING':
    print('任务等待执行')
elif async_result.status == 'RETRY':
    print('任务异常，正在重试')
elif async_result.status == 'STARTED':
    print('任务开始执行')    
elif async_result.status == 'REVOKED':
    print('任务被撤销')

