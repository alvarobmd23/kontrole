from django.db import models
from django.utils.translation import gettext_lazy as _


class Person (models.Model):
    PERSONS_TYPE = (
        ("LP", "LEGAL PERSON"),
        ("NP", "NATURAL PERSON")
    )
    personType = models.CharField(
        _("personType"),
        max_length=2,
        choices=PERSONS_TYPE,
        blank=False,
        null=False
        )
    personName = models.CharField(
        _("personName"),
        max_length=100,
        blank=False,
        null=False
        )
    personTaxpayerRegistration = models.CharField(
        _("personTaxpayerRegistration"),
        max_length=30,
        blank=True,
        null=True
        )
    personAddress = models.CharField(
        _("personAddress"),
        max_length=100,
        blank=True,
        null=True
        )
    personCity = models.CharField(
        _("personCity"),
        max_length=100,
        blank=True,
        null=True
        )
    personState = models.CharField(
        _("personState"),
        max_length=100,
        blank=True,
        null=True
        )
    personCountry = models.CharField(
        _("personCountry"),
        max_length=100,
        blank=True,
        null=True
        )
    contactObs = models.CharField(
        _("personAddress"),
        max_length=300,
        blank=True,
        null=True
        )


class PersonContact (models.Model):
    CONTACT_TYPE = (
        ("E", "E-MAIL"),
        ("T", "PHONE NUMBER"),
        ("W", "WHATSAPP"),
        ("O", "OTHER")
    )
    contactPerson = models.ForeignKey(Person, on_delete=models.CASCADE)
    contactType = models.CharField(
        _("personType"),
        max_length=1,
        choices=CONTACT_TYPE,
        blank=False,
        null=False
        )
    contact = models.CharField(
        _("personName"),
        max_length=100,
        blank=False,
        null=False
        )
    contactObs = models.CharField(
        _("personAddress"),
        max_length=300,
        blank=True,
        null=True
        )
