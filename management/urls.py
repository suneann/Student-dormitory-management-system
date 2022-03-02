# -*- coding: UTF-8 -*-
from django.urls import path
from . import views
from management.views import liststudents

urlpatterns = [
    path('student/', liststudents),
#    path('student/', liststudents_M),
]

