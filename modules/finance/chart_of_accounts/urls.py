from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (Chart_of_Accounts_Sintetico_Delete,
                    Chart_of_Accounts_Sintetico_List,
                    Chart_of_Accounts_Sintetico_New,
                    Chart_of_Accounts_Sintetico_Update,
                    ClassificationAccount_List)

app_name = 'chart_of_accounts'

urlpatterns = [
    path('sintetic/', login_required(Chart_of_Accounts_Sintetico_List.as_view()),
         name='chart_of_accounts_list'),
    path('sintetic/new/', login_required(Chart_of_Accounts_Sintetico_New.as_view()),
         name='chart_of_accounts_sintetico_new'),
    path('sintetic/update/<int:pk>', login_required(Chart_of_Accounts_Sintetico_Update.as_view()),
         name='chart_of_accounts_sintetico_update'),
    path('sintetic/delete/<int:pk>', login_required(Chart_of_Accounts_Sintetico_Delete.as_view()),
         name='chart_of_accounts_sintetico_delete')
]
