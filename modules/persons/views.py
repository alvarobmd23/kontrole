from django.contrib import messages
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .forms import (PaymentTerms_Form, PaymentTermsDays_Form, Person_Form,
                    PersonContact_Form, PersonCustomer_Form,
                    PersonSupplier_Form)
from .models import (PaymentTerms, PaymentTermsDays, Person, PersonContact,
                     PersonCustomer, PersonSupplier)

# Payment Terms Views


def paymentTerms_list(request):
    template_name = 'paymentTerms/paymentTerms_list.html'
    object = PaymentTerms.objects.all().filter(company=request.user.company)
    context = {'object_list': object}
    return render(request, template_name, context)


def paymentTerms_detail(request, pk):
    template_name = 'paymentTerms/paymentTerms_detail.html'
    obj = PaymentTerms.objects.filter(company=request.user.company).get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def paymentTerms_add(request):
    template_name = 'paymentTerms/paymentTerms_form.html'
    paymentTerms_form = PaymentTerms()
    days_paymentTerms = inlineformset_factory(
        PaymentTerms,
        PaymentTermsDays,
        form=PaymentTermsDays_Form,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form = PaymentTerms_Form(
            request.user,
            request.POST,
            instance=paymentTerms_form,
            prefix='main'
        )
        formset = days_paymentTerms(
            request.POST,
            instance=paymentTerms_form,
            prefix='paymentTerms',
            form_kwargs={'user': request.user}
        )
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            if form.paymentTermsPercentageSum == 100:
                form.company = request.user.company
                form.user_created = request.user
                form.user_updated = request.user
                form = form.save()
                formset = formset.save()
                messages.success(request,
                                 'Item added successfully!',
                                 'alert-success'
                                 )
                return HttpResponseRedirect(
                    reverse_lazy('persons:paymentTerms')
                    )
            else:
                form = PaymentTerms_Form(
                    request.user,
                    instance=paymentTerms_form,
                    prefix='main'
                )
                messages.warning(request,
                                 'The total percentage needs to be 100%!',
                                 'alert-warning'
                                 )
        else:
            form = PaymentTerms_Form(
                request.user,
                instance=paymentTerms_form,
                prefix='main'
            )
            messages.warning(
                request,
                'Invalid form',
                'alert-warning'
            )
    else:
        form = PaymentTerms_Form(
            request.user,
            instance=paymentTerms_form,
            prefix='main'
        )
        formset = days_paymentTerms(
            instance=paymentTerms_form,
            prefix='paymentTerms',
            form_kwargs={'user': request.user}
        )
    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


def paymentTerms_edit(request, pk):
    template_name = 'paymentTerms/paymentTerms_form.html'
    paymentTerms_form = PaymentTerms.objects.filter(
        company=request.user.company).get(pk=pk)
    days_paymentTerms = inlineformset_factory(
        PaymentTerms,
        PaymentTermsDays,
        form=PaymentTermsDays_Form,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form = PaymentTerms_Form(
            request.user,
            request.POST,
            instance=paymentTerms_form,
            prefix='main'
        )
        formset = days_paymentTerms(
            request.POST,
            instance=paymentTerms_form,
            prefix='paymentTerms',
            form_kwargs={'user': request.user}
        )
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            if form.paymentTermsPercentageSum == 100:
                form.company = request.user.company
                form.user_updated = request.user
                form = form.save()
                formset = formset.save()
                messages.success(request,
                                 'Item edited successfully!',
                                 'alert-success'
                                 )
                return HttpResponseRedirect(
                    reverse_lazy('persons:paymentTerms')
                    )
            else:
                form = PaymentTerms_Form(
                    request.user,
                    instance=paymentTerms_form,
                    prefix='main'
                )
                messages.warning(request,
                                 'The total percentage needs to be 100%!',
                                 'alert-warning'
                                 )
        else:
            form = PaymentTerms_Form(
                request.user,
                instance=paymentTerms_form,
                prefix='main'
            )
            formset = days_paymentTerms(
                instance=paymentTerms_form,
                prefix='paymentTerms',
                form_kwargs={'user': request.user}
            )
            messages.warning(
                request,
                'Invalid form',
                'alert-warning'
            )
    else:
        form = PaymentTerms_Form(
            request.user,
            instance=paymentTerms_form,
            prefix='main'
        )
        formset = days_paymentTerms(
            instance=paymentTerms_form,
            prefix='paymentTerms',
            form_kwargs={'user': request.user}
        )
    context = {
        'form': form,
        'formset': formset,
        'object': paymentTerms_form,
        'formset_errors': formset.errors,
    }
    return render(request, template_name, context)


class PaymentTerms_Delete(DeleteView):
    model = PaymentTerms
    success_url = reverse_lazy('persons:paymentTerms')

    def get(self, request, *args, **kwargs):
        context = messages.warning(
            request,
            'Payment Term successfully deleted!',
            'alert-warning'
        )
        return self.delete(context, request, *args, **kwargs)


# Persons Views

def persons_list(request):
    template_name = 'persons/persons_list.html'
    object = Person.objects.all().filter(company=request.user.company)
    context = {'object_list': object}
    return render(request, template_name, context)


def persons_detail(request, pk):
    template_name = 'persons/persons_detail.html'
    obj = Person.objects.filter(company=request.user.company).get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def persons_add(request):
    template_name = 'persons/persons_form.html'
    persons_form = Person()
    contact_form = inlineformset_factory(
        Person,
        PersonContact,
        form=PersonContact_Form,
        extra=1,
        min_num=0,
        validate_min=True,
    )
    supplier_form = inlineformset_factory(
        Person,
        PersonSupplier,
        form=PersonSupplier_Form,
        extra=1,
        min_num=0,
        max_num=1,
        validate_min=True,
        validate_max=True,
    )
    customer_form = inlineformset_factory(
        Person,
        PersonCustomer,
        form=PersonCustomer_Form,
        extra=1,
        min_num=0,
        max_num=1,
        validate_min=True,
        validate_max=True,
    )
    if request.method == 'POST':
        form = Person_Form(
            request.user,
            request.POST,
            instance=persons_form,
            prefix='main'
        )
        contactformset = contact_form(
            request.POST,
            instance=persons_form,
            prefix='contact',
            form_kwargs={'user': request.user}
        )
        supplierformset = supplier_form(
            request.POST,
            instance=persons_form,
            prefix='supplier',
            form_kwargs={'user': request.user}
        )
        customerformset = customer_form(
            request.POST,
            instance=persons_form,
            prefix='customer',
            form_kwargs={'user': request.user}
        )
        if (
            form.is_valid() and
            contactformset.is_valid() and
            supplierformset.is_valid() and
            customerformset.is_valid()
        ):
            form = form.save(commit=False)
            form.company = request.user.company
            form.user_created = request.user
            form.user_updated = request.user
            form = form.save()
            contactformset = contactformset.save()
            supplierformset = supplierformset.save()
            customerformset = customerformset.save()
            messages.success(
                request,
                'Person added successfully!',
                'alert-success'
            )
            return HttpResponseRedirect(
                reverse_lazy('persons:persons_list')
            )
        else:
            form = Person_Form(
                request.user,
                instance=persons_form,
                prefix='main'
            )
            if any(contactformset.errors):
                messages.warning(
                    request,
                    'Check contacts table!',
                    'alert-warning'
                )
            if any(supplierformset.errors):
                messages.warning(
                    request,
                    'Check supplier table!',
                    'alert-warning'
                )
            if any(customerformset.errors):
                messages.warning(
                    request,
                    'Check customer table!',
                    'alert-warning'
                )
    else:
        form = Person_Form(
            request.user,
            instance=persons_form,
            prefix='main'
        )
        contactformset = contact_form(
            instance=persons_form,
            prefix='contact',
            form_kwargs={'user': request.user}
        )
        supplierformset = supplier_form(
            instance=persons_form,
            prefix='supplier',
            form_kwargs={'user': request.user}
        )
        customerformset = customer_form(
            instance=persons_form,
            prefix='customer',
            form_kwargs={'user': request.user}
        )
    context = {
        'form': form,
        'contactformset': contactformset,
        'supplierformset': supplierformset,
        'customerformset': customerformset,
    }
    return render(request, template_name, context)


def persons_edit(request, pk):
    template_name = 'persons/persons_form.html'
    persons_form = Person.objects.filter(
        company=request.user.company).get(pk=pk)
    contact_form = inlineformset_factory(
        Person,
        PersonContact,
        form=PersonContact_Form,
        extra=1,
        min_num=0,
        validate_min=True,
    )
    supplier_form = inlineformset_factory(
        Person,
        PersonSupplier,
        form=PersonSupplier_Form,
        extra=1,
        min_num=0,
        max_num=1,
        validate_min=True,
        validate_max=True,
    )
    customer_form = inlineformset_factory(
        Person,
        PersonCustomer,
        form=PersonCustomer_Form,
        extra=1,
        min_num=0,
        max_num=1,
        validate_min=True,
        validate_max=True,
    )
    if request.method == 'POST':
        form = Person_Form(
            request.user,
            request.POST,
            instance=persons_form,
            prefix='main'
        )
        contactformset = contact_form(
            request.POST,
            instance=persons_form,
            prefix='contact',
            form_kwargs={'user': request.user}
        )
        supplierformset = supplier_form(
            request.POST,
            instance=persons_form,
            prefix='supplier',
            form_kwargs={'user': request.user}
        )
        customerformset = customer_form(
            request.POST,
            instance=persons_form,
            prefix='customer',
            form_kwargs={'user': request.user}
        )
        if (
            form.is_valid() and
            contactformset.is_valid() and
            supplierformset.is_valid() and
            customerformset.is_valid()
        ):
            form = form.save(commit=False)
            form.company = request.user.company
            form.user_created = request.user
            form.user_updated = request.user
            form = form.save()
            contactformset = contactformset.save()
            supplierformset = supplierformset.save()
            customerformset = customerformset.save()
            messages.success(
                request,
                'Person edited successfully!',
                'alert-success'
            )
            return HttpResponseRedirect(
                reverse_lazy('persons:persons_list')
            )
        else:
            form = Person_Form(
                request.user,
                instance=persons_form,
                prefix='main'
            )
            if any(contactformset.errors):
                messages.warning(
                    request,
                    'Check contacts table!',
                    'alert-warning'
                )
            if any(supplierformset.errors):
                messages.warning(
                    request,
                    'Check supplier table!',
                    'alert-warning'
                )
            if any(customerformset.errors):
                messages.warning(
                    request,
                    'Check customer table!',
                    'alert-warning'
                )
    else:
        form = Person_Form(
            request.user,
            instance=persons_form,
            prefix='main'
        )
        contactformset = contact_form(
            instance=persons_form,
            prefix='contact',
            form_kwargs={'user': request.user}
        )
        supplierformset = supplier_form(
            instance=persons_form,
            prefix='supplier',
            form_kwargs={'user': request.user}
        )
        customerformset = customer_form(
            instance=persons_form,
            prefix='customer',
            form_kwargs={'user': request.user}
        )

    def has_filled_forms(formset):
        for form in formset:
            if form.has_changed() and not form.empty_permitted:
                return True
        return False

    supplier_filled_forms = has_filled_forms(supplierformset)
    customer_filled_forms = has_filled_forms(customerformset)

    context = {
        'form': form,
        'contactformset': contactformset,
        'supplierformset': supplierformset,
        'supplier_filled_forms': supplier_filled_forms,
        'customerformset': customerformset,
        'customer_filled_forms': customer_filled_forms,
    }
    return render(request, template_name, context)


class Persons_Delete(DeleteView):
    model = Person
    success_url = reverse_lazy('persons:persons_list')

    def get(self, request, *args, **kwargs):
        context = messages.warning(
            request,
            'Person successfully deleted!',
            'alert-warning'
        )
        return self.delete(context, request, *args, **kwargs)
