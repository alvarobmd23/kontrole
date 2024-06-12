from django.db import models
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    nameCompany = models.CharField(_("nameCompany"), max_length=50)
