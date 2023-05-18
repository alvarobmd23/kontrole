from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (Document_Type_Delete, Document_Type_List,
                    Document_Type_New, Document_Type_Update)

app_name = 'document_type'

urlpatterns = [
    path('', login_required(Document_Type_List.as_view()), name='document_type'),
    path('new/', login_required(Document_Type_New.as_view()),
         name='document_type_new'),
    path('update/<int:pk>', login_required(Document_Type_Update.as_view()),
         name='document_type_update'),
    path('delete/<int:pk>', login_required(Document_Type_Delete.as_view()),
         name='document_type_delete')
]
