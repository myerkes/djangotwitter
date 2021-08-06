from django.urls import path

from . import views

app_name = 'myaccount'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('<int:user_pk>/profile/', views.Profile2.as_view(), name='profileid'),
]