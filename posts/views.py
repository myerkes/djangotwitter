from posts.forms import *
from posts.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

### Post Views ###
class PostList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'posts/post_list.html'

    ordering = ['-pub_datetime']

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/post_create_form.html'
    success_url = '../posts'


