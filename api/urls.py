from django.urls import path, include
from api.views import UserViewset,CompanyViewset, EmployeeViewset, DrugGroupViewsets, ProductViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserViewset)
router.register(r'companies', CompanyViewset)
router.register(r'employees', EmployeeViewset)
router.register(r'drugroup', DrugGroupViewsets)
router.register(r'product', ProductViewsets)

urlpatterns = [
    path('', include(router.urls))
]
