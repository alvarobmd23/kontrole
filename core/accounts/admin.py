from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AUser

admin.site.register(AUser, UserAdmin)
UserAdmin.fieldsets += ('Company', {'fields': ('company',)}),
UserAdmin.fieldsets += ('hierarchy', {'fields': ('hierarchy',)}),
