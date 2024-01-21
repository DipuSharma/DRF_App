from django.contrib.auth.models import User
from api.models import Company, Employee, DrugGroup, Product, Address
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.

class AdderssSerializer(serializers.ModelSerializer):
    zipcode = serializers.IntegerField()
    # Field Level Validation
    def validate_zipcode(self, value):
        if len(value) > 6:
            raise serializers.ValidationError("Zip code must be 6 digit")
        return value

    # Object level validation
    def validate(self, data):
        zipcode = data.zipcode
        city = data.city

        return data
    class Meta:
        model = Address
        fields = ["url", "address_line_1", "address_line_2", "city", "dist", "state", "zipcode",]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'is_active']


class CompanySerializer(serializers.ModelSerializer):
    address= AdderssSerializer(many=True)
    class Meta:
        model = Company
        """
        """
        fields = ['url', 'name', 'about', 'type', 'created_at', 'updated_at', 'user', 'address']

class EmployeeSerializer(serializers.ModelSerializer):
    address= AdderssSerializer(many=True)
    class Meta:
        model = Employee
        fields = ['url', 'name', 'position', 'grade', 'created_at', 'updated_at', 'company', 'address']



class DrugGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugGroup
        fields = ['url', 'name', 'prescription']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'name', 'batch', 'rac_no', 'quantity', 'mrp', 'mfg_date', 'exp_date', ]