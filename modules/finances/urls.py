
from django.contrib.auth.decorators import login_required
from django.urls import path

from modules.finances import views as v

app_name = 'finances'

urlpatterns = [
     # chartOfAccounts
     path('chartOfAccounts/',
          login_required(v.chartOfAccounts_list),
          name='chartOfAccounts'),
     # chartOfAccounts - Sintetic Accounts
     path('chartOfAccounts/sinteticAdd',
          login_required(v.Sintetic_add.as_view()),
          name='sintetic_add'),
     path('chartOfAccounts/sintetic/edit/<int:pk>/',
          login_required(v.Sintetic_edit.as_view()),
          name='sintetic_edit'),
     path('chartOfAccounts/sintetic/delete/<int:pk>/',
          login_required(v.Sintetic_delete.as_view()),
          name='sintetic_delete'),
     # chartOfAccounts - Analitic Accounts
     path('chartOfAccounts/analiticAdd',
          login_required(v.Analitic_add.as_view()),
          name='analitic_add'),
     path('chartOfAccounts/analitic/edit/<int:pk>/',
          login_required(v.Analitic_edit.as_view()),
          name='analitic_edit'),
     path('chartOfAccounts/analitic/delete/<int:pk>/',
          login_required(v.Analitic_delete.as_view()),
          name='analitic_delete'),
     # Document Type
     path('documentType/',
          login_required(v.documentType_list),
          name='documentType_list'),
     path('documentType/Add',
          login_required(v.DocumentType_add.as_view()),
          name='documentType_add'),
     path('documentType/edit/<int:pk>/',
          login_required(v.DocumentType_edit.as_view()),
          name='documentType_edit'),
     path('documentType/delete/<int:pk>/',
          login_required(v.DocumentType_delete.as_view()),
          name='documentType_delete'),
]
