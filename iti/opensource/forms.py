from django import forms
from django.forms import widgets
from opensource.models import Post, Category, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        
        fields = ( 'title', 'content', 'category','tags' )
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
          
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                    'rows': '2',
                    'placeholder': 'Join the discussion and leave a comment!',
                    },
                ),
        }
    