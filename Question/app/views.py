from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import *
from django.contrib import auth
import json
import datetime


# 转换JSON
class Change(object):
    def __init__(self, message):
        self.message = message

    # 问题转换
    def QUEST(self):
        Quest = {'Qid': self.message.qid, 'Question': self.message.question, 'Question_Detail': self.message.question_detail,
                 'Question_Date': self.message.question_date.strftime('%Y-%m-%d %H:%M:%S'), 'Count': self.message.count,
                 'username': User.objects.filter(uid=self.message.user_id).first().username}
        return Quest

    # 用户转换
    def USER(self):
        user = {'uid': self.message.uid, 'username': self.message.username, 'password': self.message.password}
        return user

    # 回答转换
    def ANSWER(self):
        answer = {'aid': self.message.aid, 'answer_date': self.message.answer_date.strftime('%Y-%m-%d %H:%M:%S'),
                  'answer_detail': self.message.answer_detail, 'question_id': self.message.question_id,
                  'username': User.objects.filter(uid=self.message.user_id).first().username}
        return answer


# 登录
def Login(request):
    if request.method == "POST":
        VueData = json.loads(request.body)  # 获取vue传过来登录的数据
        user = User.objects.all()           # 查询用户表所有信息
        ret = {"status": 0, 'url': ''}
        for i in user:
            u = Change(i).USER()            # 将用户表中数据转换为json格式
            if VueData['user'] == u['username'] and VueData['password'] == u['password']:   # 判断用户名密码是否正确
                request.session['uid'] = u['uid']       # session存值，用于用户认证
                ret['status'] = 1                       # 改变状态，vue获取时会用到做登录判断
                ret['url'] = '/index/'                  # 登录后指向的路由
                return JsonResponse(ret)                # 将ret传到vue
        else:
            return JsonResponse({'code': 300})          # 用户名密码错误时的状态


# 退出登录
def Loginout(request):
    if request.method == 'POST':
        auth.logout(request)        # 清除登录状态的session
        return JsonResponse({'code': 'loginout'})   # 注销的状态


# 主页
def Index(request):
    uid = request.session.get('uid')       # 获取登录的用户id
    if request.method == "GET":            # get请求触发
        q = {}
        count = 0                          # 计数用于问题分组
        for Quest in Question.objects.all():        # 遍历所有问题
            count += 1
            q[count] = Change(Quest).QUEST()    # 将问题表的数据全部转换成json格式
        return JsonResponse(q)                      # 将数据传到vue
    if request.method == 'POST':                    # post请求触发
        qdata = json.loads(request.body)            # 获取vue传来的问题数据
        date = datetime.datetime.now()              # 当前时间
        # 把提出的问题更新到数据库的Question表中
        Question.objects.create(question=qdata['quest'], question_detail=qdata['detail'], question_date=date, count=0, user_id=uid)
        return JsonResponse({'success': 1})         # 成功状态


# 注册
def regist(request):
    if request.method == "POST":            # post请求触发
        Reg = json.loads(request.body)      # 获取vue传来的注册信息
        username = [Change(i).USER()['username'] for i in User.objects.all()]  # 把用户列表的数据转换成JSON格式
        if Reg['user'] in username:         # 判断用户名是否已存在
            return JsonResponse({'code': 23})   # 用户名已存在的状态
        else:
            if Reg['password1'] != Reg['password2']:    # 判断两次输入的密码是否一致
                return JsonResponse({'code': 24})       # 不一致的状态
            else:
                # print('2')
                reg = User.objects.create(username=Reg['user'], password=Reg['password1'])   # 把成功注册的信息更新到用户表中
                reg.permission.add(Permission.objects.filter(pid=1).first())
                # User.objects.create(pid=3, permission='DA').user.add(uid)
                return JsonResponse({'code': 'finish'})     # 完成的状态


