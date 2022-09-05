from django.contrib import admin
from usuarios.models import User_profile

@admin.register(User_profile)
class User_profile_Admin(admin.ModelAdmin):
    list_display = ['user','phone','address','image']