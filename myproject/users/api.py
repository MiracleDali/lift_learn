# users/api.py
from ninja import Router
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from loguru import logger
from .schemas import RegisterRequest, RegisterResponse, ErrorResponse, LoginResponse, LoginRequest

# 创建一个 Router 实例，用于注册接口
router = Router()


@router.post(
    "/register",
    response={
        200: RegisterResponse,   # 成功时返回 200 状态码和 RegisterResponse
        400: ErrorResponse       # 失败时返回 400 状态码和 ErrorResponse
    }, 
    auth=None
)
def register(request, payload: RegisterRequest):
    """
    用户注册接口。
    
    参数：
    - request: Django 的请求对象（自动注入）
    - payload: 请求体数据，自动解析为 RegisterRequest 对象
    
    返回：
    - 成功：200 状态码，包含用户信息
    - 失败：400 状态码，包含错误信息
    """
    
    # 1. 校验两次密码是否一致
    if payload.password != payload.confirm_password:
        logger.warning(f"注册失败：密码不一致，用户名: {payload.username}")
        return 400, {"success": False, "message": "两次输入的密码不一致"}
    
    # 2. 校验用户名是否已存在
    if User.objects.filter(username=payload.username).exists():
        logger.warning(f"注册失败：用户名已存在，用户名: {payload.username}")
        return 400, {"success": False, "message": "该用户名已被注册"}
    
    # 3. 校验邮箱是否已被使用（可选）
    if payload.email and User.objects.filter(email=payload.email).exists():
        logger.warning(f"注册失败：邮箱已被使用，邮箱: {payload.email}")
        return 400, {"success": False, "message": "该邮箱已被注册"}
    
    # 4. 校验密码复杂度（使用 Django 内置规则）
    # try:
    #     validate_password(payload.password)
    # except ValidationError as e:
    #     # e.messages 是一个列表，包含所有密码不符合规则的原因
    #     error_msg = "; ".join(e.messages)
    #     logger.warning(f"注册失败：密码复杂度不足，用户名: {payload.username}，原因: {error_msg}")
    #     return 400, {"success": False, "message": f"密码不符合要求：{error_msg}"}
    
    # 5. 创建用户（核心步骤）
    try:
        user = User.objects.create_user(
            username=payload.username,
            password=payload.password,
            email=payload.email or ""  # 如果 email 为 None，设为空字符串
        )
        
        # 记录成功日志
        logger.info(f"用户注册成功：用户名={user.username}，ID={user.id}")
        
        # 返回成功响应
        return 200, {
            "success": True,
            "message": "注册成功",
            "user_id": user.id,
            "username": user.username,
            "email": user.email
        }
    
    except Exception as e:
        # 捕获未知异常
        logger.error(f"用户注册异常，用户名: {payload.username}，错误: {str(e)}")
        return 400, {"success": False, "message": f"注册失败：{str(e)}"}


from ninja_jwt.tokens import RefreshToken
@router.post("/login", response={200: LoginResponse, 400: ErrorResponse}, auth=None)
def login(request, payload: LoginRequest):
    """
    用户登录接口。
    
    参数：
    - request: Django 的请求对象
    - payload: 登录请求数据（用户名、密码）
    
    返回：
    - 成功：200状态码，包含 token 和用户信息
    - 失败：400状态码，包含错误信息
    """
    # 1. 使用 Django 内置认证函数验证用户
    user = authenticate(
        username=payload.username, 
        password=payload.password
    )
    # 2. 验证失败处理
    if not user:
        logger.warning(f"登录失败：用户名或密码错误，用户名: {payload.username}")
        return 400, {
            "success": False,
            "message": "用户名或密码错误"
        }
    # 3. 验证成功，生成 JWT Token
    refresh = RefreshToken.for_user(user)
    # 4. 记录登录日志
    logger.info(f"用户登录成功：用户名={user.username}，ID={user.id}")
    # 5. 返回成功响应
    return 200, {
        "success": True,
        "message": "登录成功",
        "access_token": str(refresh.access_token),
        "refresh_token": str(refresh),
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
        "groups": [group.name for group in user.groups.all()]
    }


@router.get("/me", response=RegisterResponse)
def me(request):
    """
    获取当前登录用户的信息。
    """
    logger.info(f"用户:{request.user.username}，ID={request.user.id} 获取用户信息")
    user = User.objects.get(username=request.user.username)
    logger.info(f"用户信息: {user.username}，ID={user.id}，邮箱={user.email}")
    groups = [group.name for group in user.groups.all()]
    logger.info(f"用户组: {groups}")

    return 200, {
        "success": True,
        "message": "用户信息获取成功",
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
        "groups": groups
    }