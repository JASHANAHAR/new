from django.db import models

class UserData(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, default="default@example.com")
    password = models.CharField(max_length=50)

def __str__(self):
        return self.user_name

# class home(models.Model):
#     home_name = models.CharField(max_length=50) 
#     home_mail = models.EmailField(max_length=254, default="default@example.com") 

# class user(models.Model):
#     home_name = models.CharField(max_length=50) 
#     home_mail = models.EmailField(max_length=254, default="default@example.com") 



# Create your models here.
