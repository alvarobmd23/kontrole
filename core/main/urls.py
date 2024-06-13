from django.urls import path

from core.main import views as v

app_name = 'main'

urlpatterns = [
    path('', v.public_index, name='public_index'),
    path('index', v.index, name='index'),
]
