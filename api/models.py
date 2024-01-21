from django.db import models
from django.contrib.auth.models import User

from django.db import models
from uuid import uuid4
from django.utils import timezone

# Create your models here.


class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


# Create your models here.
company_type_choice = (
    ("", ""),
    ("IT", "IT"),
    ("Non IT", "Non IT"),
    ("Govt", "Goverment"),
    ("Institute", "Institute"),
    ("Medical", "Medical"),
)


class Company(BaseModel):
    name = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=company_type_choice)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


employe_choise = (
    ("", ""),
    ("Sr. Manager", "Sr. Manager"),
    ("Manager", "Manager"),
    ("Sr. Engineer", "Sr. Engineer"),
    ("Asst. Engineer", "Asst. Engineer"),
    ("Labour", "Labour"),
    ("HR", "HR"),
    ("Tester", "Tester"),
)

employee_grade = (("", ""), ("A", "A"), ("B", "B"), ("C", "C"))


class Employee(BaseModel):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=100, choices=employe_choise)
    grade = models.CharField(max_length=50, choices=employee_grade)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="employees"
    )  # One2Many Relationship Django

    def __str__(self):
        return self.name


class Address(BaseModel):
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    dist = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.IntegerField()

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="address"
    )
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="address"
    )

    def __str__(self):
        return self.address_line_1


class DrugGroup(BaseModel):
    name = models.CharField(max_length=100)
    prescription = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(
        max_length=50,
    )
    prescription = models.CharField(max_length=200)
    batch = models.CharField(
        max_length=100,
    )
    rac_no = models.CharField(
        max_length=100,
    )
    quantity = models.FloatField(
        max_length=5,
    )
    mrp = models.FloatField(max_length=20)
    mfg_date = models.DateField(max_length=100)
    exp_date = models.DateField(max_length=100)
    grade = models.CharField(max_length=50, choices=employee_grade)
    drug_group = models.ForeignKey(
        DrugGroup, on_delete=models.CASCADE, related_name="drug_group"
    )  # one2 many relationship django
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="company"
    )  # One2Many Relationship Django

    def __str__(self):
        return self.name
