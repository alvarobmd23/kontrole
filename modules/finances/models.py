from django.conf import settings
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _

from core.companies.models import Company

User = settings.AUTH_USER_MODEL

# CHART OF ACCOUNTS

ACCOUNTS_TYPE = (
    ('1', _('1. ASSETS')),
    ('2', _('2. LIABILITIES')),
    ('3', _('3. EQUITY')),
    ('4', _('4. REVENUES')),
    ('5', _('5. EXPENSES')),
)


class SinteticAccount (models.Model):
    accountsType = models.CharField(
        _("accountsType"),
        max_length=20,
        choices=ACCOUNTS_TYPE,
        blank=False,
        null=False
    )
    sinteticName = models.CharField(
        _("sinteticName"),
        max_length=100,
        blank=False,
        null=False
    )
    user_created = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='sinteticAccount_created'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )
    user_updated = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='sinteticAccountupdated'
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("finances:chartOfAccounts")

    def __str__(self):
        return '{}/{}'.format(
            self.get_accountsType_display(),
            self.sinteticName,
        )


class AnaliticAccount (models.Model):
    sinteticAccounts = models.ForeignKey(
        SinteticAccount,
        on_delete=models.PROTECT
    )
    analiticName = models.CharField(
        _("analiticName"),
        max_length=100,
        blank=False,
        null=False
    )
    user_created = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='analiticAccount_created'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )
    user_updated = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='analiticAccount_updated'
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("finances:chartOfAccounts")

    def __str__(self):
        return '{}/{}/{}'.format(
            self.sinteticAccounts.get_accountsType_display(),
            self.sinteticAccounts.sinteticName,
            self.analiticName,
        )
