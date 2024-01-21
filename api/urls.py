from django.urls import path, include
from api import views as controller
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', controller.UserViewset)
router.register(r'address', controller.AddressViewSets)
router.register(r'companies', controller.CompanyViewset)
router.register(r'employees', controller.EmployeeViewset)
router.register(r'drugroup', controller.DrugGroupViewsets)
router.register(r'product', controller.ProductViewsets)

urlpatterns = [
    path('', include(router.urls))
]
