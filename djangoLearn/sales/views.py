from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def listorders(request):
    return HttpResponse("下面是系统中的订单消息。。。")

def listorders1(request):
    return HttpResponse("下面是系统中的订单消息。。。11")

def listorders2(request):
    return HttpResponse("下面是系统中的订单消息。。。22")

def listorders3(request):
    return HttpResponse("下面是系统中的订单消息。。。33")