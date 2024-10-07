from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


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
            return redirect(request.META.get('HTTP_REFERER', '/index'))
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
            return redirect(request.META.get('HTTP_REFERER', '/index'))
    return wrap
