from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
# class Salary(models.Model):
#     amount=models.PositiveIntegerField()

class Department(models.Model):
    department=models.CharField( max_length = 200)

    def __str__(self):
        return self.department

# class Manager(models.Model):
#     pass

class Employee(models.Model):
    name=models.CharField(max_length=50)
    salary=models.PositiveIntegerField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='dept')
    
    def __str__(self):
        return self.name

class Task(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='e_task')
    t_name=models.CharField(max_length=50)
    status=models.CharField( max_length = 20, choices=[("ACCEPTED","ACCEPTED"),("COMPLETED","COMPLETED")])



