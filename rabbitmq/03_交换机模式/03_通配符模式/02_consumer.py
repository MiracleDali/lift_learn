import pika

# 1 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '127.0.0.1', credentials=pika.PlainCredentials('admin', 'admin')))
# 1 创建通道 channel
channel = connection.channel()


# 2 创建 名为logs的交换机  durable=True, 代表持久化 
# 这样不管是生产者还是消费者先启动都会创建交换机
channel.exchange_declare(exchange='logs1',           # 定义交换机的名字
                         exchange_type='topic',    # 定义：topic 模式, 通配符模式
                         durable=True,
                         )


# 3 创建队列
result = channel.queue_declare("",              # 队列名随机，每次启动都会创建一个队列
                               exclusive=True,  # 队列只对当前连接有效，连接断开自动删除
                               # durable=True     # 队列持久化 和 exclusive=True 不能同时使用
                               )
queue_name = result.method.queue          # 获取队列名字
print("queue_name:", queue_name)


# 4 绑定队列到交换机
# routing = ["usa.#", "#.news", "#.weather"]
channel.queue_bind(exchange='logs1', 
                    queue=queue_name,
                    routing_key = "#.weather",     # 绑定路由键
                    )

print(' [*] Waiting for logs. To exit press CTRL+C')

# 5 定义回调函数
def callback(ch, method, properties, body):
    print(f" [x] Received -- {body}") 

    # 确认手动应答，确认消息已被消费
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 6 确定监听队列
channel.basic_consume(queue=queue_name,
                      # 吧默认应答改为手动应答
                      auto_ack=False,    # 手动应答
                      on_message_callback=callback)  # callback 回调函数名

 # 正式启动监听
channel.start_consuming()  