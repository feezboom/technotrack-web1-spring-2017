from django import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blogs.forms import BlogForm
from blogs.models import Blog


class SortForm(forms.Form):
    sort = forms.ChoiceField(
        choices=(
            ("no_sort", "No sort"),
            ("title", "By title"),
            ("rate", "By rate"),
            ("description", "By description"),
        ),
        required=False,
        widget=forms.RadioSelect
    )
    search = forms.CharField(required=False, widget=forms.TextInput)


class BlogsList(ListView):
    queryset = Blog.objects.all()
    template_name = "blogs/blogs.html"
    sort_form = None

    def dispatch(self, request, *args, **kwargs):
        self.sort_form = SortForm(self.request.GET)
        return super(BlogsList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogsList, self).get_context_data(**kwargs)
        context["sort_form"] = self.sort_form
        return context

    def get_queryset(self):
        qs = super(BlogsList, self).get_queryset()
        if self.sort_form.is_valid():

            if self.sort_form.cleaned_data["sort"] != "no_sort" and \
                            self.sort_form.cleaned_data["sort"] != "":
                qs = qs.order_by(self.sort_form.cleaned_data["sort"])

            if self.sort_form.cleaned_data["search"]:
                qs = qs.filter(title__icontains=self.sort_form
                               .cleaned_data["search"])
        return qs


class BlogView(DetailView):
    queryset = Blog.objects.all()
    template_name = "blogs/blog.html"


class UpdateBlog(UpdateView):
    model = Blog
    fields = ('title', 'description', 'rate')
    success_url = reverse_lazy('core:blogs:show_all_blogs')


class CreateBlog(CreateView):
    model = Blog
    # form_class = BlogForm
    success_url = reverse_lazy('core:blogs:show_all_blogs')
    # fields = '__all__'
    fields = ('title', 'description')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 1
        # form.instance.field['author'].widgets.update({'author': forms.HiddenInput()})
        return super(CreateBlog, self).form_valid(form)
    #
    # def get_form(self, form_class=form_class):
    #     initials = {
    #         "author": self.request.user,
    #         "rate": 0
    #     }
    #     form = form_class(initial=initials)
    #     return form

