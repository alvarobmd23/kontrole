from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )
    search_fields = ('nameCompany',)
    list_filter = ('nameCompany',)
