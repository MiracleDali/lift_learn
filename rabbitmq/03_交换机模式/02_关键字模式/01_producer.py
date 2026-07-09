import pika

# 1 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '127.0.0.1', credentials=pika.PlainCredentials('admin', 'admin')))
# 1 创建通道 channel
channel = connection.channel()


# 2 创建 名为logs的交换机  durable=True, 代表持久化
channel.exchange_declare(exchange='logs',           # 定义交换机的名字
                         exchange_type='direct',    # 定义：direct 模式, 关键字匹配
                         durable=True               # 持久化
                         )


# 3 向交换机插入数据
message = {
            'error': "error_hello world", 
            'info': "info_hello world", 
            'warning': "waring_hello world"
           }   

for key, value in message.items():
    channel.basic_publish(exchange='logs',      # 创建交换机
                          routing_key=key,      # 创建路由键
                          body=value,           # 创建消息体
                          # 创建消息持久化
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # 2 持久化
                          )
                          )

print(f" [x] Sent {message}")
connection.close()