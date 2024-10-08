from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

from modules.finances.models import Entry


def hierarchy_is_1(function):
    def wrap(request, *args, **kwargs):
        if request.user.hierarchy == 1:
            return function(request, *args, **kwargs)
        else:
            messages.warning(
                request,
                'Error 403: Permission Denied!',
                'alert-danger'
            )
            return redirect('main:index')
    return wrap


def hierarchy_is_2(function):
    def wrap(request, *args, **kwargs):
        if request.user.hierarchy == 2:
            return function(request, *args, **kwargs)
        else:
            messages.warning(
                request,
                'Error 403: Permission Denied!',
                'alert-danger'
            )
            return redirect('main:index')
    return wrap


def auditEntry(function):
    def wrap(request, *args, **kwargs):
        auditDate = request.user.company.auditDate
        entry = get_object_or_404(Entry, pk=kwargs['pk'])

        if entry.entryDate > auditDate:
            return function(request, *args, **kwargs)
        else:
            messages.warning(
                request,
                (
                    'Error editing this record, '
                    'its date is less than the last audit date!'
                ),
                'alert-danger'
            )
            return redirect('finances:entrys_list')
    return wrap
