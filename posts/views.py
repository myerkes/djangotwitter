from django.db.models import query
from posts.forms import *
from posts.models import Post
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
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

    def get_queryset(self):
        return Post.objects.filter(origin=None).order_by('-pub_datetime')

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/post_create_form.html'
    success_url = '../posts'

class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        replies = Post.objects.filter(origin=self.kwargs['pk'])
        context['replies'] = replies
        return context
    

class ReplyCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = ReplyCreateForm
    template_name = 'posts/reply_create_form.html'
    success_url = '..'

    def form_valid(self, form):
        origin = Post.objects.get(pk=self.kwargs['post_pk'])
        self.object = form.save(commit=False)
        self.object.origin = origin
        self.object.save
        return super().form_valid(form)

class RepostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = RepostCreateForm
    template_name = 'posts/repost_create_form.html'
    success_url = '..'

    def form_valid(self, form):
        repost = Post.objects.get(pk=self.kwargs['post_pk'])
        self.object = form.save(commit=False)
        self.object.repost = repost
        self.object.save
        return super().form_valid(form)
    