from django.urls import path
from . import views

app_name = 'xhatapp'
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.query,name="xhatgpt"), # can use name for link refering, 'xhatgpt:xhatgpt'
    path('About',views.about,name="aboutx"), # 'xhatgpt:aboutx'   
]

# take logo frm https://arcane.com/en-gb/
