# Generated by Django 4.1.7 on 2023-03-05 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_company_zip_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company", name="name", field=models.CharField(max_length=100),
        ),
    ]
