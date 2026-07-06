import pika

# 1 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '127.0.0.1', credentials=pika.PlainCredentials('admin', 'admin')))
# 1 创建通道 channel
channel = connection.channel()


# 2 创建队列 持久化队列  durable=True, 代表持久化
channel.queue_declare(queue='hand_out', durable=True, arguments={'x-queue-type': 'quorum'})


# 3 向指定队列插入消息
channel.basic_publish(exchange='',               # 简单模式
                      routing_key='hand_out',      # 指定队列
                      body='info_hello 2',            # 消息体
                      # 消息持久化
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # 2 表示持久化
                      ),
                      )     


print(" [x] Sent 'success'")