from django import forms
from django.forms import DateInput, NumberInput, Select, TextInput

from .models import (PaymentTerms, PaymentTermsDays, Person, PersonContact,
                     PersonCustomer, PersonSeller)


class PaymentTerms_Form(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PaymentTerms_Form, self).__init__(*args, **kwargs)

    class Meta:
        model = PaymentTerms
        fields = ['paymentTermDescription', 'paymentTermsPercentageSum']
        widgets = {
            'paymentTermDescription': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Payment Term Description"
            }),
            'paymentTermsPercentageSum': NumberInput(attrs={
                'id': "ptpSum",
                'class': "form-control",
                'style': 'max-width: 125px;',
                'placeholder': 'Payment Term Percentage Sum',
                'readonly': True
            }),
        }


class PaymentTermsDays_Form(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PaymentTermsDays_Form, self).__init__(*args, **kwargs)

    class Meta:
        model = PaymentTermsDays
        fields = ['paymentTermsDay', 'paymentTermsPercentage']
        widgets = {
            'paymentTermsDay': NumberInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 100px; min-width: 70px',
                'placeholder': 'How much days to Pay'
            }),
            'paymentTermsPercentage': NumberInput(attrs={
                'max': 100,
                'class': 'form-control paymentTermsPercentageSum',
                'style': 'max-width: 100px; min-width: 70px',
                'placeholder': 'Percentage of value for the day option'
            }),
        }
