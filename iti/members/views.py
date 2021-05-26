import django
from django.contrib.auth import forms
from django.forms.forms import Form
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import MyAuthForm, SignUpForm
from django.contrib.auth.views import LoginView


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registeration.html'
    success_url = reverse_lazy('login') 




class MyLoginView(LoginView):
   authentication_form = MyAuthForm