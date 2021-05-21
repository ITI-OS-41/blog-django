from django import forms
from django.forms import widgets
from opensource.models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        
        fields = ( 'title', 'content', 'category', )
        # # fields = '__all__'
        # widgets = {
        #     'fname': forms.TextInput(attrs={'class': 'form-control'}),
        #     'lname': forms.TextInput(attrs={'class': 'form-control'}),
        #     'age': forms.TextInput(attrs={'class': 'form-control'})
        # }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)

        # fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
          