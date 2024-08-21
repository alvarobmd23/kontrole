
from django.contrib.auth.decorators import login_required
from django.urls import path

from modules.persons import views as v

app_name = 'persons'

urlpatterns = [
     # paymentTerms
     path('paymentTerms/',
          login_required(v.paymentTerms_list),
          name='paymentTerms'),
     path('paymentTerms/add/',
          login_required(v.paymentTerms_add),
          name='paymentTerms_add'),
     path('paymentTerms/<int:pk>/',
          login_required(v.paymentTerms_detail),
          name='paymentTerms_detail'),
     path('paymentTerms/edit/<int:pk>/',
          login_required(v.paymentTerms_edit),
          name='paymentTerms_edit'),
     path('paymentTerms/delete/<int:pk>/',
          login_required(v.PaymentTerms_Delete.as_view()),
          name='paymentTerms_delete'),
]
