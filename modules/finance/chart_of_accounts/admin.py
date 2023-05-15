from django.contrib import admin

# Register your models here.
from .models import Analitic, Sintetic, TypeAccount

admin.site.register(TypeAccount)
admin.site.register(Sintetic)
admin.site.register(Analitic)
