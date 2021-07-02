from .models import *
from django import forms

### Post Forms ###
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_text']