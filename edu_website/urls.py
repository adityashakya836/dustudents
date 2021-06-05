"""edu_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from blog.views import blog
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.auth.views import LogoutView
from django.conf.urls import url
from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.contrib.auth.models import User

admin.site.site_header="DU Students Admin"
admin.site.site_title="DU Students Admin Panel"
admin.site.index_title="Welcome To Du Students Admin Panel"

class OTPAdmin(OTPAdminSite):
    pass
admin_site=OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice)
urlpatterns = [
    path('admin/', admin_site.urls),
    path('dadmin/',admin.site.urls),
    path('',include('mainpage.urls')),
    path('blogs/',include('blog.urls')),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
