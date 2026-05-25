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
from ninja import NinjaAPI
from api.api import router as api_router
from ninja_jwt.routers.obtain import obtain_pair_router # 导入自带的路由器


api = NinjaAPI()
api.add_router("/", api_router)             # 业务接口
api.add_router("/auth", obtain_pair_router) # 登录/刷新接口

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
