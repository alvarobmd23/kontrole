# Generated by Django 5.0.6 on 2024-07-31 14:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_alter_paymenttermsdays_company'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenttermsdays',
            name='user_created',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='paymentTermsDays_user_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='paymenttermsdays',
            name='user_updated',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='paymentTermsDays_user_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]