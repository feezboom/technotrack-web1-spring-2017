from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy

from blogs.models import Blog
from comments.models import Comment
from posts.models import Post


def show_welcome_page(request):
    blogs_count = Blog.objects.all().count()
    posts_count = Post.objects.all().count()
    comments_count = Comment.objects.all().count()
    return \
        render(request, reverse_lazy('core:welcome_page'), {
                                            "blogs_num": blogs_count,
                                            "posts_num": posts_count,
                                            "comments_num": comments_count})


def test(request, post_id=None, blog_id=None, *args, **kwargs):
    # return HttpResponse('test passed mfk, {}'.format(request.GET['a']))
    # return HttpResponse('test 0 passed mfk, {}'.format(request.GET['name']))
    # return HttpResponse('test 0 passed mfk, {}'.format(post_id))

    # We can write html code inside html response.
    # return HttpResponse(r'post_id={}, blog_id={}'.format(post_id, blog_id))

    # return render(request, 'core/example.html', {"post_id": post_id,
    #                                           "blog_id": blog_id})

    posts_titles = [
        "first post",
        "second post",
        "third post",
    ]

    return render(request, 'core/example.html', {"post_id": post_id,
                                                 "blog_id": blog_id,
                                                 "posts_titles": posts_titles})


class AuthorizationForm(forms.Form):
    login = forms.TextInput()
    password = forms.PasswordInput()
