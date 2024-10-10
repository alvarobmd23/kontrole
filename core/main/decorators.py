from functools import wraps

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


def audit(model):
    def decorator(function):
        @wraps(function)
        def wrap(request, *args, **kwargs):
            auditDate = request.user.company.auditDate
            obj = get_object_or_404(model, pk=kwargs['pk'])
            if auditDate is None or obj.date > auditDate:
                return function(request, *args, **kwargs)
            else:
                messages.warning(
                    request,
                    (
                        'This record is audited '
                        'by your company administrator!'
                    ),
                    'alert-danger'
                )
                return redirect(request.META.get('HTTP_REFERER', '/'))
        return wrap
    return decorator


def lock_verification(model):
    def decorator(function):
        @wraps(function)
        def wrap(request, *args, **kwargs):
            obj = get_object_or_404(model, pk=kwargs['pk'])
            if request.user.hierarchy == 3:
                if obj.locked is False:
                    return function(request, *args, **kwargs)
                else:
                    messages.warning(
                        request,
                        (
                            'This record is blocked '
                            'by your company administrator!'
                        ),
                        'alert-danger'
                    )
                    return redirect(request.META.get('HTTP_REFERER', '/'))
            else:
                return function(request, *args, **kwargs)
        return wrap
    return decorator
