
from django.contrib.auth.decorators import login_required
from django.urls import path

from modules.persons import views as v

app_name = 'persons'

urlpatterns = [
    # paymentTerms
    path('paymentTerms/',
         login_required(v.paymentTerms_list), name='paymentTerms'),
    path('paymentTerms/<int:pk>/',
         login_required(v.paymentTerms_detail), name='paymentTerms_detail'),
]
