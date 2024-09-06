from typing import Any

from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import AnaliticAccount_Form, SinteticAccount_Form
from .models import ACCOUNTS_TYPE, AnaliticAccount, SinteticAccount

# CHART OF ACCOUNTS - LIST


def chartOfAccounts_list(request):
    template_name = 'chartOfAccounts/chartOfAccounts_list.html'
    accountobject = (
        ACCOUNTS_TYPE
    )
    analiticobject = (
        AnaliticAccount.objects.all().
        filter(company=request.user.company).
        order_by('analiticName',)
    )
    sinteticobject = (
        SinteticAccount.objects.all().
        filter(company=request.user.company).
        order_by('sinteticName',)
    )
    context = (
        {
            'sinteticobject': sinteticobject,
            'analiticobject': analiticobject,
            'accountobject': accountobject
        }
    )
    return render(request, template_name, context)


# CHART OF ACCOUNTS - Sintetic Account

class Sintetic_add(CreateView):
    model = SinteticAccount
    form_class = SinteticAccount_Form
    template_name = 'chartOfAccounts/sinteticAccounts_form.html'

    def get_form_kwargs(self):
        kwargs = super(Sintetic_add, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        sintetic = form.save(commit=False)
        sintetic.company = self.request.user.company
        sintetic.user_created = self.request.user
        sintetic.user_updated = self.request.user
        sintetic = form.save()
        messages.success(
            self.request,
            'Sintetic Account added successfully!',
            'alert-success'
        )
        return super(Sintetic_add, self).form_valid(form)


class Sintetic_edit(UpdateView):
    model = SinteticAccount
    form_class = SinteticAccount_Form
    template_name = 'chartOfAccounts/sinteticAccounts_form.html'

    def get_form_kwargs(self):
        kwargs = super(Sintetic_edit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        sintetic = form.save(commit=False)
        sintetic.user_updated = self.request.user
        sintetic = form.save()
        messages.success(
            self.request,
            'Sintetic Account successfully modified!',
            'alert-success'
        )
        return super(Sintetic_edit, self).form_valid(form)


class Sintetic_delete(DeleteView):
    model = SinteticAccount
    success_url = reverse_lazy('finances:chartOfAccounts')

    def get(self, request, *args, **kwargs):
        context = messages.warning(
            request,
            'Sintetic Account successfully deleted!',
            'alert-warning'
        )
        return self.delete(context, request, *args, **kwargs)

    def get_queryset(self):
        company_user = self.request.user.company
        return SinteticAccount.objects.filter(company=company_user)


# CHART OF ACCOUNTS - Analitic Account

class Analitic_add(CreateView):
    model = AnaliticAccount
    form_class = AnaliticAccount_Form
    template_name = 'chartOfAccounts/analiticAccounts_form.html'

    def get_form_kwargs(self):
        kwargs = super(Analitic_add, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        analitic = form.save(commit=False)
        analitic.company = self.request.user.company
        analitic.user_created = self.request.user
        analitic.user_updated = self.request.user
        analitic = form.save()
        messages.success(
            self.request,
            'Analitic Account added successfully!',
            'alert-success'
        )
        return super(Analitic_add, self).form_valid(form)


class Analitic_edit(UpdateView):
    model = AnaliticAccount
    form_class = AnaliticAccount_Form
    template_name = 'chartOfAccounts/analiticAccounts_form.html'

    def get_form_kwargs(self):
        kwargs = super(Analitic_edit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        analitic = form.save(commit=False)
        analitic.user_updated = self.request.user
        analitic = form.save()
        messages.success(
            self.request,
            'Analitic Account successfully modified!',
            'alert-success'
        )
        return super(Analitic_edit, self).form_valid(form)


class Analitic_delete(DeleteView):
    model = AnaliticAccount
    success_url = reverse_lazy('finances:chartOfAccounts')

    def get(self, request, *args, **kwargs):
        context = messages.warning(
            request,
            'Analitic Account successfully deleted!',
            'alert-warning'
        )
        return self.delete(context, request, *args, **kwargs)

    def get_queryset(self):
        company_user = self.request.user.company
        return AnaliticAccount.objects.filter(company=company_user)
