# Generated by Django 5.0.6 on 2024-10-10 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0009_analiticaccount_active_analiticaccount_locked_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sinteticaccount',
            name='active',
        ),
    ]
