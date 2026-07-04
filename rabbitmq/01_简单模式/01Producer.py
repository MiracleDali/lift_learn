import pika

# 1 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '127.0.0.1', credentials=pika.PlainCredentials('admin', 'admin')))
# 1 创建通道 channel
channel = connection.channel()


# 2 创建队列
channel.queue_declare(queue='hello', durable=True, arguments={'x-queue-type': 'quorum'})


# 3 向指定队列插入消息
channel.basic_publish(exchange='',              # 简单模式
                      routing_key='hello',      # 指定队列
                      body='Hello nihao!')      # 消息体
print(" [x] Sent 'Hello World!'")