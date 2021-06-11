import django
from django.contrib.auth import forms
from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm, AuthFormCheckStatus
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView




def UserRegisterView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/registeration.html', {'form': form})


# def UserLogin

# class UserRegisterView(generic.CreateView):
#     form_class = SignUpForm
#     template_name = 'registration/registeration.html'
#     success_url = reverse_lazy('login') 


# for inactive user

class MyLoginView(LoginView):
   authentication_form = AuthFormCheckStatus
