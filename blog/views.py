from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Myblogpost,Comments
from blog.templatetags import get_dict
from django.core.paginator import Paginator
# Create your views here.
def blog(request):
    post=Myblogpost.objects.all().order_by('-pub_data')
    paginator=Paginator(post,10)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    blog_label=Myblogpost.objects.values('blog_category')
    category={item['blog_category'] for item in blog_label}
    return render(request,'blog/blog.html',{'page_obj':page_obj,'category':category})

def labelpost(request,category):
    blogpost=Myblogpost.objects.filter(blog_category=category)
    paginator=Paginator(blogpost,4)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    blog_label=Myblogpost.objects.values('blog_category')
    category={item['blog_category'] for item in blog_label}
    return render(request,'blog/labelpost.html',{'page_obj':page_obj,'category':category})

def blogpost(request,slug):
    blogspost=Myblogpost.objects.filter(blog_title=slug).first()
    blogspost.views=blogspost.views+1
    blogspost.save()
    comment=Comments.objects.filter(post=blogspost,parent=None)
    replies=Comments.objects.filter(post=blogspost).exclude(parent=None)
    repDict={}
    for reply in replies:
        if reply.parent.id not in repDict.keys():
            repDict[reply.parent.id]=[reply]
        else:
            repDict[reply.parent.id].append(reply)

    blog_label=Myblogpost.objects.values('blog_category')
    category={item['blog_category'] for item in blog_label}
    
    context={'blogpost':blogspost,'comments':comment,'replies':repDict,'category':category}
    return render(request,'blog/blog_post.html', context)

def search(request):
    query=request.GET['query']
    # allPosts=Myblogpost.objects.all()
    if len(query)>40:
        allPosts=Myblogpost.objects.none()
    else:
        allPostsTitle=Myblogpost.objects.filter(blog_title__icontains=query)
        allPostsContent=Myblogpost.objects.filter(blog_description__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent)

    blog_label=Myblogpost.objects.values('blog_category')
    category={item['blog_category'] for item in blog_label}
        
    params={'page_obj':allPosts,'query':query,'category':category}
    return render(request,'blog/search.html',params)

def comment(request):
    if request.method=='POST':
        comment=request.POST.get('comment')
        user=request.user
        postId=request.POST.get('postId')
        post=Myblogpost.objects.get(id=postId)
        parentId=request.POST.get('parentId')
        if parentId=="":
            comment=Comments(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,"Your comment have been posted successfully")
        else:
            parent=Comments.objects.get(id=parentId)
            comment=Comments(comment=comment,user=user,post=post,parent=parent)
            comment.save()
            messages.success(request,"Your comment have been posted successfully")

    return redirect(f'/blogs/blogpost/{post.blog_title}')

def post(request):
        if request.method=="POST":
            blog_title=request.POST['title']
            blog_sub_title = request.POST['sub_title']
            blog_by = request.POST['blog_by']
            blog_description = request.POST['description']
            blog_date = request.POST['date']
            blog_image = request.FILES['image']
            blog_category=request.POST['blog_category']
            Myblogpost.objects.create(blog_title=blog_title,blog_description=blog_description,blog_by=blog_by,blog_sub_title=blog_sub_title,
                            pub_data=blog_date,blog_img=blog_image,blog_category=blog_category)

            return redirect('/')
        else:
            blog_label=Myblogpost.objects.values('blog_category')
            category={item['blog_category'] for item in blog_label}
            return render(request,'blog/post.html',{'category':category})