from django import forms
from blogs.models import Blog

# todo: use this


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        widgets = {"author": forms.HiddenInput(),
                   "rate": forms.HiddenInput()}
        fields = "__all__"
    # fields = ['title', 'description', 'rate']
