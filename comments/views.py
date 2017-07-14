from django.views.generic import ListView, DetailView, CreateView

from comments.models import Comment


class CreateComment(CreateView):
    model = Comment
    post_owner_id = None
    post_owner = None
    # todo : fields = '__all__' and make author, blog owner fields hidden
    fields = ['text']
