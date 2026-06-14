# auth/schemas.py
from ninja import Schema
from typing import Optional, List, Any

################################################################################
# 注册请求体 Schema
class RegisterRequest(Schema):
    """
    用户注册请求的数据结构。
    
    字段说明：
    - username: 用户名（必填）
    - password: 密码（必填）
    - confirm_password: 确认密码（必填，用于二次验证）
    - email: 邮箱（可选，用于后续找回密码）
    """
    username: str
    password: str
    confirm_password: str
    email: Optional[str] = None  # Optional 表示可选，默认 None

# 注册响应体 Schema
# me 查看用户信息响应 Schema
class RegisterResponse(Schema):
    """
    用户注册成功后的响应数据结构。
    
    字段说明：
    - success: 是否成功
    - message: 提示信息
    - user_id: 新用户的 ID（成功时返回）
    - username: 新用户的用户名（成功时返回）
    """
    success: bool
    message: str
    user_id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    groups: Optional[List[str]] = None


class ErrorResponse(Schema):
    """
    错误响应的数据结构。
    
    字段说明：
    - success: 固定为 False
    - message: 错误详情
    """
    success: bool = False
    message: str

################################################################################
# 登录请求体
class LoginRequest(Schema):
    """
    用户登录请求的数据结构。
    """
    username: str
    password: str
# 登录响应 Schema
class LoginResponse(Schema):
    """
    用户登录成功后的响应数据结构。
    字段说明：
    - success: 是否成功
    - message: 提示信息
    - access_token: 访问令牌（成功时返回）
    - refresh_token: 刷新令牌（成功时返回）
    - user_id: 用户ID（成功时返回）
    - username: 用户名（成功时返回）
    - email: 用户邮箱（成功时返回）
    """
    success: bool
    message: str
    access_token: str = ""
    refresh_token: str = ""
    user_id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    groups: Optional[List[str]] = None

################################################################################
# 登出请求体
class LogoutRequest(Schema):
    """
    用户登出请求的数据结构。
    - success: 固定为 False
    - message: 详情
    """
    success: bool = False
    message: str

    
   