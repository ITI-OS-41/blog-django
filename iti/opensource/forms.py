from django import forms
from django.forms import widgets
from opensource.models import Student, Track

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ( 'fname', 'lname', 'age', 'student_track' )
        # fields = '__all__'
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'})
        }
        
class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('name',)

        # fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
          