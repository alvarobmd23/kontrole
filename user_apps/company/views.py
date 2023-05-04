from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Company


class NewCompany(CreateView):
    model = Company
    fields = ('company_name', 'company_nickname')
