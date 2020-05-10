from django.shortcuts import render
from .models import Blog

# Create your views here.
def read_blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs' : blogs})

def blog_new(request):
    return render(request, 'blog_new.html') 

def create_blog(request):
    blog = Blog()
    
    blog.title = request.POST['title']
    blog.content = request.POST['content']
    blog.save()

    blogs = Blog.objects.all()
    

    return render(request, 'blog_list.html', {'blogs' : blogs})