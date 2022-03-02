# -*- coding: UTF-8 -*-

from django.http import JsonResponse
import json
# 导入 Student_info

from common.models import Student_info
def dispatcher(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST','PUT','DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)


    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_student':
        return liststudents(request)
    elif action == 'add_student':
        return addstudent(request)
    elif action == 'modify_student':
        return modifystudent(request)
    elif action == 'del_student':
        return deletestudent(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})
        ##返回JS格式字符串

def liststudents(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Student_info.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


def addstudent(request):
    info = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = Student_info.objects.create(
        Sid=info['Sid'],
        Sname=info['Sname'],
        Ssex=info['Ssex'],
        Dmaj_id=info['Dmaj_id'],
        Aroom_id=info['Aroom_id'],
    )

    return JsonResponse({'ret': 0, 'id': record.id})
# JsonResponse在完成后都会返回相应的值

def modifystudent(request):
    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作

    studentid = request.params['id']
    newdata = request.params['newdata']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        student = Student_info.objects.get(id=studentid)
    except Student_info.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{studentid}`的学生不存在'
        }

    if 'Sid' in newdata:
        student.Sid = newdata['Sid']
    if 'Sname' in newdata:
        student.Sname = newdata['Sname']
    if 'Ssex' in newdata:
        student.Ssex = newdata['Ssex']
    if 'Dmaj_id' in newdata:
        student.Dmaj_id = newdata['Dmaj_id']
    if 'Aroom_id' in newdata:
        student.Aroom_id = newdata['Aroom_id']

    # 注意，一定要执行save才能将修改信息保存到数据库
    student.save()

    return JsonResponse({'ret': 0})

def deletestudent(request):

    studentid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        student = Student_info.objects.get(id=studentid)
    except Student_info.DoesNotExist:
        return  {
                'ret': 1,
                'msg': f'id 为`{studentid}`的客户不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    student.delete()

    return JsonResponse({'ret': 0})
