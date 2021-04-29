from django.contrib import admin
from . models import Myblogpost,Comments,PostViews
# Register your models here.

admin.site.register(Comments)
admin.site.register(PostViews)

@admin.register(Myblogpost)
class MyblogpostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tiny.js',)