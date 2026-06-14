"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja_extra import NinjaExtraAPI       # 基于类的方式
# from ninja import NinjaAPI          # 基于函数的方式
from ninja_jwt.controller import NinjaJWTDefaultController
from api.api import router as api_router
from users.api import router as auth_router
from ninja_jwt.authentication import JWTAuth

api = NinjaExtraAPI(
    docs_url="/docs",
    title="My Project API",
    description="Test Api for My Project frontend - documentation",
    version="1.0.0",
    auth=JWTAuth(),
)   # 基于类的方式
api.register_controllers(NinjaJWTDefaultController)
api.add_router('api', api_router)           # 业务路由（无前缀）
api.add_router('auth', auth_router)          # 认证路由（有前缀）

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.urls),  # 业务接口 
]