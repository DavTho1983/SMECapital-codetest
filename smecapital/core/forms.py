from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import User


class SignUpForm(UserCreationForm, ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2', )