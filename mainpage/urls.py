from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),
    path('program/',views.program,name='program'),
    path('news/',views.news,name='news'),
    path('course/<int:program_id>/',views.course,name='course'),
    path('subject/<int:course_id>/',views.subject,name='subject'),
    path('notes/<int:subject_id>/',views.subdetails,name='subdetails'),
    path('newses/<str:title>/',views.newspost,name='newspost'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
]