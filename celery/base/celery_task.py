import celery
import time

backend = 'redis://localhost:6379/1'     # 保存任务结果，可以是其他的数据库
broker = 'redis://localhost:6379/2'      # 消息中间件，rabbitmq 更好 

cel = celery.Celery(
    'celery_task',        # 任务名称
    broker=broker,        # 消息中间件地址
    backend=backend,      # 保存任务结果的数据库地址
    include=['celery_task']       # 包含的任务模块
)

@cel.task(name='celery_task.send_emali')
def send_emali(name):
    print(f"向{name}发送邮件")
    time.sleep(5)
    print(f"向{name}发送邮件成功")
    return "ok"

@cel.task(name='celery_task.send_meg')
def send_meg(name):
    print(f"向{name}发送短信")
    time.sleep(5)
    print(f"向{name}发送短信成功")
    return "ok"