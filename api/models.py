from django.db import models

# Create your models here.
company_type_choice = (('', ''), ('IT', 'IT'), ('Non IT', 'Non IT'), ('Govt','Goverment'), ('Institute', 'Institute'))

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=20)
    address_line_2 = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=6)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=company_type_choice)
    data = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name +  ' -- ' + self.zip_code   # Show One2Many field relation name and zipcode 

employe_choise = (('', ''),
('Sr. Manager', 'Sr. Manager'), 
('Manager', 'Manager'), 
('Sr. Engineer', 'Sr. Engineer'), 
('Asst. Engineer', 'Asst. Engineer'), 
('Labour', 'Labour'), ('HR','HR'), ('Tester', 'Tester'))

employee_grade = (('', ''), ('A', 'A'), ('B', 'B'), ('C', 'C'))

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=100, choices=employe_choise)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=6)
    date = models.DateTimeField(auto_now=True)
    grade = models.CharField(max_length=50, choices=employee_grade)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # One2Many Relationship Django
    
    def __str__(self):
        return self.name 