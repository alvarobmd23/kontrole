from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, UpdateView

from core.main.decorators import hierarchy_is_1, hierarchy_is_2

from .forms import Company_Form, Company_toClient_Form
from .models import Company


@hierarchy_is_1
def company_list(request):
    template_name = 'company_list.html'
    object = Company.objects.all()
    context = {'object_list': object}
    return render(request, template_name, context)


@method_decorator(hierarchy_is_1, name='dispatch')
class Company_add(CreateView):
    model = Company
    form_class = Company_Form
    template_name = 'company_form.html'
    success_url = reverse_lazy('company:companies')

    def form_valid(self, form):
        messages.success(
            self.request,
            'Company successfully added!',
            'alert-success'
        )
        return super(Company_add, self).form_valid(form)


@method_decorator(hierarchy_is_1, name='dispatch')
class Company_edit(UpdateView):
    model = Company
    form_class = Company_Form
    template_name = 'company_form.html'
    success_url = reverse_lazy('company:companies')

    def form_valid(self, form):
        messages.success(
            self.request,
            'Company successfully modified!',
            'alert-success'
        )
        return super(Company_edit, self).form_valid(form)


@method_decorator(hierarchy_is_2, name='dispatch')
class Company_toClient_edit(UpdateView):
    model = Company
    form_class = Company_toClient_Form
    template_name = 'company_form_to_client.html'
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        messages.success(
            self.request,
            'Company Name successfully modified!',
            'alert-success'
        )
        return super(Company_toClient_edit, self).form_valid(form)


@method_decorator(hierarchy_is_1, name='dispatch')
class Company_delete(DeleteView):
    model = Company
    success_url = reverse_lazy('company:companies')

    def get(self, request, *args, **kwargs):
        context = messages.warning(
            request,
            'Company successfully deleted!',
            'alert-warning'
        )
        return self.delete(context, request, *args, **kwargs)
