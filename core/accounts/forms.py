from django import forms
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.forms import (EmailInput, NumberInput, PasswordInput, Select,
                          TextInput)

from .models import AUser


class AUser_Form(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=PasswordInput(attrs={
            'class': "form-control",
            'style': "max-width: 300px",
            'placeholder': "Confirm your Password"
        })
    )

    class Meta:
        model = AUser
        fields = ['username', 'email', 'password', 'company', 'hierarchy']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 400",
                'placeholder': "UserName"
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': "max-width: 600px",
                'placeholder': "E-mail"
            }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Password"
            }),
            'company': Select(attrs={
                'class': "form-control",
                'style': "max-width: 200px",
                'placeholder': "Select the User's Company"
            }),
            'hierarchy': NumberInput(attrs={
                'class': "form-control",
                'style': "max-width: 150px",
                'placeholder': "Hierarchy Level"
            }),
        }


class AUser_toClient_Form(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=PasswordInput(attrs={
            'class': "form-control",
            'style': "max-width: 300px",
            'placeholder': "Confirm your Password"
        })
    )

    class Meta:
        model = AUser
        fields = ['username', 'email', 'password']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 400",
                'placeholder': "UserName"
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': "max-width: 600px",
                'placeholder': "E-mail"
            }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Password"
            }),
        }


class AUser_toUser_Form(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=PasswordInput(attrs={
            'class': "form-control",
            'style': "max-width: 300px",
            'placeholder': "Confirm your Password"
        })
    )

    class Meta:
        model = AUser
        fields = ['password']
        widgets = {
            'password': PasswordInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Password"
            }),
        }
