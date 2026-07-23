from celery_tasks.task01 import send_email
from celery_tasks.task02 import send_msg
from datetime import datetime, UTC


# 定时任务
v1 = datetime(2026, 7, 23, 22, 45, 00)
print(v1)
v2 = datetime.fromtimestamp(v1.timestamp(), UTC)
print(v2)
print(v2.tzinfo)
result = send_email.apply_async(args=['小王'], eta=v2)
print(result.id)