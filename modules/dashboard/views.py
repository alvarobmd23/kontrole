from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    data = {}
    data['usernow'] = auth.get_user(request)
    return render(request, 'dashboard/dashboard.html', data)
