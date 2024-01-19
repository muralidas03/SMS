from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from StudentApp.models import Course, Student


@login_required
def home(request):
    students = Student.objects.all()
    # data = {'studs':students}
    return render(request,'home.html',{'studs':students})

# Create your views here.
@login_required
def add(request):
    if request.method == 'POST':
        s = Student()
        s.name = request.POST['tbname']
        s.phone = request.POST['tbphno']
        s.email = request.POST['tbemail']
        s.age = request.POST['tbage']
        s.course = Course.objects.get(cname=request.POST['ddlcourse'])
        s.save()
        return redirect(home)

    else:
        course = Course.objects.all()
        data = {'courses':course}
        return render(request,'addstudent.html',data)

@login_required
def edit(request,id):
    s = Student.objects.get(id=id)
    if request.method == 'POST':

        s.name = request.POST['tbname']
        s.phone = request.POST['tbphno']
        s.email = request.POST['tbemail']
        s.age = request.POST['tbage']
        s.course = Course.objects.get(cname=request.POST['ddlcourse'])
        s.save()
        return redirect(home)
    else:
        courses = Course.objects.all()
        data = {'student':s,'courses':courses}
        return render(request,'edit.html',data)
    return None

@login_required
def deletefun(request,id):
    s = Student.objects.get(id=id)
    s.delete()
    return redirect(home)


def dummy(request):
    return render(request,'login.html')

@never_cache
def loginfun(request):
    if request.method == "POST":
        user_name = request.POST['tbusername']
        user_password = request.POST['tbpass']
        myuser = authenticate(username=user_name, password=user_password)
        if myuser is not None:
            if myuser.is_superuser:
                u1 = User.objects.get(username=user_name)
                request.session['myuser'] = u1.id  # based on the id we are getting a details
                request.session['myusername'] = u1.username # based on the id we are getting a details
                login(request,u1)
                return render(request, 'index1.html', {'data': u1.username})
        else:
            return render(request, 'login.html', {'msg': 'credential is not matching!!!'})
    return render(request,'login.html')

@never_cache
def registerfun(request):
    if request.method == "POST":
        uname = request.POST['tbusername']
        useremail = request.POST['tbemail']
        userpswd = request.POST['tbpass']
        if User.objects.filter(username=uname).exists():
            return render(request, 'register.html', {'user_available': True})
        elif User.objects.filter(email=useremail).exists():
            return render(request, 'register.html', {'email_available': True})
        else:
            user = User.objects.create_user(email=useremail, password=userpswd, username=uname)
            user.save()
            return render(request, 'index1.html')
    return render(request,'register.html')

@never_cache
def logoutfun(request):
    logout(request)
    request.session['myuser'] = None
    request.session['myusername'] = None
    return redirect(loginfun)