from django.shortcuts import render

from .models import PaymentTerms


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
