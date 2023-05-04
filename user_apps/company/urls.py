from django.urls import path

from user_apps.account.views import signup

from .views import NewCompany

urlpatterns = [
    path('new/', NewCompany.as_view(), name='new_company'),
    path('signup/', signup, name='signup')
]
