# Generated by Django 4.1.7 on 2024-01-21 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_employee_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='api.company'),
        ),
        migrations.AlterField(
            model_name='product',
            name='drug_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drug_group', to='api.druggroup'),
        ),
    ]
