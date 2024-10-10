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
        unique=True,
        blank=False,
        null=False
    )
    locked = models.BooleanField(
        default=False
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
        unique=True,
        blank=False,
        null=False
    )
    active = models.BooleanField(
        default=True
    )
    locked = models.BooleanField(
        default=False
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


# DOCUMENT TYPE


class DocumentType (models.Model):
    documentTypeDescription = models.CharField(
        _("documentTypeDescription"),
        unique=True,
        max_length=50
    )
    active = models.BooleanField(
        default=True
    )
    locked = models.BooleanField(
        default=False
    )
    user_created = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='documentType_user_created'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )
    user_updated = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='documentType_user_updated'
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        ordering = ('documentTypeDescription', 'pk',)

    def __str__(self):
        return self.documentTypeDescription

    def get_absolute_url(self):
        return reverse_lazy(
            'finances:documentType_list', kwargs={'pk': self.pk})


# ENTRYS


class Entry (models.Model):
    date = models.DateField()
    entryDocumentType = models.ForeignKey(
        DocumentType,
        on_delete=models.PROTECT
    )
    entryNumDocument = models.CharField(
        _("entryNumDocument"),
        max_length=20,
        blank=False,
        null=False
    )
    entryTotalValue = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        blank=False,
        null=False
    )
    entryDescription = models.CharField(
        _("entryDescription"),
        max_length=60,
        blank=False,
        null=False
    )
    entryObs = models.CharField(
        _("entryObs"),
        max_length=100,
        blank=True,
        null=True
    )
    entryTotalCredit = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        blank=False,
        null=False
    )
    entryTotalDebit = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        blank=False,
        null=False
    )
    user_created = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='entry_created'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )
    user_updated = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='entry_updated'
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date',)

    def get_absolute_url(self):
        return reverse_lazy('finances:entrys_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} - {} {} - {}'.format(
            self.date.strftime('%d/%m/%Y'),
            self.entryDocumentType,
            self.entryNumDocument,
            self.entryDescription,
        )

    def itemRef(self):
        return '{} - {} {}'.format(
            self.date.strftime('%d/%m/%Y'),
            self.entryDocumentType,
            self.entryNumDocument,
        )

    def date_formated(self):
        return self.date.strftime('%d/%m/%Y')


class EntryItem (models.Model):
    MOVEMENT_TYPE = (
        ("C", "CREDIT"),
        ("D", "DEBIT")
    )
    itemEntry = models.ForeignKey(
        Entry,
        on_delete=models.CASCADE,
        related_name='itensEntry'
    )
    itemEntryAccount = models.ForeignKey(
        AnaliticAccount,
        on_delete=models.PROTECT,
        related_name='itemEntryAccount'
    )
    itemEntryType = models.CharField(
        _("itemType"),
        max_length=1,
        choices=MOVEMENT_TYPE,
        blank=False,
        null=False
    )
    itemEntryValue = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        blank=False,
        null=False
    )
    itemEntryValueRef = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        blank=False,
        null=False
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {} - {}'.format(
            self.itemEntry.itemRef,
            self.itemEntryType,
            self.itemEntryAccount,
            self.itemEntryValue
        )
