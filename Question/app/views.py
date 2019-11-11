from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import *
import json
import datetime

# 问题转换
def Change(message):
    Quest = {'Qid': message.qid,'Question': message.question, 'Question_Detail': message.question_detail,
             'Question_Date': message.question_date.strftime('%Y-%m-%d %H:%M:%S'), 'Count': message.count,
             'User': User.objects.filter(uid=message.user_id).first().username}
    return Quest


# 用户转换
def User_json(user):
    user = {'uid': user.uid, 'username': user.username, 'password': user.password}
    return user


# 登录
def Login(request):
    if request.method == "POST":
        VueData = json.loads(request.body)
        # print(VueData)
        user = User.objects.all()
        for i in user:
            u = User_json(i)
            if VueData['user'] == u['username'] and VueData['password'] == u['password']:
                request.session['uid'] = u['uid']
                return JsonResponse({'code': 200})
        else:
            return JsonResponse({'code': 300})


# 主页
def Index(request):
    uid = request.session.get('uid')
    if request.method == "GET":
        q = {}
        for Quest in Question.objects.all():
            # u = User.objects.filter(uid=Quest.user_id).first()
            # print(Quest.question_date)
            q[Quest.qid] = Change(Quest)
        return JsonResponse(q)
    if request.method == 'POST':
        qdata = json.loads(request.body)
        date = datetime.datetime.now()
        Question.objects.create(question=qdata['quest'], question_detail=qdata['detail'], question_date=date, count=0, user_id=uid)
        return JsonResponse({'success': 1})


# 注册
def regist(request):
    if request.method == "POST":
        Reg = json.loads(request.body)
        print(Reg)
        username = [User_json(i)['username'] for i in User.objects.all()]
        print(username)
        if Reg['user'] in username:
            return JsonResponse({'code': 23})
        else:
            if Reg['password1'] != Reg['password2']:
                return JsonResponse({'code': 24})
            else:
                User.objects.create(username=Reg['user'], password=Reg['password1'])
                return JsonResponse({'code': 'finish'})


# 回答
def answer(request):
    if request.method == 'POST':
        uid = request.session.get('uid')
        # qid = json.loads(request.body)
        # print(qid)
        # Answer.obj ects.filter(question_id=qid)
        return JsonResponse({'id': 2})