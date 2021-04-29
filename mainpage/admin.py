from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Contacts)
admin.site.register(Program)
admin.site.register(Course)

@admin.register(News,Subject)
class NewsAdmin(admin.ModelAdmin):
    class Media:
        js= ('tiny.js',)