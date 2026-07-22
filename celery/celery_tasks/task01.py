import time
from celery_tasks.celery_app import cel


@cel.task
def send_email(res):
    print(f"向{res}发送邮件")
    time.sleep(5)
    return f"完成向{res}发送邮件"