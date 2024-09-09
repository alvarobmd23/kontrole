
from django.contrib.auth.decorators import login_required
from django.urls import path

from core.accounts import views as v

app_name = 'user'

urlpatterns = [
     path('logout/',
          v.custom_logout,
          name='logout'),
     path('users/',
          login_required(v.user_list),
          name='users'),
     path('user/',
          login_required(v.user_list_to_client),
          name='clientusers'),
     path('users/add',
          login_required(v.user_add),
          name='user_add'),
     path('user/add',
          login_required(v.user_add_to_client),
          name='clientuser_add'),
     path('users/edit/<int:pk>/',
          login_required(v.user_edit),
          name='user_edit'),
     path('user/edit/<int:pk>/',
          login_required(v.user_edit_to_client),
          name='clientuser_edit'),
     path('password/edit/<int:pk>/',
          login_required(v.user_edit_to_user),
          name='useruser_edit'),
     path('users/delete/<int:pk>/',
          login_required(v.User_delete.as_view()),
          name='user_delete'),
     path('user/delete/<int:pk>/',
          login_required(v.User_delete_to_client.as_view()),
          name='clientuser_delete'),
]
