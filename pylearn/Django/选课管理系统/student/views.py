from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import Student, StudentDetail,Clas,Course


def index(request):
    #获取全部学生的信息
    student_list = Student.objects.all()
    #所有学生的班级信息
    return render(request,'whole/index.html',{'student_list':student_list})

def register(request):

    return render(request,'whole/register.html')
def form(request):
    return render(request,'whole/forms.html')

def add(request):
    #获取全部的班级信息
    if request.method == 'GET':
        class_list = Clas.objects.all()
        return render(request,'whole/add.html',{'class_list':class_list})
    else:
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        clas_id = request.POST.get('clas_id')

        Student.objects.create(
            name = name,
            age = age,
            sex = sex,
            clas_id = clas_id
        )
        # Student.objects.create(**request.POST.dict )
        # print(*request.POST)
        return redirect('/student/index')
def delete(request,stu_id):
    stu = Student.objects.get(pk=stu_id)
    if request.method == 'GET':
        return render(request,'whole/delete.html',{'stu':stu})
    elif request.method == 'POST':
        stu.delete()
        return redirect('/student/index')

def edit(request,edit_id):
    stu = Student.objects.get(pk=edit_id)
    if request.method == 'GET':
        courses_list = Course.objects.all()
        clas_list = Clas.objects.all()
        return render(request,'whole/edit.html',{'stu':stu,'courses_list':courses_list,'clas_list':clas_list})
    elif request.method == 'POST':
        # cour = request.POST.getlist('course_id_list')
        # data = request.POST.dict()
        # data.pop('course_id_list')
        # # Student.objects.filter(pk=edit_id).update(*data)
        # # stu.courses.set(cour)
        # print(*data)
        # return redirect('/student/index')db_student2course
        print("request.POST", request.POST)
        course_id_list = request.POST.getlist("course_id_list")
        # 获取客户端数据
        data = request.POST.dict()
        print("data", data)
        # 删除并获取课程id列表
        data.pop("course_id_list")
        print(data)
        # 更新除了多对多以外的数据
        # edit_id = int(edit_id)
        Student.objects.filter(id=edit_id).update(**data)
        stu.courses.set(course_id_list)
        return redirect("/student/index")


def elective(request):
    #获得所有的课程
    courses = Course.objects.all()
    return render(request,'whole/elective.html',{'courses':courses})

def search(request):
    text = request.GET.get('info')
    key_word = request.GET.get('key_word')
    print(text)
    print(key_word)
    if key_word == '姓名':
        student_list = Student.objects.filter(name__contains=text)
        return render(request, 'whole/index.html', {'student_list': student_list})
    elif key_word == '班级':
        student_list = Student.objects.filter(clas__name=text)
        return render(request, 'whole/index.html', {'student_list': student_list})