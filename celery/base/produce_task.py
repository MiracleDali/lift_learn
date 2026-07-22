
from celery_task import send_emali, send_meg

result = send_emali.delay("zhangsan")
print('1', result.id)

result2 = send_meg.delay("lisi")
print('2', result2.id)
