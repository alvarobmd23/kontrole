from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Chart_of_Accounts_Sintetico, ClassificationAccount


class ClassificationAccount_List(ListView):
    model = ClassificationAccount
    template_name = "chart_of_accounts/classificationaccount_List.html"
    paginate_by = 50

    def get_queryset(self):
        company_user = self.request.user.company
        return ClassificationAccount.objects.filter(company=company_user)


class Chart_of_Accounts_Sintetico_List(ListView):
    model = Chart_of_Accounts_Sintetico
    paginate_by = 50

    def get_queryset(self):
        company_user = self.request.user.company
        return Chart_of_Accounts_Sintetico.objects.filter(company=company_user)


class Chart_of_Accounts_Sintetico_New(CreateView):
    model = Chart_of_Accounts_Sintetico
    fields = ['mother_account', 'sintetic_account']

    def form_valid(self, form):
        Chart_of_Accounts_Sintetico = form.save(commit=False)
        Chart_of_Accounts_Sintetico.company = self.request.user.company
        Chart_of_Accounts_Sintetico.save()
        return super(Chart_of_Accounts_Sintetico_New, self).form_valid(form)


class Chart_of_Accounts_Sintetico_Update(UpdateView):
    model = Chart_of_Accounts_Sintetico
    fields = ['mother_account', 'sintetic_account']


class Chart_of_Accounts_Sintetico_Delete(DeleteView):
    model = Chart_of_Accounts_Sintetico
    success_url = reverse_lazy('chart_of_accounts:chart_of_accounts_list')
