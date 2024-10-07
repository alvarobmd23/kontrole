from typing import Any

from django.contrib import messages
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import (AnaliticAccount_Form, DocumentType_Form, Entry_Form,
                    ItemEntry_Form, SinteticAccount_Form)
from .models import (ACCOUNTS_TYPE, AnaliticAccount, DocumentType, Entry,
                     EntryItem, SinteticAccount)

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


# Document Type


def documentType_list(request):
    template_name = 'documentType/documentType_list.html'
    object = DocumentType.objects.all().filter(company=request.user.company)
    context = {'object_list': object}
    return render(request, template_name, context)


class DocumentType_add(CreateView):
    model = DocumentType
    form_class = DocumentType_Form
    template_name = 'documentType/documentType_form.html'
    success_url = reverse_lazy('finances:documentType_list')

    def form_valid(self, form):
        form_instance = form.save(commit=False)
        form_instance.company = self.request.user.company
        form_instance.user_created = self.request.user
        form_instance.user_updated = self.request.user
        form_instance = form.save()
        messages.success(
            self.request,
            'Document Type successfully added!',
            'alert-success'
        )
        return super(DocumentType_add, self).form_valid(form)


class DocumentType_edit(UpdateView):
    model = DocumentType
    form_class = DocumentType_Form
    template_name = 'documentType/documentType_form.html'
    success_url = reverse_lazy('finances:documentType_list')

    def form_valid(self, form):
        form_instance = form.save(commit=False)
        form_instance.company = self.request.user.company
        form_instance.user_updated = self.request.user
        form_instance = form.save()
        messages.success(
            self.request,
            'Document Type successfully edited!',
            'alert-success'
        )
        return super(DocumentType_edit, self).form_valid(form)


class DocumentType_delete(DeleteView):
    model = DocumentType
    success_url = reverse_lazy('finances:documentType_list')

    def get(self, request, *args, **kwargs):
        context = messages.warning(
            request,
            'Document Type successfully deleted!',
            'alert-warning'
        )
        return self.delete(context, request, *args, **kwargs)


# Entrys Views

def entrys_list(request):
    template_name = 'entrys/entry_list.html'
    object = Entry.objects.all().filter(company=request.user.company)
    context = {'object_list': object}
    return render(request, template_name, context)


def entrys_detail(request, pk):
    template_name = 'entrys/entry_detail.html'
    obj = Entry.objects.filter(company=request.user.company).get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def entrys_add(request):
    template_name = 'entrys/entry_form.html'
    entrys_form = Entry()
    items_entry = inlineformset_factory(
        Entry,
        EntryItem,
        form=ItemEntry_Form,
        extra=0,
        min_num=2,
        validate_min=True,
    )
    if request.method == 'POST':
        form = Entry_Form(
            request.user,
            request.POST,
            instance=entrys_form,
            prefix='main'
        )
        formset = items_entry(
            request.POST,
            instance=entrys_form,
            prefix='itemEntry',
            form_kwargs={'user': request.user}
        )
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            if (form.entryTotalValue ==
                    form.entryTotalCredit ==
                    form.entryTotalDebit):
                form.company = request.user.company
                form.user_created = request.user
                form.user_updated = request.user
                form = form.save()
                formset = formset.save()
                messages.success(request,
                                 'Document added successfully!',
                                 'alert-success'
                                 )
                return HttpResponseRedirect(
                    reverse_lazy('finances:entrys_list')
                )
            else:
                if form.entryTotalCredit != form.entryTotalDebit:
                    form = Entry_Form(request.user,
                                      instance=entrys_form,
                                      prefix='main')
                    messages.warning(
                        request,
                        (
                           'The total Credit amount must equal '
                           'the total Debit amount!'
                        ),
                        'alert-warning')

                else:
                    form = Entry_Form(request.user,
                                      instance=entrys_form,
                                      prefix='main')
                    messages.warning(
                        request,
                        (
                            'The total Value must equal '
                            'the total Credit amount and '
                            'the total Debit amount!'
                        ),
                        'alert-warning'
                    )
        else:
            form = Entry_Form(request.user,
                              instance=entrys_form,
                              prefix='main')
            messages.warning(request, 'Invalid Form!', 'alert-warning')
    else:
        form = Entry_Form(
            request.user,
            instance=entrys_form,
            prefix='main'
        )
        formset = items_entry(
            instance=entrys_form,
            prefix='itemEntry',
            form_kwargs={'user': request.user}
        )
    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


def entrys_edit(request, pk):
    template_name = 'entrys/entry_form.html'
    entrys_form = Entry.objects.filter(
        company=request.user.company).get(pk=pk)
    items_entry = inlineformset_factory(
        Entry,
        EntryItem,
        form=ItemEntry_Form,
        extra=0,
        min_num=2,
        validate_min=True,
    )
    if request.method == 'POST':
        form = Entry_Form(
            request.user,
            request.POST,
            instance=entrys_form,
            prefix='main'
        )
        formset = items_entry(
            request.POST,
            instance=entrys_form,
            prefix='itemEntry',
            form_kwargs={'user': request.user}
        )
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            if (form.entryTotalValue ==
                    form.entryTotalCredit ==
                    form.entryTotalDebit):
                form.company = request.user.company
                form.user_updated = request.user
                form = form.save()
                formset = formset.save()
                messages.success(request,
                                 'Document edited successfully!',
                                 'alert-success'
                                 )
                return HttpResponseRedirect(
                    reverse_lazy('finances:entrys_list')
                )
            else:
                if form.entryTotalCredit != form.entryTotalDebit:
                    form = Entry_Form(request.user,
                                      instance=entrys_form,
                                      prefix='main')
                    messages.warning(
                        request,
                        (
                           'The total Credit amount must equal '
                           'the total Debit amount!'
                        ),
                        'alert-warning')

                else:
                    form = Entry_Form(request.user,
                                      instance=entrys_form,
                                      prefix='main')
                    messages.warning(
                        request,
                        (
                            'The total Value must equal '
                            'the total Credit amount and '
                            'the total Debit amount!'
                        ),
                        'alert-warning'
                    )
        else:
            form = Entry_Form(request.user,
                              instance=entrys_form,
                              prefix='main')
            messages.warning(request, 'Invalid Form!', 'alert-warning')
    else:
        form = Entry_Form(
            request.user,
            instance=entrys_form,
            prefix='main'
        )
        formset = items_entry(
            instance=entrys_form,
            prefix='itemEntry',
            form_kwargs={'user': request.user}
        )
    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


class Entrys_delete(DeleteView):
    model = Entry
    success_url = reverse_lazy('finances:entrys_list')

    def get(self, request, *args, **kwargs):
        context = messages.warning(
            request,
            'Document successfully deleted!',
            'alert-warning'
        )
        return self.delete(context, request, *args, **kwargs)
