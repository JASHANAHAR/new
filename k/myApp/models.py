from django.db import models
from django_countries.fields import CountryField

class UserData(models.Model):
    GENDER_CHOICE = [
        ("male", "Male"),
        ("female", "Female"),
    ]
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password_strength = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

# class home(models.Model):
#     home_name = models.CharField(max_length=50) 
#     home_mail = models.EmailField(max_length=254, default="default@example.com") 

# class user(models.Model):
#     home_name = models.CharField(max_length=50) 
#     home_mail = models.EmailField(max_length=254, default="default@example.com") 

# Create your models here.
