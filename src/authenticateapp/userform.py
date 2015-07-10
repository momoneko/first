from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password1', max_length=100)

    class Meta:
        model = User
        fields = [
            'username', 'password',
            'email', 'first_name', 'last_name'
        ]
