from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

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
