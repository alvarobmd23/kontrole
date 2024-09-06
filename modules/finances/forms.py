from django import forms
from django.forms import DateInput, NumberInput, Select, TextInput

from .models import AnaliticAccount, SinteticAccount

# CHART OF ACCOUNTS


class SinteticAccount_Form(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SinteticAccount_Form, self).__init__(*args, **kwargs)

    class Meta:
        model = SinteticAccount
        fields = ['accountsType', 'sinteticName']
        widgets = {
            'accountsType': Select(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Account Type"
            }),
            'sinteticName': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Sintetic Name"
            }),
        }


class AnaliticAccount_Form(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(AnaliticAccount_Form, self).__init__(*args, **kwargs)
        self.fields['sinteticAccounts'].queryset = (
            SinteticAccount.objects.filter(company=user.company).
            order_by('accountsType', 'sinteticName')
        )

    class Meta:
        model = AnaliticAccount
        fields = ['sinteticAccounts', 'analiticName']
        widgets = {
            'sinteticAccounts': Select(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Sintetic Account"
            }),
            'analiticName': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Analitic Name"
            }),
        }
