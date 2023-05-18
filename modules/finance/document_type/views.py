from typing import Any

from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Document_Type


class Document_Type_List(ListView):
    model = Document_Type
    paginate_by = 50

    def get_queryset(self):
        company_user = self.request.user.company
        return Document_Type.objects.filter(company=company_user)


class Document_Type_New(CreateView):
    model = Document_Type
    fields = ['document_type']

    def form_valid(self, form):
        document_type = form.save(commit=False)
        document_type.company = self.request.user.company
        document_type.save()
        messages.success(
            self.request, 'Tipo de Documento criado com sucesso!', 'alert-success')
        return super(Document_Type_New, self).form_valid(form)


class Document_Type_Update(UpdateView):
    model = Document_Type
    fields = ['document_type']

    def form_valid(self, form):
        document_type = form.save(commit=False)
        document_type.company = self.request.user.company
        document_type.save()
        messages.success(
            self.request, 'Tipo de Documento modificado com sucesso!', 'alert-success')
        return super(Document_Type_Update, self).form_valid(form)


class Document_Type_Delete(DeleteView):
    model = Document_Type
    success_url = reverse_lazy('document_type:document_type')

    def get_queryset(self):
        company_user = self.request.user.company
        return Document_Type.objects.filter(company=company_user)