# 回答详情
def answer_detail(request):
    if request.method == 'POST':        # post请求触发
        qid = json.loads(request.body)['qid']   # 返回所选问题的id
        request.session['qid'] = qid            # 把问题id存入session
        a = {}
        count = 0                               # 清空计数
        answers = Answer.objects.filter(question_id=qid).all()  # 把对应问题的所有回答数据查询出来
        for answer in answers:  # 遍历回答数据
            count += 1          # 计数回答次数
            a[count] = Change(answer).ANSWER()  # 以计数分组，将回答数据转换为json格式
        return JsonResponse(a)          # 把回答数据传给Vue


# 回答
def answer(request):
    if request.method == 'POST':            # post请求触发
        uid = request.session.get('uid')    # 获取登陆的用户id
        qid = request.session.get('qid')    # 获取点击的问题id
        qdetail = json.loads(request.body)['detail']    # 获取vue中回答详情的数据
        answer_date = datetime.datetime.now()           # 获取当前时间
        count = Question.objects.filter(qid=qid).first().count  # 获取当前问题被回答的次数
        # 把回答的信息更新到数据库Answer表中
        Answer.objects.create(answer_date=answer_date, answer_detail=qdetail, question_id=qid, user_id=uid)
        Question.objects.filter(qid=qid).update(count=count + 1) # 回答的总计数+1
        return JsonResponse({'code': 'finish'})  # 完成状态


# 修改密码
def change_password(request):
    if request.method == 'POST':            # post请求触发
        uid = request.session.get('uid')    # 获取当前登录的用户
        password = json.loads(request.body)['password']     # 获取vue传来的新密码
        User.objects.filter(uid=uid).update(password=password)  # 把密码改为新密码
        return JsonResponse({'code': 200})      # 返回状态


# 个人中心
def People(request):
    uid = request.session.get('uid')    # 获取当前登录用户的id
    if request.method == 'GET':         # get请求触发
        people = User.objects.filter(uid=uid).first().username      # 获取当前登录的用户名
        answer_count = len(Answer.objects.filter(user_id=uid).all())    # 获取当前用户回答问题的次数
        quit_count = len(Question.objects.filter(user_id=uid).all())    # 获取当前用户提问的次数
        answer_data = [Change(answer).ANSWER() for answer in Answer.objects.filter(user_id=uid).all()]      # 获取当前用户所回答的问题的详情数据
        asks = [Change(quest).QUEST() for quest in Question.objects.filter(user_id=uid).all()]      # 获取当前用户提问的详情数据
        for i in answer_data:   # 遍历当前用户所回答的问题的详情数据
            i['question'] = Question.objects.filter(qid=i['question_id']).first().question      # 把回答对应的问题名称放到回答的总数据中
        # 返回信息
        return JsonResponse({'name': people, 'answer_count': answer_count, 'quit_count': quit_count, 'answer_detail': answer_data, 'asks': asks})
    if request.method == 'POST':       # post请求触发
        name = json.loads(request.body)['name']     # 获取vue传来的用户名数据
        for user in User.objects.all():             # 遍历所有用户
            if name == user.username:               # 判断vue传来的用户名数据是否存在
                return JsonResponse({'status': 'exist'})    # 返回用户名存在的状态
        else:
            User.objects.filter(uid=uid).update(username=name)      # 将更改后的名字更新
            return JsonResponse({'status': 'success'})      # 返回更改成功


# 删除问题
def Delete(request):
    if request.method == 'POST':        # post请求触发
        if 'qid' in json.loads(request.body):           # 判断删除的是不是qid
            qid = json.loads(request.body)['qid']       # 获取qid
            Question.objects.filter(qid=qid).delete()   # 删除qid
        elif 'aid' in json.loads(request.body):         # 判断删除的是不是aid
            aid = json.loads(request.body)['aid']       # 获取aid
            Answer.objects.filter(aid=aid).delete()     # 删除aid
        return JsonResponse({'status': 'success'})      # 返回删除成功


# 修改问题
def Change(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'success'})      # 返回修改成功