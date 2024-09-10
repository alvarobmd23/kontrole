from django import forms
from django.forms import NumberInput, Select, TextInput

from .models import (PaymentTerms, PaymentTermsDays, Person, PersonContact,
                     PersonCustomer, PersonSeller, PersonSupplier)


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
                'style': 'max-width: 80px; min-width: 80px',
                'placeholder': 'How much days to Pay'
            }),
            'paymentTermsPercentage': NumberInput(attrs={
                'max': 100,
                'class': 'form-control paymentTermsPercentageSum',
                'style': 'max-width: 90px; min-width: 90px',
                'placeholder': 'Percentage of value for the day option'
            }),
        }


class PersonContact_Form(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PersonContact_Form, self).__init__(*args, **kwargs)

    class Meta:
        model = PersonContact
        fields = ['contactType', 'contactDescription', 'contactObs']
        widgets = {
            'contactType': Select(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Contact Type"
            }),
            'contactDescription': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Contact Description"
            }),
            'contactObs': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Observation"
            }),
        }


class PersonCustomer_Form(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PersonCustomer_Form, self).__init__(*args, **kwargs)

    class Meta:
        model = PersonCustomer
        fields = [
            'customerFinDiscount',
            'customerPaymentTerms',
            'customerAccount',
            'customerObs']
        widgets = {
            'customerFinDiscount': NumberInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 80px; min-width: 80px',
                'placeholder': 'Financial Discount'
            }),
            'customerPaymentTerms': Select(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Payment Term"
            }),
            'customerAccount': Select(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Account"
            }),
            'customerObs': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px, height: 200px",
                'placeholder': "Observation"
            }),
        }


class PersonSupplier_Form(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PersonSupplier_Form, self).__init__(*args, **kwargs)

    class Meta:
        model = PersonSupplier
        fields = [
            'supllierFinDiscount',
            'supllierPaymentTerms',
            'supllierAccount',
            'supllierObs'
        ]
        widgets = {
            'supllierFinDiscount': NumberInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 80px; min-width: 80px',
                'placeholder': 'Financial Discount'
            }),
            'supllierPaymentTerms': Select(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Payment Term"
            }),
            'supllierAccount': Select(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Account"
            }),
            'supllierObs': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px, height: 200px",
                'placeholder': "Observation"
            }),
        }


class PersonSeller_Form(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PersonSeller_Form, self).__init__(*args, **kwargs)

    class Meta:
        model = PersonSeller
        fields = ['sellerComission', 'sellerObs']
        widgets = {
            'sellerComission': NumberInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 80px; min-width: 80px',
                'placeholder': 'How much days to Pay'
            }),
            'sellerObs': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px, height: 200px",
                'placeholder': "Observation"
            }),
        }


class Person_Form(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(Person_Form, self).__init__(*args, **kwargs)

    class Meta:
        model = Person
        fields = [
            'personType',
            'personName',
            'personTaxpayerRegistration',
            'personAddress',
            'personCity',
            'personState',
            'personCountry',
            'personObs'
        ]
        widgets = {
            'personType': Select(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Person Type"
            }),
            'personName': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Person Name"
            }),
            'personTaxpayerRegistration': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "TaxPayer Number"
            }),
            'personAddress': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Address"
            }),
            'personCity': TextInput(attrs={
                'class': "form-control",
                'placeholder': "City"
            }),
            'personState': TextInput(attrs={
                'class': "form-control",
                'placeholder': "State"
            }),
            'personCountry': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Country"
            }),
            'personObs': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Observation"
            }),
        }
