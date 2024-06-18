from django.contrib import admin

from .models import (PaymentTerms, PaymentTermsDays, Person, PersonContact,
                     PersonCustomer, PersonSeller)


class PersonContactInline(admin.TabularInline):
    model = PersonContact


class PersonCustomerInline(admin.TabularInline):
    model = PersonCustomer


class PersonSellerInline(admin.TabularInline):
    model = PersonSeller


class PersonAdmin(admin.ModelAdmin):
    inlines = [PersonContactInline, PersonCustomerInline, PersonSellerInline]


admin.site.register(Person, PersonAdmin)


class PaymentTermsDaystInline(admin.TabularInline):
    model = PaymentTermsDays


class PaymentTermsAdmin(admin.ModelAdmin):
    inlines = [PaymentTermsDaystInline]


admin.site.register(PaymentTerms, PaymentTermsAdmin)
