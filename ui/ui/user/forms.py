from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import sign

#Create your forms here

class signForm(forms.ModelForm):
    class Meta:
        model = sign
        fields = [
            'Phone',
            'Age',
            'Gender'
        ]
