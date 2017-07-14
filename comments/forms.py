from django import forms

from comments.models import Comment


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {"author": forms.HiddenInput(),
                   "post_owner": forms.HiddenInput()}


