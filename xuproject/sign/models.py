from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100) #发布会标题
    limit = models.IntegerField() #参加人数
    status = models.BooleanField() #状态
    address = models.CharField(max_length=200) #地址
    start_time = models.DateTimeField('events time')  #发布会时间
    creat_time = models.DateTimeField(auto_now=True)  #创建时间（自动获取当前时间）

    def __str__(self):
        return self.name

class UserInfo(models.Model):
    user = models.CharField(max_length=20)
    pwd  = models.CharField(max_length=20)

    def __str__(self):
        return self.user
