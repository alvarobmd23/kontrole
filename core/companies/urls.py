
from django.contrib.auth.decorators import login_required
from django.urls import path

from core.companies import views as v

app_name = 'company'

urlpatterns = [
     path('companies/',
          login_required(v.company_list),
          name='companies'),
     path('companies/add',
          login_required(v.Company_add.as_view()),
          name='company_add'),
     path('companies/edit/<int:pk>/',
          login_required(v.Company_edit.as_view()),
          name='company_edit'),
     path('company/edit/<int:pk>/',
          login_required(v.Company_toClient_edit.as_view()),
          name='clientcompany_edit'),
     path('companies/delete/<int:pk>/',
          login_required(v.Company_delete.as_view()),
          name='company_delete'),
]
