from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from demoapp.forms import Loginform, userloginform, courseaddform
from demoapp.models import userlogin, Login, courses


# Create your views here.
def home(request):
    return render(request,"index.html")

def register(request):
    form = Loginform()
    form1 = userloginform()
    if request.method == "POST":
        form = Loginform(request.POST)
        form1 = userloginform(request.POST,request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.is_user = True
            user.save()
            usr = form1.save(commit=False)
            usr.user = user
            usr.save()
            return redirect('loginview')
    return render(request,"registration.html",{'form':form,'form1':form1})

def loginview(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username =username,password = password)
        if user is not None and user.is_staff:
            login(request,user)
            return redirect('adminhome')
        if user is not None and user.is_user:
            login(request,user)
            return redirect('userhome')
        else:
            messages.info(request,"Invalid Credentials")
    return render(request,"login.html")

def adminhome(request):
    return render(request,'admin/adminhome.html')

def userhome(request):
    return render(request,'user/userhome.html')


def profileview(request):
    u= request.user
    data = userlogin.objects.filter(user=u)
    print(data)
    return render(request,'user/profileview.html',{'data':data})

#Change Password
# def changepass(request,id):
#     user = Login.objects.get(id=id)
#     form = Loginform(instance=user)
#     if request.method == "POST":
#         form = Loginform(request.POST or None,request.FILES,instance=user or None)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.save()
#             return redirect('userhome')
#     return render(request,'user/changePassword.html',{'form':form})


def courseadd(request):
    form = courseaddform()
    u = request.user
    if request.method == 'POST':
        form = courseaddform(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
        return redirect('admviewcourse')
    return render(request,'admin/courseadd.html', {'form': form})

def admviewcourse(request):
    data = courses.objects.all()
    return render(request,'admin/admviewcourse.html',{'data':data})


def courseupdate(request,id):
    user = courses.objects.get(id=id)
    form = courseaddform(instance=user)
    if request.method == "POST":
        form = courseaddform(request.POST or None, request.FILES, instance=user or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('admviewcourse')
    return render(request,'admin/updatecourse.html', {'form': form})

def deletecourse(request,id):
    course = courses.objects.get(id=id)
    course.delete()
    return redirect('admviewcourse')

# USER

def userviewcourse(request):
    data = courses.objects.all()
    return render(request,'user/userviewcourse.html',{'data':data})
