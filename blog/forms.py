from django import forms

from blog.models import Post


class BlogCreateForm(forms.ModelForm):
    model = Post
    fields = '__all__'


