from django.contrib import admin

from .models import AnaliticAccount, Entry, EntryItem, SinteticAccount

admin.site.register(SinteticAccount)

admin.site.register(AnaliticAccount)


class ItemEntryInline(admin.TabularInline):
    model = EntryItem


class EntryAdmin(admin.ModelAdmin):
    inlines = [ItemEntryInline]


admin.site.register(Entry, EntryAdmin)

admin.site.register(EntryItem)
