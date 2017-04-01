from django.views.generic import ListView, DetailView

from blogs.models import Blog


class BlogsList(ListView):
    queryset = Blog.objects.all()
    template_name = "blogs/blogs.html"


class BlogView(DetailView):
    queryset = Blog.objects.all()
    template_name = "blogs/blog.html"


# def show_all_blogs(request):
#     blogs = Blog.objects.all()
#     return render(request, "blogs/blogs.html", dict(all_blogs_list=blogs))
#
#
# def show_one_blog(request, blog_id=None):
#     blog = Blog.objects.get(id=blog_id)
#     posts = Post.objects.filter(blog_owner_id=blog_id)
#     return render(request, "blogs/blog.html", dict(blog=blog, posts=posts))
