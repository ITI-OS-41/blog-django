from django.forms.forms import Form
from django.urls import path
from . import views

urlpatterns = [
    # path('register/', UserRegisterView.as_view(), name='register'),
    path('register/', views.UserRegisterView, name='register'),
    
]   