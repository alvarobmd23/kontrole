from typing import Any

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Person


class Persons_List(ListView):
    model = Person
    paginate_by = 50

    def get_queryset(self):
        company_user = self.request.user.company
        return Person.objects.filter(company=company_user)


class Persons_New(CreateView):
    model = Person
    fields = ['name', 'nickname', 'typeperson', 'cpfcnpj',
              'address', 'city', 'country', 'phone', 'email', 'obs']

    def form_valid(self, form):
        person = form.save(commit=False)
        person.company = self.request.user.company
        person.save()
        return super(Persons_New, self).form_valid(form)


class Persons_Update(UpdateView):
    model = Person
    fields = ['name', 'nickname', 'typeperson', 'cpfcnpj',
              'address', 'city', 'country', 'phone', 'email', 'obs']

    def get_queryset(self):
        company_user = self.request.user.company
        return Person.objects.filter(company=company_user)


class Persons_Delete(DeleteView):
    model = Person
    success_url = reverse_lazy('persons:persons')

    def get_queryset(self):
        company_user = self.request.user.company
        return Person.objects.filter(company=company_user)
