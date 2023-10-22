from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employee.views import EmployeeViewSet

router = DefaultRouter()
router.register(r"", EmployeeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
