
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='first'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:id>/', views.post_one, name='post_one'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:pk>/edit/', views.PostEditView.as_view(), name='post-edit'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    
]