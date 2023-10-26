from django.db import models
from django import forms
from login.models import User


class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','name', 'email', 'password']
