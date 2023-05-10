from django.db import models
from django.db.models import Case, Value, When
from django.urls import reverse
from django.utils.translation import gettext as _

from user_apps.company.models import Company


class ClassificationAccount(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    mother_account = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("chart_of_accounts:chart_of_accounts_list")

    def __str__(self):
        return self.mother_account


class Chart_of_Accounts_Sintetico(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    mother_account = models.ForeignKey(
        ClassificationAccount, on_delete=models.CASCADE)
    sintetic_account = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("chart_of_accounts:chart_of_accounts_list")

    def __str__(self):
        return "%s - %s" % (self.description, self.mother_account)


class Chart_of_Accounts_Analitic(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    sintetic_account = models.ForeignKey(
        Chart_of_Accounts_Sintetico, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("chart_of_accounts:chart_of_accounts_list")

    def __str__(self):
        return "%s - %s" % (self.description, self.sintetic_account)
