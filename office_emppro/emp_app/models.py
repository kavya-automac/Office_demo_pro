from django.db import models

# Create your models here.

class Department(models.Model):
    objects = models.Manager()
    name=models.CharField(max_length=100,null=False)
    location=models.CharField(max_length=100)

    def __str__(self):   # to display the dept name in admin page
        return self.name

class Role(models.Model):
    objects = models.Manager()
    name=models.CharField(max_length=100,null=False)

    def __str__(self):  # to display the role name in admin page
        return self.name


class Employee(models.Model):
    objects = models.Manager()
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary= models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    hire_date=models.DateField()


    def __str__(self):   # to display the  frstand lastnames and phnno. in admin page
        return "%s %s %s" %(self.first_name,self.last_name,self.phone)
