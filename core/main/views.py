from django.shortcuts import render


def public_index(request):
    return render(request, 'public_index.html')


def index(request):
    return render(request, 'index.html')
