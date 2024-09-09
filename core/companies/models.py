from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    nameCompany = models.CharField(
        _("nameCompany"),
        max_length=50,
        unique=True
        )
    usersNumbers = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        ordering = ('nameCompany',)

    def __str__(self):
        return self.nameCompany
