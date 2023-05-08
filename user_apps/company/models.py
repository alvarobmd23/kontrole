from django.db import models
from django.urls import reverse


class Company (models.Model):
    company_name = models.CharField(max_length=100)
    company_nickname = models.CharField(max_length=100)
    logo = models.FileField

    def get_absolute_url(self):
        return reverse("dashboard:dashboard")

    def __str__(self):
        return self.company_name
