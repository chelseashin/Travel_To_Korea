from django.contrib import admin
from .models import MyUser

# Register your models here.
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'email', 'gender', 'birth', ]
admin.site.register(MyUser, MyUserAdmin)