from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Review


class Register_Form(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Enter Your Username"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': "Enter Your Password",
        'type': 'password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': "Confirm Your Password",
        'type': 'password'
    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class Review_Form(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': "Write Your Comment Here......"
    }))

    class Meta:
        model = Review
        fields = ['body', 'vote']
        unique_together = [['owner', 'project']]
