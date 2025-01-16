"""
URL configuration for k project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')dd
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myApp import views
from . import views



urlpatterns = [
    # path('',views.homePage, name='home'),
    # path('view/',views.view, name='view'),
    # path('edit_submit',views.edit_submit, name="edit_submit"),
    path('registation', views.registation, name='registation'),
    # path('delete/<int:id>/',views.delete, name='delete'),
    # path('edit/<int:id>/',views.edit, name='edit'),
    # path('login',views.login, name='login'),
    
    
]

