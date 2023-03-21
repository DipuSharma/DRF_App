from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from api.models import Company, Employee
from api.serializers import UserSerializer, CompanySerializer, EmployeeSerializer


# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def company(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            comp = Company.objects.filter(user=user)
            print("User_company_________________________", comp)
            com_serializer = CompanySerializer(comp, many=True, context={'request': request})
            return Response(com_serializer.data)
        except Exception as e:
            return Response({'message': 'Opps!! User not exists'})

    def employees(self, request, pk=None):
        print("Company Id____________________", pk)
        # try:
        #     company = Company.objects.get(pk=pk)
        #     employee = Employee.objects.filter(company=company)
        #     emp_serializer = EmployeeSerializer(employee, many=True, context={'request':request})
        #     return Response(emp_serializer.data)
        # except Exception as e:
        #     return Response(
        #        { 'message': 'Oops Company not exists!!'}
        #     )


class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # Custome api serializer just like find employee of particular company
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            employee = Employee.objects.filter(company=company)
            emp_serializer = EmployeeSerializer(employee, many=True, context={'request': request})
            return Response(emp_serializer.data)
        except Exception as e:
            return Response(
                {'message': 'Oops Company not exists!!'}
            )


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
