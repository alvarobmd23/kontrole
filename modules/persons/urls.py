from django.urls import path

from .views import persons

urlpatterns = [
    path('', persons)
]
