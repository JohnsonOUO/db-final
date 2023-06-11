from django.contrib import admin

# Register your models here.
from home.models import *

class Favorite_Admin(admin.ModelAdmin):
    list_display = ('stock_id', 'user_id')
admin.site.register(Favorite, Favorite_Admin)

class stock_info_Admin(admin.ModelAdmin):
    list_display = ('stock_id', 'stock_name', 'industry', 'address', 'telephone')
admin.site.register(stock_info, stock_info_Admin)