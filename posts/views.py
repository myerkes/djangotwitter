from posts.models import Post
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

class PostList(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'posts/post_list.html'
