from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def public_index(request):
    return render(request, 'public_index.html')


@login_required
def index(request):
    return render(request, 'index.html')
