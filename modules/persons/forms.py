from django import forms
from django.forms import DateInput, NumberInput, Select, TextInput

from .models import (PaymentTerms, PaymentTermsDays, Person, PersonContact,
                     PersonCustomer, PersonSeller)


class PaymentTerms_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PaymentTerms_Form, self).__init__(*args, **kwargs)

    class Meta:
        model = PaymentTerms
        fields = ['paymentTermDescription']
        widgets = {
            'paymentTermDescription': Select(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Payment Term Description"
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
                'style': 'max-width: 50px',
                'placeholder': 'How much days to Pay'
            }),
            'paymentTermsPercentage': NumberInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 50px',
                'placeholder': 'Percentage of value for the day option'
            }),
        }
