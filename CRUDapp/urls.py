from django.urls import path,re_path
from django.urls import include
from CRUDapp import views

urlpatterns = [
    path(r'employee',views.employeeApi),
    re_path(r'^employee/([0-9]+)/$',views.employeeApi)
]
