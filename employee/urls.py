from django.urls import path

from employee.views import EmployeeList, EmployeeDetail

urlpatterns = [
    path("", EmployeeList.as_view(), name="employee-list"),
    path("/<int:pk>/", EmployeeDetail.as_view(), name="employee-detail"),
]
