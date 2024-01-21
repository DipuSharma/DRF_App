from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from api.models import Company, Employee, DrugGroup, Product, Address
from api import serializers as serialize_service 


# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serialize_service.UserSerializer

    @action(detail=True, methods=['get'])
    def company(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            comp = Company.objects.filter(user=user)
            com_serializer = serialize_service.CompanySerializer(comp, many=True, context={'request': request})
            return Response(data=JSONRenderer.render(com_serializer.data))
        except Exception as e:
            return Response({'message': 'Opps!! User not exists'})


class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = serialize_service.CompanySerializer

    # Custome api serializer just like find employee of particular company
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            employee = Employee.objects.filter(company=company)
            emp_serializer = serialize_service.EmployeeSerializer(employee, many=True, context={'request': request})
            return Response(emp_serializer.data)
        except Exception as e:
            return Response(
                {'message': 'Oops Company not exists!!'}
            )


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = serialize_service.EmployeeSerializer

class DrugGroupViewsets(viewsets.ModelViewSet):
    queryset = DrugGroup.objects.all()
    serializer_class = serialize_service.DrugGroupSerializer

class ProductViewsets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serialize_service.ProductSerializer

class AddressViewSets(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = serialize_service.AdderssSerializer