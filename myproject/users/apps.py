from django.apps import AppConfig

class AuthConfig(AppConfig):
    """
    用户认证模块的 App 配置类。
    
    - `default_auto_field`: 指定默认主键类型，Django 3.2+ 要求显式声明
    - `name`: app 的唯一标识符，必须与文件夹同名
    - `verbose_name`: 后台显示的友好名称（可选）
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = '用户认证管理'