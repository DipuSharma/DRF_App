from django.db import models

# Create your models here.


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=20)
    address_line_2 = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=6)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'), ('Non IT', 'Non IT'), ('Govt','Goverment'), ('Institute', 'Institute')))
    data = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    