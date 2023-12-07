from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
# from datetime import date
# Create your models here.
# models.py
from django.db import models



class SaveQueries(models.Model):
    question = models.CharField(null=False,max_length=2800) # jst limiting !!
    returnquery = models.CharField(null=False,max_length=35000)
    query_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.question + " " + self.returnquery


from django.contrib.auth.models import User
from django.db import models

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class SelectedItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    selected_item = models.CharField(max_length=100)

    def __str__(self):
        return self.selected_item

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # You should hash the password before storing it

class ProjectDetails(models.Model):
    user_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    project_scope = models.TextField()
    project_main_features = models.TextField()
    functional_requirements = models.TextField()
    business_requirements = models.TextField()
    non_functional_requirements = models.TextField()

    def __str__(self):
        return f"{self.user_name} - {self.timestamp}"