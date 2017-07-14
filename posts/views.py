from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from blogs.models import Blog
from posts.models import Post


class PostsList(ListView):
    queryset = Post.objects.all()
    template_name = "posts/posts.html"


class PostView(DetailView):
    queryset = Post.objects.all()
    template_name = "posts/post.html"


class CreatePost(CreateView):
    model = Post
    blog_owner_id = None
    blog_owner = None
    # todo : fields = '__all__' and make author, blog owner fields hidden
    fields = ('title', 'text')
    template_name = 'posts/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 1
        form.instance.blog_owner = self.blog_owner
        return super(CreatePost, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        print (self.request.GET.get('blog_id', ''))
        self.blog_owner_id = self.request.GET.get('blog_id', '')
        self.blog_owner = \
            get_object_or_404(Blog, pk=self.blog_owner_id)
        return super(CreatePost, self).dispatch(request, *args, **kwargs)

    # todo : make it work
    # success_url = reverse_lazy('core:blogs:show_blog_by_id',
    #                            kwargs={'pk': blog_owner_id})
    success_url = reverse_lazy('core:blogs:show_all_blogs')
