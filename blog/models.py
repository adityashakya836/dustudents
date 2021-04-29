from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils.timezone import now

# Create your models here.
class Myblogpost(models.Model):
    id=models.AutoField(primary_key=True)
    blog_title=models.CharField(max_length=30)
    blog_description=models.TextField()
    blog_by=models.CharField(max_length=30)
    blog_sub_title=models.CharField(max_length=30)
    pub_data=models.DateTimeField()
    blog_img=models.ImageField(upload_to='blogpics/images',default="")
    blog_category=models.CharField(max_length=40)
    views=models.IntegerField(default=0)
    def __str__(self):
        return self.blog_title+' by '+self.blog_by
    
    @property
    def views_count(self):
        return PostViews.objects.filter(post=self).count()

class Comments(models.Model):
    id=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Myblogpost,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:15]+"...."+self.user.username

class PostViews(models.Model):
    IPAddress=models.GenericIPAddressField(default="45.234.82.169")
    user=models.ForeignKey(User,on_delete=CASCADE)
    post=models.ForeignKey(Myblogpost,on_delete=CASCADE)
    views=models.IntegerField(default=0)

    def __str__(self):
        return '{0} in {1} post'.format(self.IPAddress,self.post.blog_title)