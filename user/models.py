from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    staff =models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField("地址",max_length=200,null=True)
    phone=models.CharField("电话",max_length=50,null=True)
    image =models.ImageField(default='avatar.png',upload_to='Profile_Images')

    class Meta:
        verbose_name = '客户详细信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        # 关系 表字段调用
        return self.staff.username