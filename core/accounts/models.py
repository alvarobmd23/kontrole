from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.companies.models import Company


class AUser(AbstractUser):
    email = models.EmailField(unique=True)
    company = models.ForeignKey(
        Company,
        verbose_name=_("company"),
        on_delete=models.CASCADE
        )
    hierarchy = models.PositiveIntegerField()
