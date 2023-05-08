from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView

from .models import Company


class NewCompany(CreateView):
    model = Company
    fields = ('company_name', 'company_nickname')

    def form_valid(self, form):
        obj = form.save()
        user_new = self.request.user
        user_new.company = obj
        user_new.save()
        return redirect('dashboard:dashboard')


class EditCompany(UpdateView):
    model = Company
    fields = ('company_name', 'company_nickname')

    def get_object(self):
        return self.request.user.company
