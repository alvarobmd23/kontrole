from django.shortcuts import render


def persons(request):
    return render(request, 'persons/persons.html')
