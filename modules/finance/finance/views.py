from django.contrib import messages
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import FinanceItemFormSet
from .models import Finance


class FinanceList(ListView):
    model = Finance

    def get_queryset(self):
        company_user = self.request.user.company
        return Finance.objects.filter(company=company_user)


class FinanceCreate(CreateView):
    model = Finance
    fields = ['date', 'document_type', 'n_doc',
              'description', 'total_value', 'obs']

    def form_valid(self, form):
        finance = form.save(commit=False)
        finance.company = self.request.user.company
        finance.save()
        messages.success(
            self.request, 'Lançamento criado com sucesso!', 'alert-success')
        return super(FinanceCreate, self).form_valid(form)


class FinanceFinanceItemCreate(CreateView):
    model = Finance
    fields = ['date', 'document_type', 'n_doc',
              'description', 'total_value', 'obs']
    success_url = reverse_lazy('finance:finance-list')

    def get_context_data(self, **kwargs):
        data = super(FinanceFinanceItemCreate,
                     self).get_context_data(**kwargs)
        if self.request.POST:
            data['financeitems'] = FinanceItemFormSet(self.request.POST)
        else:
            data['financeitems'] = FinanceItemFormSet()
        return data

    def form_valid(self, form):
        finance = form.save(commit=False)
        finance.company = self.request.user.company
        context = self.get_context_data()
        financeitems = context['financeitems']
        with transaction.atomic():
            self.object = form.save()
            if financeitems.is_valid():
                financeitems.instance = self.object
                financeitems.save()

        return super(FinanceFinanceItemCreate, self).form_valid(form)


class FinanceUpdate(UpdateView):
    model = Finance
    success_url = '/'
    fields = ['date', 'document_type', 'n_doc',
              'description', 'total_value', 'obs']

    def form_valid(self, form):
        finance = form.save(commit=False)
        finance.company = self.request.user.company
        finance.save()
        messages.success(
            self.request, 'Lançamento modificado com sucesso!', 'alert-success')
        return super(FinanceUpdate, self).form_valid(form)


class FinanceFinanceItemUpdate(UpdateView):
    model = Finance
    fields = ['date', 'document_type', 'n_doc',
              'description', 'total_value', 'obs']
    success_url = reverse_lazy('finance:finance-list')

    def get_context_data(self, **kwargs):
        data = super(FinanceFinanceItemUpdate,
                     self).get_context_data(**kwargs)
        if self.request.POST:
            data['financeitems'] = FinanceItemFormSet(
                self.request.POST, instance=self.object)
        else:
            data['financeitems'] = FinanceItemFormSet(
                instance=self.object)
        return data

    def form_valid(self, form):
        finance = form.save(commit=False)
        finance.company = self.request.user.company
        context = self.get_context_data()
        financeitems = context['financeitems']
        with transaction.atomic():
            self.object = form.save()

            if financeitems.is_valid():
                financeitems.instance = self.object
                financeitems.save()

        finance.save()
        return super(FinanceFinanceItemUpdate, self).form_valid(form)


class FinanceDelete(DeleteView):
    model = Finance
    success_url = reverse_lazy('finance:finance-list')

    def get_queryset(self):
        company_user = self.request.user.company
        return Finance.objects.filter(company=company_user)
