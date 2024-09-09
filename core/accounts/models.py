from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.companies.models import Company


class AUser(AbstractUser):
    email = models.EmailField(unique=True)
    company = models.ForeignKey(
        Company,
        verbose_name=_("company"),
        on_delete=models.CASCADE,
        related_name='users'
        )
    hierarchy = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(3)
        ]
    )
