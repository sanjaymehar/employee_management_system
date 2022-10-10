from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import json
from rest_framework import generics
from .serializers import *

# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")

def department(request):
    #department_list = Department.objects.all()
    department_list = Department.objects.raw('SELECT * FROM emp_department')
    return render(request,'departments.html',{'department_list':department_list})

def manage_departments(request):
    department = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
            print(id)
        if id.isnumeric() and int(id) > 0:
            department = Department.objects.raw(f'SELECT * FROM emp_department WHERE emp_department.id = {id}')[0]
            #department = Department.objects.filter(pk=id).first()
            print(department)
    
    context = {
        'department' : department
    }
    return render(request, 'manage_department.html',context)

def save_department(request):
    data =  request.POST
    resp = {'status':'failed'}    
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 : 
            d_name=data['name']
            d_id=data['id']
            #save_department = Department.objects.filter(id = data['id']).update(department=data['name'])
            q=f'UPDATE emp_department SET department = \'{d_name}\' WHERE emp_department.id = {d_id}'
            Department.objects.raw(q)[:]
        else:
            d_name=data['name']
            q=f'INSERT INTO emp_department (department) VALUES (\'{d_name}\') RETURNING emp_department.id'
            Department.objects.raw(q)[:]
            #save_department = Department(department=data['name'])
        resp['status'] = 'success'
    except Exception as e:
        print(e)
        resp['status'] = 'success'
    return HttpResponse(json.dumps(resp), content_type="application/json")

def delete_department(request):
    data =  request.POST
    resp = {'status':''}
    try:
        d_id=data['id']
        resp['status'] = 'success'
        Department.objects.raw(f'DELETE FROM emp_department WHERE emp_department.id = {d_id}')[:]
        #Department.objects.filter(id = data['id']).delete()
        
    except:
        resp['status'] = 'success'
    return HttpResponse(json.dumps(resp), content_type="application/json")


def employee(request):
    #employee_list = Employee.objects.all()
    employee_list =Employee.objects.raw('SELECT * FROM emp_employee')
    return render(request,'employees.html',{'employee_list':employee_list})

def view_employee(request):
    employee = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employee.objects.raw(f'SELECT * FROM emp_employee WHERE emp_employee.id = {id}')[0]
            #employee = Employee.objects.filter(pk=id).first()
    context = {
        'employee' : employee,
        
    }
    return render(request, 'view_employee.html',context)

def manage_employees(request):
    employee = {}
    #departments = Department.objects.all() 
    departments =Department.objects.raw('SELECT * FROM emp_department')
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employee.objects.raw(f'SELECT * FROM emp_employee WHERE emp_employee.id = {id}')[0]
            #employee = Employee.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
     
    }
    return render(request, 'manage_employee.html',context)


def save_employee(request):
    data =  request.POST
    resp = {'status':'failed'}
    print(data)
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Employee.objects.filter(pk = data['id'])
        if check:
            d_id=data['department_id']
            e_id=data['id']
            name=data['firstname']
            salary=data['salary']
            #dept = Department.objects.filter(id=data['department_id']).first()
 
            q=f'UPDATE emp_employee SET name = \'{name}\', department_id = {d_id}, salary = {salary} WHERE emp_employee.id = {e_id}'
            Employee.objects.raw(q)[:]    

            #Employee.objects.filter(id = data['id']).update(name = data['firstname'],department = dept,salary = data['salary'])
        resp['status'] = 'success'

    else:
        try:
            d_id=data['department_id']
            e_id=data['id']
            name=data['firstname']
            salary=data['salary']
            # dept = Department.objects.filter(id=data['department_id']).first()
            # save_employee = Employee(name = data['firstname'],department= dept,salary = data['salary'])
            # save_employee.save()
            q=f'INSERT INTO emp_employee (name, salary, department_id) VALUES (\'{name}\', {salary}, {d_id}) RETURNING emp_employee.id'
            Employee.objects.raw(q)[:]
            resp['status'] = 'success'
        except Exception as e:
            resp['status'] = 'success'
            print(e)
    return HttpResponse(json.dumps(resp), content_type="application/json")

def delete_employee(request):
    data =  request.POST
    resp = {'status':''}
    try:
        #Employee.objects.filter(pk = data['id']).delete()
        e_id=data['id']
        Employee.objects.raw(f'DELETE FROM emp_employee WHERE emp_employee.id= {e_id}')[:]
        resp['status'] = 'success'
    except:
        resp['status'] = 'success'
    return HttpResponse(json.dumps(resp), content_type="application/json")

def task(request):
    #task_list = Task.objects.all()
    task_list =Task.objects.raw('SELECT * FROM emp_task')
    return render(request,'task.html',{'task_list':task_list})

def view_task(request):
    task = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
            print("aaaa",id)
        if id.isnumeric() and int(id) > 0:
            #task = Task.objects.filter(pk=id).first()
            task=Task.objects.raw(f'SELECT * FROM emp_task WHERE emp_task.id = {id}')[0]
    context = {
        'task' : task,
        
    }
    return render(request, 'view_task.html',context)

