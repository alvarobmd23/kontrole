# Generated by Django 5.0.6 on 2024-10-08 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0007_alter_entry_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ('-date',)},
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='entryDate',
            new_name='date',
        ),
    ]