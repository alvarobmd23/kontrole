# Generated by Django 4.2.1 on 2023-05-13 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart_of_accounts', '0005_alter_sintetic_typeaccount_delete_typeaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[(1, '1. ATIVO'), (2, '2. PASSIVO'), (3, '3. RECEITAS'), (4, '4. CUSTOS E DESPESAS')], max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='sintetic',
            name='typeaccount',
        ),
    ]
