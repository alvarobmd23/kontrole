from django.core.exceptions import PermissionDenied


def hierarchy_is_1(function):
    def wrap(request, *args, **kwargs):
        if request.user.hierarchy == 1:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


def hierarchy_is_2(function):
    def wrap(request, *args, **kwargs):
        if request.user.hierarchy == 2:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap
