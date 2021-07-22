from django.core import paginator
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User,auth
from blog.models import Myblogpost
from . models import *
# Create your views here.

def home(request):
    blogpost=Myblogpost.objects.all().order_by("-pub_data")[:3]
    news=News.objects.all().order_by("-news_date")[:3]
    return render(request,'mainpage/home.html',{'blogpost':blogpost,'news':news})

def aboutus(request):
    return render(request,'mainpage/about.html')
def contact(request):
    if request.method=='POST':
        u_name=request.POST.get('name','')
        u_email=request.POST.get('email','')
        u_phone=request.POST.get('phone','')
        u_message=request.POST.get('message','')
        if len(u_name)==0 or len(u_email)==0 or len(u_phone)==0 or len(u_message)==0:
            messages.error(request,'All Fields are required')
        else:
            contact=Contacts(c_name=u_name,c_email=u_email,c_phone=u_phone,c_message=u_message)
            contact.save()
            messages.success(request,'Thank you for contacting us. We will get back to you as soon as possible')
        return redirect('/contact/')
    else:
        return render(request,'mainpage/contact.html')
def program(request):
    prog=Program.objects.all()
    return render(request,'mainpage/courses.html',{'program':prog})

def news(request):
    news=News.objects.all().order_by("-news_date")
    paginator=Paginator(news,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'mainpage/news.html',{'news':page_obj})

def newspost(request,title):
    news=News.objects.filter(news_title=title)
    return render(request,'mainpage/newspost.html',{'news':news[0]})


def course(request,program_name):
    prog=Program.objects.get(program_name=program_name)
    course=Course.objects.filter(program=prog)
    return render(request,'mainpage/course.html',{'course':course})

def subject(request,course_name):
    cour=Course.objects.get(course_name=course_name)
    subject=Subject.objects.filter(course=cour)
    return render(request,'mainpage/subject.html',{'subject':subject})

def subdetails(request,subject_name):
    sub=Subject.objects.filter(subject_name=subject_name)
    return render(request,'mainpage/notes.html',{'sub':sub})

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        password1=request.POST['pass1']
        password2=request.POST['pass2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request,"User Already exists")
            elif User.objects.filter(email=email).exists():
                messages.warning(request,"Email already taken")
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                messages.success(request,"User Created")
        else:
            messages.error(request,"Password Not match")
        return redirect('/')
    else:
        return redirect('/')
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid login credential')
            return redirect('/')
    else:
        return render(request,'mainpage/home.html')
        
def logout(request):
    auth.logout(request)
    return redirect('/')
def search(request):
    query=request.GET['query']
    allProg=Program.objects.filter(program_name__icontains=query)
    return render(request,"mainpage/search.html",{'query':allProg})