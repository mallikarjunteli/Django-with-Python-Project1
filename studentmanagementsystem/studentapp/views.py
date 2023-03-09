from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect


# Create your views here.
def index_fun(request):
    c1 = Course.objects.values()
    return render(request,'index.html',{'data' : c1})

def read_data_fun(request):
    sname = request.POST['txtName']
    sage = request.POST['txtAge']
    scourse = request.POST['ddlcourse']
    c2 = Course.objects.values(Course_name=scourse)
    s1 = Student(name=sname,age=sage,course_id=c2)
    s1.save()
    return redirect('index')

def display_fun(request):
    s1 = Student.objects.all()
    return render(request,'display.html',{'data':s1})

def delete_fun(request,x):
    s1 = Student.object.get(id=x)
    s1.delete()
    return redirect('display')

def update_fun(request,id):
    s1 = Student.objects.get(id=id)
    c1 = Course.objects.get(id= s1.course_id_id)
    c2 = Course.objects.values()
    if request.method == 'POST':
        s1.name = request.POST['txtName']
        s1.age = request.POST['txtAge']
        s1.course_id = Course.objects.get(course_name=request.POST['ddlcourse'])
        s1.save()
        return redirect('display')
    return
render(request,'update.html',{'data':s1,'data2':c1.course_name,'data3':c2})


def reg_fun(request):
    return render(request,'register.html')

def reg_data_fun(request):
    uname = request.POST['txtName']
    password = request.POST['txtPswd']
    mail = request.POST['txtrEmail']
    u1 = User.objects.create_superuser(username=uname,password=password,email=mail)
    u1.save()
    return redirect('log')

def log_fun(request):
    return render(request,'login.html',{'data':''})

def log_read_fun(request,_issuperuser=None):
    if request.method=='POST':
        name = request.POST['txtName']
        password = request.POST['txtPswd']
        myuser = authenticate(username=name,password=password)
        if myuser is not None:
            if myuser.is_superuser:
                return render(request,'home.html',{'data1:myuser'})
            else:
                return render(request,'login.html',{'data':'credential are not valid'})


def home_fun(request):
    return render(request,'home.html')


def logout_fun(request):
    logout(request)
    return render('log')
    return None