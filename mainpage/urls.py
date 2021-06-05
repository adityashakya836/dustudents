from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView
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
    path('logout/',views.logout,name='logout'),
    path('search/',views.search,name="search"),
    
]