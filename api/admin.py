from django.contrib import admin
from api.models import Company, Employee, DrugGroup, Product

# Register your models here.

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(DrugGroup)
admin.site.register(Product)