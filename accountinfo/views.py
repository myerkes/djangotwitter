from django.shortcuts import render
from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

def profile(request):
    return render(request, 'accountinfo/profile.html')

class Profile2(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.filter(poster=self.kwargs['user_pk'])
        context['post_list'] = posts
        return context