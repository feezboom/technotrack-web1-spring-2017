from django.shortcuts import render

from blogs.models import Blog


def show_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/blogs.html', {'all_blogs_list': blogs})


def show_blog(request, blog_id=None):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/blog.html', {'blog': blog})
