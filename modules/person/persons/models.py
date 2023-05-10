from django.db import models
from django.urls import reverse

from user_apps.company.models import Company


class Person(models.Model):
    class TypePerson(models.IntegerChoices):
        PF = 1, "Pessoa Física"
        PJ = 2, "Pessoa Jurídica"

    typeperson = models.PositiveSmallIntegerField(
        choices=TypePerson.choices,
        default=TypePerson.PF,
        blank=True,
        null=True)
    cpfcnpj = models.CharField(max_length=14, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    obs = models.CharField(max_length=100, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("persons:persons")

    def __str__(self):
        return self.name
