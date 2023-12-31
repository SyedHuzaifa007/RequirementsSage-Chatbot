"""ChatGppt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from xhatapp import views
from django.contrib.auth import views as auth_views
from xhatapp.views import chatbot_view, export_to_pdf

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.login_usr,name='indexpage'),
   # path('login',views.login_usr,name="llooggin"),
    path('Xhat/',include('xhatapp.urls')),
    path("check",views.query,name="xhat"),
    path('Signin',views.create,name='createeacc'),
    path('logout',views.usr_logout,name="logggout"),
    path('password_reset',views.forgot,name="password_reset"),
    path('password_reset_done',views.forgotdone,name="password_reset_done"),
    path('chatbot/', chatbot_view, name='chatbot'),
    path('export-pdf/', export_to_pdf, name='export_pdf'),
    path('export-to-pdf/', export_to_pdf, name='export_to_pdf'),
    path('login',views.forgotdone,name="login"),
    path('Download',views.download,name="Download"),
    path('Account_Settings.html',views.Account,name="Account"),
  ]
