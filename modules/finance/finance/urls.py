from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'finance'
urlpatterns = [
    path('', login_required(views.FinanceList.as_view()), name='finance-list'),
    path('new/', login_required(views.FinanceFinanceItemCreate.as_view()),
         name='finance-new'),
    path('finance/<int:pk>', login_required(views.FinanceFinanceItemUpdate.as_view()),
         name='finance-update'),
    path('finance_delete/<int:pk>', login_required(views.FinanceDelete.as_view()),
         name='finance-delete'),
]
