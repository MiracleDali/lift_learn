from django.db import models

# Create your models here.
class Customer(models.Model):
    # 客户表
    name = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    # null=True 允许为空
    email = models.EmailField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)


class TestModel(models.Model):
    # 定义外键字段关联客户表
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # 测试表
    ORDER_STATUS_CHOICES = (
        (1, '状态1'),
        (2, '状态2'),
        (3, '状态3'),
        (4, '状态4'),
        (5, '状态5'),
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=ORDER_STATUS_CHOICES)
    class Meta(object):
        db_table = 'test_model'
        verbose_name = '状态测试表'
        verbose_name_plural = verbose_name