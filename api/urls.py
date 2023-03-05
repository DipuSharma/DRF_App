from django.urls import path, include
from api.views import CompanyViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewset)


urlpatterns = [
    path('', include(router.urls))
]
