from django.shortcuts import render , HttpResponse
from blog.models import Blogs
# Create your views here.

def home(request):
    blogs = Blogs.objects.all()
    print(blogs)
    params = {'blogs':blogs}
    return render(request , 'blog/bloghome.html', params)

def blogPost(request,myid): #slug variable should be same.. as in urls.py
    print(myid)
    # return HttpResponse(f'Blog post working...{slug}') #An fstring for checking slug...
    blogPost = Blogs.objects.filter(sno=myid).first
    params = {'blogPost':blogPost}
    return render(request , 'blog/blogPost.html',params)