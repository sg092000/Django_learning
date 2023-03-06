from django.db import models

# Create your models here.

class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=50)
    EmployeeAddress = models.CharField(max_length=500)
    DOJ = models.DateField()
    
class EmpPersonalDetail(models.Model):
    P_contact = models.IntegerField(null = False , blank = False)
    S_contact = models.IntegerField(blank = True)
    
    
    
