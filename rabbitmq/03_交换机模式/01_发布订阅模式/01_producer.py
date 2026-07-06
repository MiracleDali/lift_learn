import pika

# 1 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '127.0.0.1', credentials=pika.PlainCredentials('admin', 'admin')))
# 1 创建通道 channel
channel = connection.channel()


# 2 创建 名为logs的交换机  durable=True, 代表持久化
channel.exchange_declare(exchange='logs',           # 定义交换机的名字
                         exchange_type='fanout',    # 定义：fanout模式，将消息广播给所有队列
                         durable=True               # 持久化
                         )


# 3 向交换机插入数据
message = "info: hello world"
channel.basic_publish(exchange='logs',     # 指定交换机
                      routing_key='',      # 这是队列这里不用
                      body=message,        # 消息体
                      # 消息持久化
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # 2 表示持久化
                      ),
                      ) 

print(f" [x] Sent {message}")
connection.close()