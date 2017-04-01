from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blogs.views import show_all_blogs
from comments.models import Comment
from posts.models import Post


class PostView(DetailView):
    queryset = Post.objects.all()
    template_name = "posts/post.html"

# class CommentsList(ListView):
#     queryset = Comment.objects.all()
#     template_name = '/post/.html'
#
#     pass


# def show_one_post(request, post_id=None):
#     post = Post.objects.get(id=blog_id)
#     comments = Post.objects.filter(blog_owner_id=blog_id)
#     return render(request, 'blogs/blog.html', {"blog": blog,
#                                                "posts": posts})
