from django.contrib import messages
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .forms import PaymentTerms_Form, PaymentTermsDays_Form
from .models import PaymentTerms, PaymentTermsDays


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
                                 'The total percentage needs to be 100%',
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
                                 'The total percentage needs to be 100%',
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
    context = {'form': form, 'formset': formset, 'object': paymentTerms_form}
    return render(request, template_name, context)


class PaymentTerms_Delete(DeleteView):
    model = PaymentTerms
    success_url = reverse_lazy('persons:paymentTerms')

    def get(self, request, *args, **kwargs):
        context = messages.warning(
            request,
            'Payment Term successfully deleted',
            'alert-warning'
        )
        return self.delete(context, request, *args, **kwargs)
