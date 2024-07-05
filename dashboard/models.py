from django.db import models
from django.contrib.auth.models import User


# Create your models here.
CATEGORY = (
    ('food', '食品'),
    ('clothes', '服装'),
    ('electronics', '电子产品'),
    ('books', '图书'),
    ('education', '教育'),
    ('social_service', '社会服务'),
    ('others', '其他'),
)

class Product(models.Model):
    name = models.CharField(verbose_name='产品名称', max_length=100, null=True)
    category = models.CharField(verbose_name='产品分类', max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(verbose_name='产品数量', null=True)
    price = models.FloatField(verbose_name='产品价格', null=True)
    description = models.TextField(verbose_name='产品描述', null=True)
    created_time = models.DateTimeField(verbose_name ='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, verbose_name = '产品名称', on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, verbose_name = '客户', on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(verbose_name = '订单数量', null=True)
    created_time = models.DateTimeField(verbose_name = '创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return f'{self.staff}于{self.created_time}购买了{self.product}-{self.order_quantity}个'