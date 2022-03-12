from datetime import date
from email.policy import default
from django import forms
from . models import Student

class Studentinfo(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','standard','email','password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control '}),
            'standard':forms.TextInput(attrs={'class':'form-control '}),
            'email':forms.EmailInput(attrs={'class':'form-control '}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
            
        }
