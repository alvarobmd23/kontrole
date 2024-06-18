from django import forms
from django.forms import inlineformset_factory

from .models import Person, PersonContact


class PersonForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['document_type'].queryset = Document_Type.objects.filter(
            company=user.company)

    class Meta:
        model = Person
