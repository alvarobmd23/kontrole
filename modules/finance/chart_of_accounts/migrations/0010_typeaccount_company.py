# Generated by Django 4.2.1 on 2023-05-13 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('chart_of_accounts', '0009_typeaccount_alter_sintetic_typeaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeaccount',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='company.company'),
            preserve_default=False,
        ),
    ]
