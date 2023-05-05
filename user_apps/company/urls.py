from django.urls import path

from .views import EditCompany, NewCompany

urlpatterns = [
    path('new/', NewCompany.as_view(), name='new_company'),
    path('edit/<int:company_id>/', EditCompany.as_view(), name='edit_company'),
]
