# Generated by Django 4.1.7 on 2024-01-21 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_company_address_line_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zipcode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='type',
            field=models.CharField(choices=[('', ''), ('IT', 'IT'), ('Non IT', 'Non IT'), ('Govt', 'Goverment'), ('Institute', 'Institute'), ('Medical', 'Medical')], max_length=100),
        ),
    ]
