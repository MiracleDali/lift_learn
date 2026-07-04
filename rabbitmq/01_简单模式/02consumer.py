import pika

# 1 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '127.0.0.1', credentials=pika.PlainCredentials('admin', 'admin')))
# 1 创建通道 channel
channel = connection.channel()


# 2 创建队列
channel.queue_declare(queue='hello', durable=True, arguments={'x-queue-type': 'quorum'})


# 3 定义回调函数
def callback(ch, method, properties, body):
    print(f" [x] Received {body}") 


# 4 确定监听队列
channel.basic_consume(queue='hello',
                      auto_ack=True,   # 默认应答
                      on_message_callback=callback)  # callback 回调函数名


print(' [*] Waiting for messages. To exit press CTRL+C')
 # 正式启动监听
channel.start_consuming()  