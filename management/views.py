from django.shortcuts import render
# -*- coding: UTF-8 -*-
# Create your views here.
from django.http import HttpResponse

# def listorders(request):
#     return HttpResponse("下面是所有的返回信息 。")


# 导入 student 对象定义
from  common.models import  Student_info

# def liststudents(request):
#     # 返回一个 QuerySet 对象 ，包含所有的表记录
#     # 每条表记录都是是一个dict对象，
#     # key 是字段名，value 是 字段值
#     qs = Student_info.objects.values()
#
#     # 定义返回字符串
#     retStr = ''
#     for student in  qs:
#         for name,value in student.items():
#             retStr += f'{name} : {value} | '
#
#         # <br> 表示换行
#         retStr += '<br>'
#
#     return HttpResponse(retStr)
#
# def liststudents_M(request):
#     # 返回一个 QuerySet 对象 ，包含所有的表记录
#     qs = Student_info.objects.values()
#
#     # 检查url中是否有参数Ssex
#     ph =  request.GET.get('Ssex',None)
#
#     # 如果有，添加过滤条件
#     if ph:
#         qs = qs.filter(Ssex=ph)
#
#     # 定义返回字符串
#     retStr = ''
#     for student in  qs:
#         for name,value in student.items():
#             retStr += f'{name} : {value} | '
#         # <br> 表示换行
#         retStr += '<br>'
#
#     return HttpResponse(retStr)
# 先定义好HTML模板
html_template = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
        <th>学号</th>
        <th>姓名</th>
        <th>性别</th>
        <th>专业</th>
        <th>寝室号</th>
        </tr>

        {% for student in students %}
            <tr>

            {% for name, value in student.items %}            
                <td>{{ value }}</td>            
            {% endfor %}

            </tr>
        {% endfor %}

        </table>
    </body>
</html>
'''

from django.template import engines

django_engine = engines['django']
template = django_engine.from_string(html_template)


def liststudents(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Student_info.objects.values()

    # 检查url中是否有参数phonenumber
    ph = request.GET.get('Ssex', None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(Ssex=ph)

    # 传入渲染模板需要的参数
    rendered = template.render({'students': qs})

    return HttpResponse(rendered)