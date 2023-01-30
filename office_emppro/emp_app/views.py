from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import auth,User
from django.contrib import messages
from . models import *
from django.contrib.auth.decorators import login_required

from datetime import datetime
from django.db.models import Q

# Create your views here.


def index(request):
    return render(request,'index.html')
def register(request):
    print("request", request)
    print("request.method",request.method)
    print("request.session", request.session)
    print("request.POST",request.POST)
    print("request.GET", request.GET)

    for key,value in request.POST.items():
        print("key",key)
        print("value",value)

    if request.method == 'POST' and "login" in request.POST["submit"]:
        return redirect('login')
    if request.method == 'POST' and "register" in request.POST["submit"]:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']

        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        email=request.POST['email']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')

    else:
        return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'INVALID CREDENTIALS')
            return redirect('login')
    else:
      return render(request,'login.html')

def all_emp(request):
    emps= Employee.objects.all()
    context={
        'emps': emps
    }
    print(context)

    return render(request,'view_all_emp.html',context)

def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = request.POST['bonus']
        phone = request.POST['phone']
        dept = request.POST['dept']
        role = request.POST['role']

        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully")
    elif request.method=='GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse("An Exception Occured ! Employee has been not Added")
def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return  HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("Please enter a  valid emp id")
    emps =Employee.objects.all()
    context = {
        'emps' :emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps =Employee.objects.all()
        print("name list", emps)
        filter_emps = Employee.objects.filter(first_name="Kavya")
        print("name filter: ",filter_emps)
        if name:
            emps=emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps= emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {
            'emps' : emps
        }
        return render(request,'view_all_emp.html',context)
    elif request.method =='GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("An Exeption Occured")



    return render(request,'filter_emp.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


