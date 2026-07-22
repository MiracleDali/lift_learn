import time
from celery_tasks.celery_app import cel


@cel.task
def send_msg(name):
    print(f"向{name}发送短信")
    time.sleep(5)
    return f"向{name}发送短信成功"