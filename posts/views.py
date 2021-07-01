from posts.models import Post, Reply
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

### Post Views ###
class PostList(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'posts/post_list.html'

### Reply Views ###
class ReplyList(DetailView):
    model = Post
    template_name = 'posts/reply_list.html'
