from django.db import models
from django.urls import reverse

from user_apps.company.models import Company


class Document_Type(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    document_type = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("document_type:document_type")

    def __str__(self):
        return self.document_type
