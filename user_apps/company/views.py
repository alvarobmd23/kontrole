from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView

from modules.finance.chart_of_accounts.models import TypeAccount
from modules.finance.document_type.models import Document_Type

from .models import Company


class NewCompany(CreateView):
    model = Company
    fields = ('company_name', 'company_nickname')

    def form_valid(self, form):
        obj = form.save()
        user_new = self.request.user
        user_new.company = obj
        user_new.save()
        a = TypeAccount(company=obj, typeaccount='1. ATIVO')
        a.save()
        b = TypeAccount(company=obj, typeaccount='2. PASSIVO')
        b.save()
        c = TypeAccount(company=obj, typeaccount='3. RECEITAS')
        c.save()
        d = TypeAccount(company=obj, typeaccount='4. DESPESAS E CUSTOS')
        d.save()
        e = Document_Type(company=obj, document_type='Nota Fiscal')
        e.save()
        f = Document_Type(company=obj, document_type='Recibo')
        f.save()
        g = Document_Type(company=obj, document_type='Duplicata')
        g.save()
        h = Document_Type(company=obj, document_type='Boleto')
        h.save()
        return redirect('dashboard:dashboard')


class EditCompany(UpdateView):
    model = Company
    fields = ('company_name', 'company_nickname')

    def get_object(self):
        return self.request.user.company
