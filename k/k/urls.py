"""
URL configuration for k project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myApp/',include('myApp.urls')),
    path('api/', include('myApp.urls')),
    path('',views.homePage, name='home'),
    path('view/',views.view, name='view'),
    path('registation', views.registation, name='registation'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('login',views.login, name='login'),
    path('finaldata',views.finaldata, name='finaldata'),
    path('get_countries',views.get_countries, name='get_countries'),    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)