def manage_task(request):
    task = {}
    status = ["ACCEPTED","COMPLETED"]
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            #task = Task.objects.filter(id=id).first()
            task=Task.objects.raw(f'SELECT * FROM emp_task WHERE emp_task.id = {id}')[0]
    context = {
        'task' : task,
        'status' : status,
     
    }
    return render(request, 'manage_task.html',context)


def save_task(request):
    data =  request.POST
    resp = {'statuss':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            t_id=data['id']
            t_name=data['id']
            t_status=data['status']
            #save_task = Task.objects.filter(pk = data['id']).update(t_name=data['id'],status=data['status'])
            q=f'UPDATE emp_task SET t_name = \'{t_name}\', status = \'{t_status}\' WHERE emp_task.id = {t_id}'
            Task.objects.raw(q)[:]
           
            resp['statuss'] = 'success'
    except:
        resp['statuss'] = 'success'
    return HttpResponse(json.dumps(resp), content_type="application/json")


def delete_task(request):
    data =  request.POST
    resp = {'status':''}
    try:
        #Task.objects.filter(id = data['id']).delete()
        t_id=data['id']
        Task.objects.raw(f'DELETE FROM emp_task WHERE emp_task.id = {t_id}')[:]
        resp['status'] = 'success'
    except:
        resp['status'] = 'success'
    return HttpResponse(json.dumps(resp), content_type="application/json")


def add_new_task(request):
    status = ["ACCEPTED","COMPLETED"]
    #employee = Employee.objects.all() 
    employee =Employee.objects.raw('SELECT * FROM emp_employee')
    context = {
        'employee' : employee,
        'status' : status,
        
    }
    return render(request, 'add_new_task.html',context)


def save_new_task(request):
    data =  request.POST
    resp = {'status':''}
    try:
        # emp=Employee.objects.get(pk=data['employee_id']) 
        # Task(employee=emp,t_name=data['task_name'],status=data['status_id']).save()    
        e_id=data['employee_id']
        t_name=data['task_name']
        t_status=data['status_id']
        q=f'INSERT INTO emp_task (employee_id, t_name, status) VALUES ({e_id}, \'{t_name}\', \'{t_status}\') RETURNING emp_task.id'
        Task.objects.raw(q)[:]
        resp['status'] = 'success'
    except:

        resp['status'] = 'success'
    return HttpResponse(json.dumps(resp), content_type="application/json")

def signle_emp(request):
    emp=Employee.objects.all()
    return render(request,"single.html",{"emp":emp})

def emp_task(request):
    task = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
            print("aaaa",id)
        if id.isnumeric() and int(id) > 0:
            #task = Task.objects.filter(pk=id).first()
            task=Task.objects.raw(f'SELECT * FROM emp_task WHERE emp_task.id = {id}')[0]
    context = {
        'task' : task,
        
    }
    return render(request, 'single.html',context)

##############################################################################################################
class DepartmentList(generics.ListAPIView):
    queryset = Department.objects.raw('SELECT * FROM emp_department')
    serializer_class = DepartmentSerializer


class DepartmentCreate(generics.CreateAPIView):
    queryset = Department.objects.raw('SELECT * FROM emp_department')
    serializer_class = DepartmentSerializer

class DepartmentRetrieve(generics.RetrieveAPIView):
    queryset = Department.objects.raw('SELECT * FROM emp_department')
    serializer_class = DepartmentSerializer
    

class DepartmentUpdate(generics.UpdateAPIView):
    queryset = Department.objects.raw('SELECT * FROM emp_department')
    serializer_class = DepartmentSerializer


class DepartmentDestroy(generics.DestroyAPIView):
    queryset = Department.objects.raw('SELECT * FROM emp_department')
    serializer_class = DepartmentSerializer 



class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.raw('SELECT * FROM emp_employee')
    serializer_class = EmployeeSerializer


class EmployeeCreate(generics.CreateAPIView):
    queryset = Employee.objects.raw('SELECT * FROM emp_employee')
    serializer_class = EmployeeSerializer

class EmployeeRetrieve(generics.RetrieveAPIView):
    queryset = Employee.objects.raw('SELECT * FROM emp_employee')
    serializer_class = EmployeeSerializer
    

class EmployeeUpdate(generics.UpdateAPIView):
    queryset = Employee.objects.raw('SELECT * FROM emp_employee')
    serializer_class = EmployeeSerializer


class EmployeeDestroy(generics.DestroyAPIView):
    queryset = Employee.objects.raw('SELECT * FROM emp_employee')
    serializer_class = EmployeeSerializer 


class TaskList(generics.ListAPIView):
    queryset = Task.objects.raw('SELECT * FROM emp_task')
    serializer_class = TaskSerializer


class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.raw('SELECT * FROM emp_task')
    serializer_class = TaskSerializer

class TaskRetrieve(generics.RetrieveAPIView):
    queryset = Task.objects.raw('SELECT * FROM emp_task')
    serializer_class = TaskSerializer
    

class TaskUpdate(generics.UpdateAPIView):
    queryset = Task.objects.raw('SELECT * FROM emp_task')
    serializer_class = TaskSerializer


class TaskDestroy(generics.DestroyAPIView):
    queryset = Task.objects.raw('SELECT * FROM emp_task')
    serializer_class = TaskSerializer 
