from django.urls import path
from . import views      # 从当前目录导入 views

urlpatterns = [
    path("", views.index, name="index")      # 空路径，即 "/polls/"
]