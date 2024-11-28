from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Student
from django.db.models import Avg, F


def add(request):
    Student.objects.create(
        name='王',
        age=20,
        sex=1,
        classmate='2'
    )
    return HttpResponse('添加成功')
def select(request):
    stu = Student.objects.all()#第一步查询到的是一个jquery集合
    print(stu)
    print(stu[0].name)
    return HttpResponse('查询成功')
def select2(request):

    # age_avg = Student.objects.aggregate(age_avg = Avg('age'))#查询年龄的平均值
    #原生sql
    ret = Student.objects.raw("SELECT * FROM db_student")
    print(ret,type(ret))
    for stu in ret:
        print(stu)
    return HttpResponse('OK')
#修改
def update(request):
     #让所有男生的年龄减少2岁
     #需要用到源数据的更新
    stu = Student.objects.filter(sex=1).update(age = F('age') - 2)#用F代表该属性的值
    print(stu)#返回值stu代表受影响的行数
    return HttpResponse('OK')
#删除操作
def delete(request):
    #删除姓名以王开头的记录
    stu = Student.objects.filter(name__startswith='王').delete()
    print(stu)
    return HttpResponse('删除成功')
