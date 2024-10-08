# Generated by Django 5.0.6 on 2024-09-13 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_alter_company_usersnumbers'),
        ('persons', '0019_personseller_user_created_personseller_user_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='personseller',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='companies.company'),
            preserve_default=False,
        ),
    ]
