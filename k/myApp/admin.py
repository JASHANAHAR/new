from django.contrib import admin
from .models import UserData

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_name', 'email', 'gender', 'country', 'password', 'image')
    list_filter = ('country',)
    search_fields = ('name', 'user_name', 'email', 'country')

admin.site.register(UserData, UserDataAdmin)
