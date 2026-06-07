"""
日志用户名上下文注入中间件。

作用：
- 每个请求开始时，从 request 中获取当前登录用户名
- 使用 Loguru 原生的 `contextualize` 绑定到日志上下文
- 当前请求处理过程中，所有日志都会自动带上用户名
- 请求结束自动清理上下文，线程安全

支持两种认证方式：
1. Django session 认证：直接从 request.user 拿
2. JWT 认证（ninja_jwt）：从 Authorization header 解析 token 获取用户

默认先用第一种，拿不到再尝试第二种。
"""

from loguru import logger
from django.contrib.auth import get_user_model

# 获取用户模型（支持自定义用户模型）
User = get_user_model()


class LogUserContextMiddleware:
    """
    日志用户上下文中间件。

    工作流程：
    1. 请求进来，尝试获取当前用户名
    2. 使用 `with logger.contextualize()` 绑定用户名到上下文
    3. 调用后续处理链，整个处理过程中所有日志自动带用户名
    4. 处理完成退出 with 块，自动清理上下文
    """

    def __init__(self, get_response):
        """
        中间件初始化，Django 启动时调用一次。

        参数：
            get_response: 下一个中间件或视图的可调用对象
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        每个请求都会调用。

        流程：
        1. 获取用户名（优先 request.user，不行再试 JWT header）
        2. 绑定到 Loguru 上下文，处理请求
        3. 返回响应
        """
        # 默认用户名：匿名用户
        username = "anonymous"

        # ------------- 尝试从 request.user 获取（session 认证）-------------
        if hasattr(request, "user") and request.user.is_authenticated:
            username = request.user.username

        # ------------- 尝试从 JWT Authorization header 获取（ninja_jwt）-------------
        # 如果上面没拿到已认证用户，才走这里
        else:
            # 取出 Authorization header
            auth_header = request.META.get("HTTP_AUTHORIZATION", "")
            # 格式必须是 Bearer <token>
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]
                try:
                    # 用 ninja_jwt 解析 token，获取用户 ID，查库拿到用户
                    from ninja_jwt.tokens import AccessToken
                    from ninja_jwt.settings import api_settings

                    access_token = AccessToken(token)
                    user_id = access_token[api_settings.USER_ID_CLAIM]
                    user = User.objects.get(id=user_id)
                    username = user.username
                except Exception:
                    # token 无效或用户不存在，保持 anonymous
                    pass

        # ------------- 绑定用户名到上下文，处理请求 -------------
        # 使用 Loguru 原生 contextualize，自动线程隔离
        # with 块退出自动清理，不会影响下一个请求
        with logger.contextualize(username=username):
            # 调用后续处理链
            response = self.get_response(request)

        # 返回响应
        return response

    def process_exception(self, request, exception):
        """
        处理未捕获的异常。

        Django 遇到未捕获的异常会调用这个方法。
        我们在这里记录日志，异常信息已经自动带上用户名了。

        参数：
            request: 当前请求对象
            exception: 异常对象

        返回：
            None，继续让 Django 处理
        """
        # 记录错误日志，带上异常栈
        logger.opt(exception=True).error(f"Unhandled exception: {type(exception).__name__}")
        return None