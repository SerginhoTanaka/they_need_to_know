from django.db import models
from django import forms
from login.models import User


class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }