from django.views.generic import ListView, DetailView

from comments.models import Comment


class CommentList(ListView):
    queryset = Comment.objects.all()
    template_name = "posts/post.html"


class CommentView(DetailView):
    queryset = Comment.objects.all()
    template_name = "comments/comment.html"
