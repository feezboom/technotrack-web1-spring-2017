from django.views.generic import ListView, DetailView
from posts.models import Post


class PostsList(ListView):
    queryset = Post.objects.all()
    template_name = "posts/posts.html"


class PostView(DetailView):
    queryset = Post.objects.all()
    template_name = "posts/post.html"
