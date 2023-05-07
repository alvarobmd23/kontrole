from django.urls import path

from .views import persons

app_name = 'persons'

urlpatterns = [
    path('', persons)
]
