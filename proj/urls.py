
from django.contrib import admin
from django.urls import path, include
from emp.views import *
from django.contrib.auth import views as auth_views
#from django.generic.base import RedirectView
from rest_framework import routers

router = routers.DefaultRouter()
urlpatterns = [
    #path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('admin/', admin.site.urls),
    path("",dashboard,name="home-page"),
    path("department/",department,name="department"),
    path("employee/",employee,name="employee"),
    path("task/",task,name="task"),
    path('manage_departments',manage_departments, name="manage_departments-page"),
    path('save_department',save_department, name="save-department-page"),
    path('delete_department', delete_department, name="delete-department"),
    path('view_employee', view_employee, name="view-employee-page"),
    path('manage_employees',manage_employees, name="manage_employees-page"),
    path('save_employee', save_employee, name="save-employee-page"),
    path('delete_employee', delete_employee, name="delete-employee"),
    path('view_task', view_task, name="view_task-page"),
    path('manage_task',manage_task, name="manage_task-page"),
    path('save_task', save_task, name="save_task-page"),
    path('delete_task',delete_task, name="delete-task"),
    path('add_new_task',add_new_task, name="add_new_task"),
    path('save_new_task', save_new_task, name="save_new_task"),

#######################################################################################

    path('api/', include(router.urls)),
    path('api/alldepartments/',DepartmentList.as_view()),
    path('api/getdepartment/<int:pk>',DepartmentRetrieve.as_view()),
    path('capi/createdepartment/',DepartmentCreate.as_view()),
    path('api/updatedepartment/<int:pk>',DepartmentUpdate.as_view()),
    path('api/deletedepartment/<int:pk>',DepartmentDestroy.as_view()),

    path('api/allemployee/',EmployeeList.as_view()),
    path('api/getemployee/<int:pk>',EmployeeRetrieve.as_view()),
    path('capi/createemployee/',EmployeeCreate.as_view()),
    path('api/updateemployee/<int:pk>',EmployeeUpdate.as_view()),
    path('api/deleteemployee/<int:pk>',EmployeeDestroy.as_view()),

    path('api/alltask/',TaskList.as_view()),
    path('api/gettask/<int:pk>',TaskRetrieve.as_view()),
    path('capi/createtask/',TaskCreate.as_view()),
    path('api/updatetask/<int:pk>',TaskUpdate.as_view()),
    path('api/deletetask/<int:pk>',TaskDestroy.as_view()),





    



] 
