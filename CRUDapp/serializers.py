from rest_framework import serializers
from CRUDapp.models import Employee , EmpPersonalDetail


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('EmployeeId' , 'EmployeeName' , 'EmployeeAddress','DOJ')
        

class EmpPersonalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpPersonalDetail
        fields = ('P_contact' , 'S_contact')