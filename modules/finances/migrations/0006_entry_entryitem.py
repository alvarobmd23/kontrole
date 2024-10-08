# Generated by Django 5.0.6 on 2024-10-02 12:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_alter_company_usersnumbers'),
        ('finances', '0005_alter_analiticaccount_analiticname_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entryDate', models.DateField()),
                ('entryNumDocument', models.CharField(max_length=20, verbose_name='entryNumDocument')),
                ('entryTotalValue', models.DecimalField(decimal_places=2, max_digits=15)),
                ('entryDescription', models.CharField(max_length=60, verbose_name='entryDescription')),
                ('entryObs', models.CharField(blank=True, max_length=100, null=True, verbose_name='entryObs')),
                ('entryTotalCredit', models.DecimalField(decimal_places=2, max_digits=15)),
                ('entryTotalDebit', models.DecimalField(decimal_places=2, max_digits=15)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('entryDocumentType', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finances.documenttype')),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='entry_created', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='entry_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('entryDate',),
            },
        ),
        migrations.CreateModel(
            name='EntryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemEntryType', models.CharField(choices=[('C', 'CREDIT'), ('D', 'DEBIT')], max_length=1, verbose_name='itemType')),
                ('itemEntryValue', models.DecimalField(decimal_places=2, max_digits=15)),
                ('itemEntryValueRef', models.DecimalField(decimal_places=2, max_digits=15)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('itemEntry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itensEntry', to='finances.entry')),
                ('itemEntryAccount', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='itemEntryAccount', to='finances.analiticaccount')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
