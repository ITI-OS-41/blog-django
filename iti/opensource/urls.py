from django.urls import path
from opensource import views

urlpatterns = [
    path('', views.getAllPosts),
    path('post/<postId>', views.getPost),
    path('post/create/', views.newPost),
    path('post/edit/<postId>', views.editPost),
    path('post/delete/<postId>', views.deletePost),
]   