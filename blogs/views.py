from django import forms
from django.views.generic import ListView, DetailView

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
