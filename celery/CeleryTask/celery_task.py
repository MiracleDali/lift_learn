import celery
import time

"""
pip install redis   install redis
redis会细分为0-15，16个库
"""
# 1库存任务结果 task result store
backend = 'redis://127.0.0.1:6379/1'
# 2库为消息中间件 message broker
broker = 'redis://127.0.0.1:6379/2'


"""
创建celery实例
'test': 为app名称——可以自定义-随便起
'backend': 为结果存储库
'broker': 为消息中间件-可以随便换
"""
cel = celery.Celery('test',backend=backend, broker=broker)

# 使用上面实例对象的装饰器创建任务
@cel.task
def send_message(name):
    print(f'向{name}发送消息...')
    time.sleep(5)
    print(f'向{name}发送消息成功')
    return 'ok'

@cel.task
def send_email(name):
    kl
    print(f'向{name}发送邮件...')
    time.sleep(5)
    print(f'向{name}发送邮件成功')
    return 'ok'