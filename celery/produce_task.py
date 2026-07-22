from celery_tasks.task01 import send_email
from celery_tasks.task02 import send_msg

print('开始')

res = send_email.delay("小王")
print(res)

res2 = send_msg.delay("小李")
print(res2)