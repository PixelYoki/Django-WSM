from django.contrib import admin
from .models import Product, Order
# Register your models here.

admin.site.site_header = '商品库存交易信息后台管理'
admin.site.title = '商品库存交易系统'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'price', 'created_time')
    list_per_page = 20
    list_filter = ('category', 'created_time')
    search_fields = ('name', 'category')
    date_hierarchy = 'created_time'
    ordering = ('-created_time',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'staff', 'order_quantity', 'created_time')
    list_per_page = 20
    list_filter = ('created_time',)
    search_fields = ('product', 'staff')
    date_hierarchy = 'created_time'
    ordering = ('-created_time',)

