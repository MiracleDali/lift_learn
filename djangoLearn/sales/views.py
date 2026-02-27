# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# 导入 CUstomer 模型类
from common.models import Customer



def listcustomers(request):
    qs = Customer.objects.values()

    # 检查 url 中是否有参数
    ad = request.GET.get('address', None)
    if ad:
        qs = qs.filter(address=ad)

    resultStr = ""
    for quseyser in qs:
        for key, value in quseyser.items():
            resultStr += f'{key}: {value} | '
        # 换行
        resultStr += '<br>'
    return HttpResponse(resultStr)



def listorders(request):
    return HttpResponse("下面是系统中的订单消息。。。")
