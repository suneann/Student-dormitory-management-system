# -*- coding: UTF-8 -*-
from django.contrib import admin
from .models import Dmaj_info,Outer_info,Room_info,Apart_info,Student_info,Pprice_info,Floor_info
# Register your models here.
from django.contrib import admin
from django.contrib.admin.models import LogEntry


admin.site.site_header= "学生寝室管理"
admin.site.site_title = "学生寝室管理子系统"
admin.site.index_title = "管理员界面"

# from django.contrib.auth.models import Group, User
# admin.site.unregister(Group)
# admin.site.unregister(User)

class Dmaj_info_Admin(admin.ModelAdmin):
    list_display = ['Ddep','Dmaj']

class Apart_info_Admin(admin.ModelAdmin):
    list_display = ['Aapart']

class Floor_info_Admin(admin.ModelAdmin):
    list_display = ['Lfloor','Lapart']

class Room_info_Admin(admin.ModelAdmin):
    list_display = ['Rroom','RFAinfo','Rlimit','exists']
    search_fields = ('Rroom','RFAinfo')

class Student_info_Admin(admin.ModelAdmin):
    list_display = ['Sid','Sname','Ssex','Sclass','Dmaj','Aroom']
    search_fields = ('Sid', 'Sname', 'Sclass')

class Outer_info_Admin(admin.ModelAdmin):
    list_display = ['Oname','Osex','Ocellphone','Aapart','Ointime','Oouttime','Ops']


class Pprice_info_Admin(admin.ModelAdmin):
    list_display = ['Aapart', 'Pname', 'Pprice', 'Pnum', 'Pintime', 'Pouttime']


admin.site.register(Dmaj_info,Dmaj_info_Admin)

admin.site.register(Outer_info,Outer_info_Admin)

admin.site.register(Room_info,Room_info_Admin)

admin.site.register(Apart_info,Apart_info_Admin)

admin.site.register(Student_info,Student_info_Admin)

admin.site.register(Pprice_info,Pprice_info_Admin)

admin.site.register(Floor_info,Floor_info_Admin)