from django.db import models
from django.contrib.auth.models import User
'''因为要用到它，所以要先导入'''
class UserInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)   
    #和自带的User表一对一关联
    role=models.CharField(max_length=32)  #可以加扩展信息字段，比如年龄，性别，角色
# Create your models here.
