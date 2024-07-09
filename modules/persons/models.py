from django.conf import settings
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from core.companies.models import Company

User = settings.AUTH_USER_MODEL


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
    personObs = models.CharField(
        _("personObs"),
        max_length=300,
        blank=True,
        null=True
    )
    user_created = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='person_user_created'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )
    user_updated = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='person_user_updated'
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        ordering = ('personName',)

    def __str__(self):
        return '{} - {} {}'.format(
            self.personName,
            self.personType,
            self.personTaxpayerRegistration
        )


class PersonContact (models.Model):
    CONTACT_TYPE = (
        ("E", "E-MAIL"),
        ("T", "PHONE NUMBER"),
        ("W", "WHATSAPP"),
        ("O", "OTHER")
    )
    contactPerson = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    contactType = models.CharField(
        _("contactType"),
        max_length=1,
        choices=CONTACT_TYPE,
        blank=False,
        null=False
    )
    contactDescription = models.CharField(
        _("contact"),
        max_length=100,
        blank=False,
        null=False
    )
    contactObs = models.CharField(
        _("contactObs"),
        max_length=300,
        blank=True,
        null=True
    )
    user_created = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='personContact_user_created'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )
    user_updated = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='personContact_user_updated'
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {} - {}'.format(
            self.pk,
            self.contactPerson,
            self.contactType,
            self.contactDescription
        )


class PersonSeller (models.Model):
    sellerPerson = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    sellerComission = models.DecimalField(
        _("sellerComission"),
        max_digits=4,
        decimal_places=2,
        default=0
    )
    sellerObs = models.CharField(
        _("sellerObs"),
        max_length=300,
        blank=True,
        null=True
    )
    user_created = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='personSeller_user_created'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )
    user_updated = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='personSeller_user_updated'
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    @property
    def comissionInPercentage(self):
        return f"{self.sellerComission} %"

    @property
    def comissionToCalculate(self):
        return (self.sellerComission/100)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(
            self.pk,
            self.sellerPerson,
            self.comissionInPercentage
        )


class PaymentTerms(models.Model):
    paymentTermDescription = models.CharField(
        _("paymentTermDescription"),
        max_length=50
    )
    user_created = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='paymentTerms_user_created'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )
    user_updated = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='paymentTerms_user_updated'
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.paymentTermDescription
    
    def get_absolute_url(self):
        return reverse_lazy('persons:paymentTerms_detail', kwargs={'pk': self.pk})


class PaymentTermsDays(models.Model):
    paymentTerms = models.ForeignKey(
        PaymentTerms,
        on_delete=models.CASCADE,
        related_name='paymentterm')
    paymentTermsDay = models.PositiveSmallIntegerField(
        _("paymentTermsDay"),
        default=0
    )
    paymentTermsPercentage = models.DecimalField(
        _(""),
        max_digits=5,
        decimal_places=2,
        default=0
    )
    user_created = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='paymentTermsDays_user_created'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )
    user_updated = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='paymentTermsDays_user_updated'
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    @property
    def paymentTermsPercentageInPercentage(self):
        return f"{self.paymentTermsPercentage} %"

    @property
    def paymentTermsPercentageToCalculate(self):
        return (self.paymentTermsPercentage/100)

    class Meta:
        ordering = ('paymentTermsDay',)

    def __str__(self):
        return '{} - {} day(s) - {}'.format(
            self.paymentTerms,
            self.paymentTermsDay,
            self.paymentTermsPercentageInPercentage
        )


class PersonCustomer(models.Model):
    customerPerson = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    customerFinDiscount = models.DecimalField(
        _("customerFinDiscount"),
        max_digits=5,
        decimal_places=2,
        default=0
    )
    customerPaymentTerms = models.ForeignKey(
        PaymentTerms,
        verbose_name=_("customerPaymentTerms"),
        on_delete=models.PROTECT
    )
    customerObs = models.CharField(
        _("customerObs"),
        max_length=300,
        blank=True,
        null=True
    )
    user_created = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='personCustomer_user_created'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )
    user_updated = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='personCustomer_user_updated'
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    @property
    def customerFinDiscountPercentage(self):
        return f"{self.customerFinDiscount} %"

    @property
    def customerFinDiscountCalculate(self):
        return (self.customerFinDiscount/100)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} of Financial Discount - {}'.format(
            self.customerPerson,
            self.customerFinDiscountPercentage,
            self.customerPaymentTerms
        )
