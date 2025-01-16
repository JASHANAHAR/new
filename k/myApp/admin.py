from django.contrib import admin
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import UserData

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_name', 'email', 'gender', 'country', 'password', 'image')
    

admin.site.register(UserData, UserDataAdmin)