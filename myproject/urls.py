"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
import blogpost.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogpost.views.read_blog_list, name='read_blog_list'),
    path('blog/new', blogpost.views.blog_new, name='blog_new'),
    path('blog/create', blogpost.views.create_blog, name="create_blog"),
    path('blog/detail/<int:pk>', blogpost.views.read_blog_one, name='read_blog_one'),
    # int: 변수 명이랑 views.py에 있는 변수 명이랑 같아야해
    path('blog/update/<int:pk>', blogpost.views.update_blog, name='update_blog'),
    path('blog/delete/<int:pk>', blogpost.views.delete_blog, name='delete_blog'),
    path('signup/', accounts.views.signup, name="signup"),
    path('login/', accounts.views.login, name="login"),
    path('logout/', accounts.views.logout, name="logout"),
]
