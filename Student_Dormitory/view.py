# -*- coding: UTF-8 -*-
# from django.http import HttpResponse

from django.shortcuts import render

# def hello(request):
#     return HttpResponse("Hello world ! ")

from django.shortcuts import render

# def runoob(request):
#   view_name = "iodin"
#   return  render(request,"runoob.html", {"name":view_name})


from django.shortcuts import render


# def runoob(request):
#     context = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'runoob.html', context)
# from django.shortcuts import render
# def runoob(request):
#   view_name = 0
#   return  render(request,"runoob.html",{"name":view_name})

#  return  render(request,"runoob.html", {"name":view_name})


# def runoob(request):
#     views_list = ["1","2","3"]
#     return render(request, "runoob.html", {"views_list": views_list})

# from django.shortcuts import render
# def runoob(request):
#     views_dict = {"name":"iodin"}
#     return render(request, "runoob.html", {"views_dict": views_dict})

# def runoob(request):
#     num=1024
#     return render(request, "runoob.html", {"num": num})

from django.shortcuts import render

# def runoob(request):
#     import datetime
#     now  =datetime.datetime.now()
#     return render(request, "runoob.html", {"time": now})



# def runoob(request):
#     views_str = "<a href='https://www.iodin.cn/'>Turning to the blog</a>"
#     return render(request, "runoob.html", {"views_str": views_str})

def runoob(request):
    views_num = 88
    return render(request, "runoob.html", {"num": views_num})