import grpc
import test_pb2
import test_pb2_grpc
from loguru import logger
import sys
import time

logger.remove()
logger.add(sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> [<level>{level}</level>] <cyan>{process.id}</cyan> <cyan>{thread.id}</cyan> [<magenta>{file}</magenta>] [<yellow>{line}</yellow>]: <level>{message}</level>",
    level="DEBUG",
    # colorize=True,      # 显式启用颜色
    # enqueue=False       # 控制台建议关闭异步，以确保颜色正常显示
)

def connect():
    # 与 gRPC 服务器建立连接
    channel = grpc.insecure_channel('localhost:50051')
    # 创建存根（Stub）客户端代理
    stub = test_pb2_grpc.TestLearnStub(channel)
    return stub

def run1():
    stub = connect()
    logger.info('######## 1.一元RPC ########')
    num = int(input('请输入1-10的数字开始和刘亦菲比大小：'))
    request = test_pb2.test1_request(id = num)
    response = stub.Test1(request)
    logger.info(response)

def run2():
    stub = connect()
    logger.info('######## 2.服务端流式RPC ########')
    num = int(input('输入出场明星的数量1-5之间：'))
    request = test_pb2.server_request(id = num)
    for response in stub.server_stream(request):
        logger.info(response)

def run3():
    stub = connect()
    logger.info('######## 3.客户端流式RPC ########')
    num1 = int(input('输入第一次发送的数字：'))
    num2 = int(input('输入第二次发送的数字：'))
    num3 = int(input('输入第三次发送的数字：'))
    number = [num1, num2, num3]
    def request_data():
        for i in number:
            yield test_pb2.client_request(id = i)
    response = stub.client_stream(request_data())
    logger.info(response.reply)

def run4():
    stub = connect()
    logger.info('######## 4.双向流式RPC ########')
    def request_generator():
        for i in range(5):
            print(f"发送: {i}")
            yield test_pb2.bidirectional_request(id=i)
    responses = stub.bidirectional_stream(request_generator())
    for response in responses:
        logger.info(f"接收: {response.reply}")

    


if __name__ == '__main__':
    number = input('请输入运行程序序号：')
    dicts = {
        '1': run1,
        '2': run2,
        '3': run3,
        '4': run4
    }
    dicts[number]()