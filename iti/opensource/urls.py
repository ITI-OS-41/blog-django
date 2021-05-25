from django.urls import path
from opensource import views

urlpatterns = [
    path('', views.getAllPosts, name='posts'),
    path('post/<int:pk>', views.getPost, name='post'),
    path('post/create/', views.newPost),
    path('post/edit/<int:pk>', views.editPost),
    path('post/delete/<int:pk>', views.deletePost),
    path('like/<int:pk>', views.likePost, name='like_post'),
    path('subscribe/<int:pk>', views.subscribeCategory, name='subscribe_category'),
    # path('category/<int:pk>', views.category, name='category'),
    # path('tag/<int:pk>', views.tag, name='tag'),
    path('tag/<slug:slug>/', views.tagged, name="tagged"),
]   