from django.urls import path

from demoapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('loginview',views.loginview,name="loginview"),
    path('adminhome',views.adminhome,name="adminhome"),
    path('userhome',views.userhome,name="userhome"),
    path('profileview',views.profileview,name="profileview"),
    path('userviewcourse',views.userviewcourse,name="userviewcourse"),
    path('courseadd',views.courseadd,name='courseadd'),
    path('admviewcourse',views.admviewcourse,name='admviewcourse'),
    path('courseupdate/<int:id>/',views.courseupdate,name='courseupdate'),
    path('deletecourse/<int:id>/',views.deletecourse,name='deletecourse'),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='user/changepassword1.html',success_url = '/passwordchangedone/'),name='change_password'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='user/passwordchangedone.html'),name='passwordchangedone'),



]
