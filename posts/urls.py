from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('posts/create', views.PostCreate.as_view(), name='postcreate'),
    path('<int:pk>/replies', views.ReplyList.as_view(), name='replies'),
]