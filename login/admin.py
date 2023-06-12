from django.contrib import admin

# Register your models here.
from login.models import *


class User_admin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'password')
admin.site.register(User, User_admin)