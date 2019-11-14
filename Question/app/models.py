from django.db import models


# 创建用户表
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    permission = models.ManyToManyField(to="Permission")


# 创建问题表
class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200)
    question_detail = models.CharField(max_length=300)
    question_date = models.DateTimeField()
    count = models.IntegerField()
    user = models.ForeignKey(to="User", to_field="uid", on_delete=models.CASCADE)   # 创建一对多表一个用户多个问题


# 创建回答表
class Answer(models.Model):
    aid = models.AutoField(primary_key=True)
    answer_date = models.DateTimeField()
    answer_detail = models.CharField(max_length=300)
    question = models.ForeignKey(to="Question", to_field="qid", on_delete=models.CASCADE)
    user = models.ForeignKey(to="User", to_field="uid", on_delete=models.CASCADE)


# 权限表
class Permission(models.Model):
    pid = models.AutoField(primary_key=True)
    permission = models.CharField(max_length=32)
