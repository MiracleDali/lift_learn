import grpc
from concurrent import futures
import time
import random
import sys
from loguru import logger
from typing import List, Tuple, Iterator
import test_pb2_grpc
import test_pb2

logger.remove()
logger.add(sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> [<level>{level}</level>] <cyan>{process.id}</cyan> <cyan>{thread.id}</cyan> [<magenta>{file}</magenta>] [<yellow>{line}</yellow>]: <level>{message}</level>",
    level="DEBUG",
    # colorize=True,      # 显式启用颜色
    # enqueue=False       # 控制台建议关闭异步，以确保颜色正常显示
)

class TestLearnServicer(test_pb2_grpc.TestLearnServicer):
    # 简单 rpc
    def Test1(self, request, context):
        print()
        logger.info(f"客户端发送数据{request.id}")
        args = request.id
        random_number = random.randint(1, 10)
        if args > random_number:
            request_args = ">"
            result = "亦菲说你真棒"
        elif args < random_number:
            request_args = "<"
            result = "亦菲说再接再厉"
        else:
            request_args = "=="
            result = "亦菲说呀旗鼓相当"
        return test_pb2.test1_response(reply=f"{args} {request_args} {random_number} {result}")
    
    # 服务端流式 rpc
    def server_stream(self, request, context):
        print()
        logger.info(f"客户端发送数据{request.id}")
        args = request.id
        stars = ['章若楠', '古力娜扎', '迪丽热巴', '马尔扎哈', '安妮海瑟薇']
        for i in range(args):
            time.sleep(0.5)
            star = stars[i]
            yield test_pb2.server_response(reply=f"{star} 闪亮出场")

    # 客户端流式 rpc
    def client_stream(self, request_iterator, context):
        print()
        logger.info("开始接收客户端数据...")
        args = []
        for request in request_iterator:
            logger.info(f"接收数据{request.id}")
            args.append(request.id)
        logger.info(f"接收完毕，接收数据为{args}")
        return test_pb2.client_response(reply = f"你输入了 {str(args)}")
    
    # 双向流式 rpc
    def bidirectional_stream(self, request_iterator, context):
        print()
        logger.info("开始接收客户端数据...")
        lists = ['nace', 'good', 'pretty', 'beautiful', 'handsome']
        for request in request_iterator:
            time.sleep(0.5)
            logger.info(f"接收数据{request.id}")
            args = request.id
            if 0 <= args < len(lists):
                reply = lists[args]
            else:
                reply = "unknown"
            yield test_pb2.bidirectional_response(reply=f"{args} {reply}")

def serve():
    # 创建一个gRPC服务器, 设置线程最多10个并发
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 注册服务
    test_pb2_grpc.add_TestLearnServicer_to_server(TestLearnServicer(), server)
    # 监听端口
    server.add_insecure_port('[::]:50051')
    # 启动服务
    server.start()
    logger.info("gRPC服务启动成功, 监听端口 50051...")
    # 阻塞主线程，直到按 Ctrl+C 退出
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
