# Generated by Django 4.1.7 on 2023-08-01 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_druggroup_alter_company_user_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='exp_date',
            field=models.DateField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='mfg_date',
            field=models.DateField(max_length=100),
        ),
    ]