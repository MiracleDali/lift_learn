from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.listorders, name='listorders'),
    path('orders1/', views.listorders1, name='listorders'),
    path('orders2/', views.listorders2, name='listorders'),
    path('orders3/', views.listorders3, name='listorders'),
]
