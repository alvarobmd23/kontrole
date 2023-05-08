from django.db import models
from django.urls import reverse

from user_apps.company.models import Company


class Person(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("persons:persons")

    def __str__(self):
        return self.name
