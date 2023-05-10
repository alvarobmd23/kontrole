"""
URL configuration for kontrole project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('core.urls')),
    path('company/', include('user_apps.company.urls', namespace='company')),
    path('accounts/', include('user_apps.account.urls', namespace='accounts')),
    path('', include('modules.dashboard.urls', namespace='dashboard')),
    path('person/persons/', include('modules.person.persons.urls', namespace='persons')),
    path('finance/chart_of_accounts/',
         include('modules.finance.chart_of_accounts.urls', namespace='chart_of_accounts')),
]
