from django.db import models

# Create your models here.
# 问题模型
class Question(models.Model):
    question_text = models.CharField(max_length=200)         # 问题的文本，字符字段
    pub_date = models.DateTimeField('date published')        # 布日期，日期时间字段
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)        # 外键，关联问题  关联到 Question
    choice_text = models.CharField(max_length=200)      # 选项的文本，字符字段
    votes = models.IntegerField(default=0)          # 票数，整数字段，默认为0