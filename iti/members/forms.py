from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm): 
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs) 

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'




#class MyAuthForm(AuthenticationForm):
#    error_messages = {
#        'invalid_login': (
#            "Please enter a correct %(username)s and password."
#        ),
#        'inactive': ("This account is inactive."),
#    }
#
#    def confirm_login_allowed(self, user):
#
#        if not user.is_active:
#            raise forms.ValidationError(
#                self.error_messages['inactive'],
#                code='inactive',
#            )
#
#    def get_user(self):
#        return self.user_cache
#
#    def get_invalid_login_error(self):
#        return forms.ValidationError(
#            self.error_messages['invalid_login'],
#            code='invalid_login',
#            params={'username': self.username_field.verbose_name},
#        )
   
  