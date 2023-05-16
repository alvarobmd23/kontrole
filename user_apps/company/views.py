from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView

from modules.finance.chart_of_accounts.models import TypeAccount

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
        p = TypeAccount(company=obj, typeaccount='2. PASSIVO')
        p.save()
        r = TypeAccount(company=obj, typeaccount='3. RECEITAS')
        r.save()
        d = TypeAccount(company=obj, typeaccount='4. DESPESAS E CUSTOS')
        d.save()
        return redirect('dashboard:dashboard')


class EditCompany(UpdateView):
    model = Company
    fields = ('company_name', 'company_nickname')

    def get_object(self):
        return self.request.user.company
