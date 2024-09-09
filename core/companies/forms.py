from django import forms
from django.forms import NumberInput, TextInput

from .models import Company


class Company_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Company_Form, self).__init__(*args, **kwargs)

    class Meta:
        model = Company
        fields = ['nameCompany', 'usersNumbers']
        widgets = {
            'nameCompany': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Company Name"
            }),
            'usersNumbers': NumberInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Numbers of Users"
            }),
        }


class Company_toClient_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Company_toClient_Form, self).__init__(*args, **kwargs)

    class Meta:
        model = Company
        fields = ['nameCompany']
        widgets = {
            'nameCompany': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Company Name"
            }),
        }
