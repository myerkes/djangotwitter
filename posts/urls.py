from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('posts/create', views.PostCreate.as_view(), name='postcreate'),
    path('posts/<int:post_pk>/reply', views.ReplyCreate.as_view(), name='replycreate'),
    path('posts/<int:post_pk>/repost', views.RepostCreate.as_view(), name='repostcreate'),
]