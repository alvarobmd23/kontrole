from django.contrib import admin

from .models import (PaymentTerms, PaymentTermsDays, Person, PersonContact,
                     PersonCustomer, PersonSeller, PersonSupplier)


class PersonContactInline(admin.TabularInline):
    model = PersonContact


class PersonCustomerInline(admin.TabularInline):
    model = PersonCustomer


class PersonSupplierInline(admin.TabularInline):
    model = PersonSupplier


class PersonAdmin(admin.ModelAdmin):
    inlines = [PersonContactInline, PersonCustomerInline, PersonSupplierInline]


admin.site.register(Person, PersonAdmin)


class PaymentTermsDaystInline(admin.TabularInline):
    model = PaymentTermsDays


class PaymentTermsAdmin(admin.ModelAdmin):
    inlines = [PaymentTermsDaystInline]


admin.site.register(PaymentTerms, PaymentTermsAdmin)

admin.site.register(PaymentTermsDays)

admin.site.register(PersonSeller)
