
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Analitic, Sintetic, TypeAccount


def indexview(request):
    company_user = Sintetic.objects.filter(company=request.user.company)
    queryset = company_user.values(
        'company', 'company__company_name', 'typeaccount__typeaccount', 'sintetic', 'analitic__analitic').distinct()
    return render(request, 'chart_of_accounts/chart_of_accounts.html', {'objects': queryset})


class Analitic_New(CreateView):
    model = Analitic
    fields = ['sintetic', 'analitic']

    def get_queryset(self):
        company_user = self.request.user.company
        return Sintetic.objects.filter(company=company_user)

    def form_valid(self, form):
        analitic = form.save(commit=False)
        analitic.company = self.request.user.company
        analitic.save()
        return super(Analitic_New, self).form_valid(form)


class Analitic_Update(UpdateView):
    model = Analitic
    fields = ['sintetic', 'analitic']

    def get_queryset(self):
        company_user = self.request.user.company
        return Analitic.objects.filter(company=company_user)


class Analitic_Delete(DeleteView):
    model = Analitic
    success_url = reverse_lazy('chart_of_account:chart_of_account')

    def get_queryset(self):
        company_user = self.request.user.company
        return Analitic.objects.filter(company=company_user)


class Sintetic_New(CreateView):
    model = Sintetic
    fields = ['typeaccount', 'sintetic']

    def form_valid(self, form):
        sintetic = form.save(commit=False)
        sintetic.company = self.request.user.company
        sintetic.save()
        return super(Sintetic_New, self).form_valid(form)


class Sintetic_Update(UpdateView):
    model = Sintetic
    fields = ['typeaccount', 'sintetic']

    def get_queryset(self):
        company_user = self.request.user.company
        return Sintetic.objects.filter(company=company_user)


class Sintetic_Delete(DeleteView):
    model = Sintetic
    success_url = reverse_lazy('chart_of_account:chart_of_account')

    def get_queryset(self):
        company_user = self.request.user.company
        return Sintetic.objects.filter(company=company_user)
