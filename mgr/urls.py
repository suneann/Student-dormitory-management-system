"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# -*- coding: UTF-8 -*-
from django.urls import path,include
from django.contrib import admin
from django.urls import path
from mgr import management,sign_in_out

from management.views import liststudents

urlpatterns = [

    path('management/', management.dispatcher),
    # path('signin/', sign_in_out.signin),
    # path('signout',sign_in_out),
]

