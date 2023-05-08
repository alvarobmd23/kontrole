from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import EditCompany, NewCompany

app_name = 'company'

urlpatterns = [
    path('new/', NewCompany.as_view(), name='new_company'),
    path('edit/', login_required(EditCompany.as_view()), name='edit_company'),
]
