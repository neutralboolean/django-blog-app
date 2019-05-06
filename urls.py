from django.urls import path
from django.views.generic import ListView, DetailView
from .models import Post
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/<slug:slug>/', views.PostView.as_view(), name='post'),
    path('', views.ret_to_index, name='return'),
]
