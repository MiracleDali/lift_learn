
from celery_task import send_email, send_message


result = send_email.delay('张三')
print(result.id)

result = send_message.delay('张三')
print(result.id)