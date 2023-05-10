from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import Persons_Delete, Persons_List, Persons_New, Persons_Update

app_name = 'persons'

urlpatterns = [
    path('', login_required(Persons_List.as_view()), name='persons'),
    path('new/', login_required(Persons_New.as_view()),
         name='persons_new'),
    path('update/<int:pk>', login_required(Persons_Update.as_view()),
         name='persons_update'),
    path('delete/<int:pk>', login_required(Persons_Delete.as_view()),
         name='persons_delete')
]
