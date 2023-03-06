from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CRUDapp.models import Employee
from CRUDapp.serializers import EmployeeSerializer



# Create your views here.
@csrf_exempt
def employeeApi(request,id=None):
    
    
    if(request.method == 'GET' and id==None) :
        try:
            employeeDetail = Employee.objects.all()
            emp_serializer = EmployeeSerializer(employeeDetail,many = True)
            return JsonResponse(emp_serializer.data,safe = False)
        except Exception as e:
            return JsonResponse("data doesnt exist",safe=False)
    
    # if(request.method == 'GET' and id==None) :
    #     try:
    #         employeeDetail = Employee.objects.all()
    #         emp_serializer = EmployeeSerializer(employeeDetail,many = True)
    #         empList = []
    #         try:
    #             for i in emp_serializer.data:
    #                 df = i
    #                 empList.append(df)
    #             print(empList)
    #         except Exception as e:
    #             return JsonResponse("not ran well",safe = False)    
    #         return JsonResponse(emp_serializer.data,safe = False)
    #     except Exception as e:
    #         return JsonResponse("data doesnt exist",safe=False)
        
    
    
    if (request.method == 'GET' and id!=None) :
        try : 
            emp = Employee.objects.get(EmployeeId = id)
            emp_serializer = EmployeeSerializer(emp)
            print(emp_serializer)
            return JsonResponse(emp_serializer.data,safe = False)
        except Exception as e:
            return JsonResponse("data doesnt exist with this id",safe=False)
        
        
        
    if request.method == 'POST':
        try : 
            emp_data = JSONParser().parse(request)
            emp_serializer = EmployeeSerializer(data = emp_data)
            if emp_serializer.is_valid():
                emp_serializer.save()
                return JsonResponse("ADDED SUCCESSFULLY!!!",safe = False)
            return JsonResponse("Data can't be added",safe = False)
        except Exception as e:
            return JsonResponse("cant add your data",safe=False)
    
    
    if request.method == 'PUT':
        try : 
            emp_data = JSONParser().parse(request)
            emp = Employee.objects.get(EmployeeId = id)
            emp_serializer = EmployeeSerializer(emp,data=emp_data)
            if emp_serializer.is_valid():
                emp_serializer.save()
                return JsonResponse("UPDATED SUCCESSFULLY!!!",safe = False)
            return JsonResponse("Data can't be updated",safe = False)
        except Exception as e:
            return JsonResponse("cant update",safe=False)
    
    
    if request.method == 'DELETE':
        try :
            emp = Employee.objects.get(EmployeeId = id)
            emp.delete()
            return JsonResponse("data deleted successfully",safe=False)
        except Exception as e:
            return JsonResponse("data doesnt exist",safe=False)
    
        
        
        
            
        
    
