"""
Loguru 集成配置模块。

本模块作用：
1. 拦截 Python 标准 logging 的所有输出（包括 Django 内部、uvicorn、第三方库）
2. 统一转发给 Loguru，实现：
   - 控制台彩色输出（开发环境）
   - 文件滚动存储（生产环境）
   - 自动轮转压缩
3. 日志格式预留 username 位置，由中间件自动注入当前请求用户

加载时机：
- 在 settings.py 最顶部被 import
- 确保 Django 初始化之前 Loguru 已经接管所有日志输出
"""

import logging
import sys
from pathlib import Path
from loguru import logger


class InterceptHandler(logging.Handler):
    """
    自定义日志拦截处理器。

    作用：将 Python 标准 logging 模块的输出转发给 Loguru。
    这是官方推荐的稳定方案，不依赖 Loguru 私有API，兼容性好。
    """

    def emit(self, record):
        """
        处理一条日志记录。

        参数：
            record: logging 原生的日志记录对象

        过程：
            1. 获取日志级别
            2. 找到真正的调用栈帧（保证文件名和行号正确）
            3. 转发给 Loguru 输出，并绑定默认用户名 "system"
        """
        # 根据级别名称获取 Loguru 对应的级别
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            # 如果找不到，直接用数字级别
            level = record.levelno

        # 向上找调用栈，跳过 logging 自身的帧
        # 目的是让 Loguru 正确计算深度，保证文件名和行号显示正确
        frame, depth = logging.currentframe(), 2
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        # 转发给 Loguru，原生 logging 日志默认用 system 用户名
        logger.opt(depth=depth, exception=record.exc_info).bind(username="system").log(
            level, record.getMessage()
        )


def setup_loguru():
    """
    初始化 Loguru 全局配置。

    做了这些事：
    1. 移除 Loguru 默认的 handler（避免重复输出）
    2. 配置控制台输出（始终开启，DEBUG级别，彩色）
    3. 配置文件输出（仅生产环境开启，按天轮转，保留30天，zip压缩）
    4. 拦截 Python 标准 logging 的所有日志器，全部转 Loguru
    """
    # 移除默认 handler，我们要重新配置
    logger.remove()

    # ============= 定义日志格式 =============
    # 格式顺序：时间 | 级别 | 用户名 | 文件:函数:行号 | 消息
    # - 用户名固定占 12 个字符宽度，保证对齐
    # - 使用 ANSI 颜色标记，控制台会自动着色
    LOG_FORMAT = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "  # 绿色时间，精确到毫秒
        "<level>{level: <8}</level> | "                      # 级别（根据级别自动着色），占8字符
        "<yellow>{extra[username]: <12}</yellow> | "        # 黄色用户名，占12字符
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "  # 青色文件函数行号
        "<level>{message}</level>"                           # 消息（级别颜色）
    )

    # ============= 控制台输出配置 =============
    # 开发环境始终输出到控制台，级别 DEBUG
    logger.add(
        sys.stderr,                # 输出到标准错误流（符合 convention）
        format=LOG_FORMAT,         # 使用上面定义的格式
        level="DEBUG",             # 最低日志级别
        colorize=True,             # 启用彩色输出
        enqueue=True,              # 异步写入队列，线程安全，不阻塞主线程
        backtrace=True,            # 捕获完整异常栈
        diagnose=True,             # 启用变量诊断，方便调试
    )

    # ============= 文件输出配置（仅生产环境）==============
    # 读取 Django 设置，开发环境不写文件，只在生产环境写入
    from django.conf import settings
    if not settings.DEBUG:
        # 创建 logs 目录（如果不存在）
        log_dir = Path(settings.BASE_DIR) / "logs"
        log_dir.mkdir(exist_ok=True)

        # 文件不需要颜色，去掉所有 ANSI 颜色标记
        file_format = LOG_FORMAT.replace("<green>", "").replace("</green>", "") \
                                 .replace("<level>", "").replace("</level>", "") \
                                 .replace("<yellow>", "").replace("</yellow>", "") \
                                 .replace("<cyan>", "").replace("</cyan>", "")

        logger.add(
            log_dir / "django_{time:YYYY-MM-DD}.log",  # 文件名按日期命名
            format=file_format,          # 无颜色的纯文本格式
            rotation="00:00",            # 轮转时机：每天零点创建新文件
            retention="30 days",         # 保留时间：30天，自动删除旧文件
            compression="zip",           # 轮转后自动压缩旧文件为 zip，节省空间
            level="INFO",                # 文件只记录 INFO 及以上级别，避免太大
            encoding="utf-8",            # 编码 UTF-8，支持中文
            enqueue=True,                # 异步写入，线程安全
            backtrace=True,              # 异常栈完整
        )

    # ============= 拦截所有原生 logging =============
    # 1. 配置根日志器使用我们的拦截处理器
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

    # 2. 遍历所有已经注册的日志器，全部换成拦截处理器
    # 确保 Django、uvicorn 等内部日志也能被拦截
    for logger_name in list(logging.root.manager.loggerDict.keys()):
        logging.getLogger(logger_name).handlers = [InterceptHandler()]
        logging.getLogger(logger_name).propagate = False  # 禁止向上传播，避免重复

    # 返回配置好的 logger，供其他模块导入
    return logger


# 导出 logger，方便其他模块直接从这里导入使用
__all__ = ["logger", "setup_loguru"]