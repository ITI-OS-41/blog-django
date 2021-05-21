from django.urls import path
from opensource import views

urlpatterns = [
    path('', views.getAllPosts),
    path('post/<postId>', views.getPost),
    path('create/', views.newPost),
    path('edit/<postId>', views.editPost),
    path('delete/<postId>', views.deletePost),
]   