from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, UpdateView

from core.companies.models import Company
from core.main.decorators import hierarchy_is_1, hierarchy_is_2

from .forms import AUser_Form, AUser_toClient_Form, AUser_toUser_Form
from .models import AUser


def custom_logout(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


@hierarchy_is_1
def user_list(request):
    template_name = 'user_list.html'
    object = AUser.objects.all().order_by(
        'company',
        'hierarchy',
        'username',
    )
    context = {'object_list': object}
    return render(request, template_name, context)


@hierarchy_is_2
def user_list_to_client(request):
    template_name = 'user_list_to_client.html'
    object = AUser.objects.all().filter(company=request.user.company).order_by(
        'hierarchy',
        'username',
    )
    context = {'object_list': object}
    return render(request, template_name, context)


@hierarchy_is_1
def user_add(request):
    template_name = 'user_form.html'
    user_form = AUser()

    if request.method == 'POST':
        form = AUser_Form(
            request.POST,
            instance=user_form
        )
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if password != confirm_password:
                messages.warning(
                    request,
                    'Passwords do not match!',
                    'alert-warning'
                )
            else:
                form = form.save(commit=False)
                form.password = make_password(password)
                form.save()
                messages.success(
                    request,
                    'User successfully added!',
                    'alert-success'
                )
                return HttpResponseRedirect(
                    reverse_lazy('user:users')
                    )

    else:
        form = AUser_Form(
            instance=user_form
        )

    context = {'form': form}
    return render(request, template_name, context)


@hierarchy_is_2
def user_add_to_client(request):
    template_name = 'user_form_to_client.html'
    user_form = AUser()

    if request.method == 'POST':
        form = AUser_toClient_Form(
            request.POST,
            instance=user_form
        )
        company = request.user.company
        if company.users.count() >= company.usersNumbers:
            messages.error(
                request,
                'This company has already reached the maximum number of allowed users!',
                'alert-error'
            )
            return HttpResponseRedirect(
                reverse_lazy('user:clientusers')
                )
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if password != confirm_password:
                messages.warning(
                    request,
                    'Passwords do not match!',
                    'alert-warning'
                )
            else:
                form = form.save(commit=False)
                form.password = make_password(password)
                form.company = company
                form.hierarchy = 3
                form.save()
                messages.success(
                    request,
                    'User successfully added!',
                    'alert-success'
                )
                return HttpResponseRedirect(
                    reverse_lazy('user:clientusers')
                    )

    else:
        form = AUser_toClient_Form(
            instance=user_form
        )

    context = {'form': form}
    return render(request, template_name, context)


@hierarchy_is_1
def user_edit(request, pk):
    template_name = 'user_form.html'
    user_form = AUser.objects.get(pk=pk)

    if request.method == 'POST':
        form = AUser_Form(
            request.POST,
            instance=user_form
        )
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if password != confirm_password:
                messages.warning(
                    request,
                    'Passwords do not match!',
                    'alert-warning'
                )
            else:
                form = form.save(commit=False)
                form.password = make_password(password)
                form.save()
                messages.success(
                    request,
                    'User successfully edited!',
                    'alert-success'
                )
                return HttpResponseRedirect(
                    reverse_lazy('user:users')
                    )

    else:
        form = AUser_Form(
            instance=user_form
        )

    context = {'form': form}
    return render(request, template_name, context)


@hierarchy_is_2
def user_edit_to_client(request, pk):
    template_name = 'user_form_to_client.html'
    user_form = AUser.objects.get(pk=pk)

    if request.method == 'POST':
        form = AUser_toClient_Form(
            request.POST,
            instance=user_form
        )
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if password != confirm_password:
                messages.warning(
                    request,
                    'Passwords do not match!',
                    'alert-warning'
                )
            else:
                form = form.save(commit=False)
                form.password = make_password(password)
                form.save()
                messages.success(
                    request,
                    'User successfully edited!',
                    'alert-success'
                )
                return HttpResponseRedirect(
                    reverse_lazy('user:clientusers')
                    )

    else:
        form = AUser_toClient_Form(
            instance=user_form
        )

    context = {'form': form}
    return render(request, template_name, context)


def user_edit_to_user(request, pk):
    template_name = 'user_form_to_user.html'
    user_form = AUser.objects.get(pk=pk)

    if request.method == 'POST':
        form = AUser_toUser_Form(
            request.POST,
            instance=user_form
        )
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if password != confirm_password:
                messages.warning(
                    request,
                    'Passwords do not match!',
                    'alert-warning'
                )
            else:
                form = form.save(commit=False)
                form.password = make_password(password)
                form.save()
                messages.success(
                    request,
                    'Password successfully changed!',
                    'alert-success'
                )
                return HttpResponseRedirect(
                    reverse_lazy('main:index')
                    )

    else:
        form = AUser_toUser_Form(
            instance=user_form
        )

    context = {'form': form}
    return render(request, template_name, context)


@method_decorator(hierarchy_is_1, name='dispatch')
class User_delete(DeleteView):
    model = AUser
    success_url = reverse_lazy('user:users')

    def get(self, request, *args, **kwargs):
        context = messages.warning(
            request,
            'User successfully deleted!',
            'alert-warning'
        )
        return self.delete(context, request, *args, **kwargs)


@method_decorator(hierarchy_is_2, name='dispatch')
class User_delete_to_client(DeleteView):
    model = AUser
    success_url = reverse_lazy('user:clientusers')

    def get(self, request, *args, **kwargs):
        context = messages.warning(
            request,
            'User successfully deleted!',
            'alert-warning'
        )
        return self.delete(context, request, *args, **kwargs)

    def get_queryset(self):
        company_user = self.request.user.company
        return AUser.objects.filter(company=company_user)
