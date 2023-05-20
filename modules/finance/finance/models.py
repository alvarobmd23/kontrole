from django.db import models
from django.urls import reverse

from modules.finance.chart_of_accounts.models import Analitic
from modules.finance.document_type.models import Document_Type
from user_apps.company.models import Company


class Finance(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    date = models.DateField()
    document_type = models.ForeignKey(Document_Type, on_delete=models.PROTECT)
    n_doc = models.CharField(max_length=10, blank=True, null=True)
    total_value = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100, blank=True, null=True)
    obs = models.CharField(max_length=100, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('finance-update', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.date} {self.description} {self.total_value}"


class FinanceItem(models.Model):
    class TypeMovement(models.IntegerChoices):
        DEBITO = 1, "Débito"
        CREDITO = 2, "Crédito"
    finance = models.ForeignKey(Finance, on_delete=models.CASCADE)
    account = models.ForeignKey(Analitic, on_delete=models.PROTECT)
    typemovement = models.PositiveSmallIntegerField(
        choices=TypeMovement.choices,
        default=TypeMovement.DEBITO,
        blank=True,
        null=True)
    value = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.finance} {self.typemovement} {self.account} {self.value}"
