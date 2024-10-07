from django import forms
from django.forms import DateInput, NumberInput, Select, TextInput

from .models import (AnaliticAccount, DocumentType, Entry, EntryItem,
                     SinteticAccount)

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
                'class': "form-select",
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
                'class': "form-select",
                'style': "max-width: 300px",
                'placeholder': "Sintetic Account"
            }),
            'analiticName': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Analitic Name"
            }),
        }


# DOCUMENT TYPE FORM
class DocumentType_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DocumentType_Form, self).__init__(*args, **kwargs)

    class Meta:
        model = DocumentType
        fields = ['documentTypeDescription']
        widgets = {
            'documentTypeDescription': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Document Type"
            }),
        }


# ENTRY FORM
class Entry_Form(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(Entry_Form, self).__init__(*args, **kwargs)
        self.fields['entryDocumentType'].queryset = (
            DocumentType.objects.filter(company=user.company).
            order_by('documentTypeDescription')
        )

    class Meta:
        model = Entry
        fields = [
            'entryDate',
            'entryDocumentType',
            'entryNumDocument',
            'entryTotalValue',
            'entryDescription',
            'entryObs',
            'entryTotalCredit',
            'entryTotalDebit'
            ]
        widgets = {
            'entryDate': DateInput(attrs={
                'class': "form-control",
                'style': "max-width: 200px",
            }),
            'entryDocumentType': Select(attrs={
                'class': "form-select",
                'style': "max-width: 200px",
                'placeholder': "Document Type"
            }),
            'entryNumDocument': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': "Document Number"
            }),
            'entryTotalValue': NumberInput(attrs={
                'class': "form-control vlSum",
                'style': "max-width: 200px",
                'placeholder': "Document Value"
            }),
            'entryDescription': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 600px",
                'placeholder': "Description"
            }),
            'entryObs': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 600px",
                'placeholder': "Observation"
            }),
            'entryTotalCredit': NumberInput(attrs={
                'class': "form-control cSum",
                'style': "max-width: 200px; display: none",
                'placeholder': "Credit Value",
                'readonly': True
            }),
            'entryTotalDebit': NumberInput(attrs={
                'class': "form-control dSum",
                'style': "max-width: 200px; display: none",
                'placeholder': "Debit Value",
                'readonly': True
            }),
        }


class ItemEntry_Form(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ItemEntry_Form, self).__init__(*args, **kwargs)
        self.fields['itemEntryAccount'].queryset = (
            AnaliticAccount.objects.filter(company=user.company).
            order_by(
                'sinteticAccounts',
            )
        )

    class Meta:
        model = EntryItem
        fields = [
            'itemEntryAccount',
            'itemEntryType',
            'itemEntryValue',
            'itemEntryValueRef'
            ]
        widgets = {
            'itemEntryAccount': Select(attrs={
                'class': "account select2",
                'style': "max-width: 300px",
                'placeholder': "Account"
            }),
            'itemEntryType': Select(attrs={
                'class': "form-select account",
                'style': "max-width: 300px",
                'placeholder': "Account Type"
            }),
            'itemEntryValue': NumberInput(attrs={
                'class': "form-control itemvlSum account",
                'style': "max-width: 200px",
                'placeholder': "Value"
            }),
            'itemEntryValueRef': NumberInput(attrs={
                'class': "form-control valueRef",
                'style': "max-width: 200px; display: none",
                'placeholder': "Value Ref",
                'readonly': True
            }),
        }
