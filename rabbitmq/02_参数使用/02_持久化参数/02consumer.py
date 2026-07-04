import pika

# 1 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '127.0.0.1', credentials=pika.PlainCredentials('admin', 'admin')))
# 1 创建通道 channel
channel = connection.channel()


# 2 创建队列
channel.queue_declare(queue='hello2', durable=True, arguments={'x-queue-type': 'quorum'})


# 3 定义回调函数
def callback(ch, method, properties, body):
    print(f" [x] Received -- {body}") 

    # 确认手动应答，确认消息已被消费
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 4 确定监听队列
channel.basic_consume(queue='hello2',
                      # 吧默认应答改为手动应答
                      auto_ack=False,    # 手动应答
                      on_message_callback=callback)  # callback 回调函数名


print(' [*] Waiting for messages. To exit press CTRL+C')
 # 正式启动监听
channel.start_consuming()  