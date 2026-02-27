from django.db import models

# Create your models here.
class Customer(models.Model):
    # 客户表
    name = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    # null=True 允许为空
    email = models.EmailField(max_length=200, null=True)