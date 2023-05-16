from django.db import models
from django.urls import reverse

# Create your models here.
from user_apps.company.models import Company


class TypeAccount(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    typeaccount = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("chart_of_account:chart_of_account")

    def __str__(self):
        return self.typeaccount


class Sintetic(models.Model):
    typeaccount = models.ForeignKey(TypeAccount, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    sintetic = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("chart_of_account:chart_of_account")

    def __str__(self):
        return self.sintetic


class Analitic(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    sintetic = models.ForeignKey(Sintetic, on_delete=models.PROTECT)
    analitic = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("chart_of_account:chart_of_account")

    def __str__(self):
        return self.analitic
