from django.urls import path
from . import views      # 从当前目录导入 views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),      # 空路径，即 "/polls/"
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]