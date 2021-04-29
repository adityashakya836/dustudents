from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('ourblog/',views.blog,name='blog'),
    path('blogpost/<str:slug>',views.blogpost,name='blogpost'),
    path('search/',views.search,name='search'),
    #comments
    path('comments/',views.comment,name='comments'),
    path('post/',views.post,name='post'),
    path('label/<str:category>',views.labelpost,name='labelpost')
]
