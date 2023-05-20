from django.forms import ModelForm, inlineformset_factory

from modules.finance.chart_of_accounts.models import Analitic

from .models import Finance, FinanceItem


class FinanceForm(ModelForm):
    class Meta:
        model = Finance
        exclude = ()


class FinanceItemForm(ModelForm):

    class Meta:
        model = FinanceItem
        fields = ['finance', 'typemovement', 'account', 'value']
        exclude = ()


FinanceItemFormSet = inlineformset_factory(
    Finance, FinanceItem, form=FinanceItemForm, extra=1)
