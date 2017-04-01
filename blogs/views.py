from django.shortcuts import render

from blogs.models import Blog
from posts.models import Post


def show_all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/blogs.html', {'all_blogs_list': blogs})


def show_one_blog(request, blog_id=None):
    blog = Blog.objects.get(id=blog_id)
    posts = Post.objects.filter(blog_owner_id=blog_id)
    return render(request, 'blogs/blog.html', {"blog": blog,
                                               "posts": posts})
