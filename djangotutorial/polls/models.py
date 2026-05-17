from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# 问题模型
class Question(models.Model):
    question_text = models.CharField(max_length=200)         # 问题的文本，字符字段
    pub_date = models.DateTimeField('date published')        # 布日期，日期时间字段

    def __str__(self):
        return self.question_text
    # 添加自定义方法：为 Question 添加 was_published_recently 方法，判断问题是否是最近一天发布的
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)        # 外键，关联问题  关联到 Question
    choice_text = models.CharField(max_length=200)      # 选项的文本，字符字段
    votes = models.IntegerField(default=0)          # 票数，整数字段，默认为0

    def __str__(self):
        return self.choice_text