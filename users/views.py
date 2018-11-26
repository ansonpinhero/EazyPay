# users/views.py
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required , user_passes_test
from .forms import CustomUserCreationForm
from django.shortcuts import render_to_response, redirect , render
from django.template import RequestContext
from .models import  CustomUser,JobProfile , BankProfile ,Salary
from django import forms
from django.utils import timezone
from .forms import JobProfileForm,BankForm , SalaryForm
import datetime
hra=2000
ma=500
da=500
JOB_CODES = {
                'P1':'Professor',
                'P2':'Associate Professor',
                'P3':'Assistant Professor',
                'L1':'Lab Assistant',
            }
PAY = {
                'P1': 1000,
                'P2': 800,
                'P3': 600,
                'L1': 100,  
     }
DEP_CODES = {
                'CSE':'Computer Science and Engineering ',
                'ME':'Mechanical Engineering',
                'ECE':'Electronics & Communication Engineering',
                'EEE':'Electrical & Electronics Engineering',
                'CE':'Civil Engineering',
                'AE':'Automobile Engineering',
                'BSH':'Basic Science and Humanities',
            }
MONTH={
        '1':'Januvary',
        '2':'Februvary',
        '3':'March',
        '4':'April',
        '5':'May',
        '6':'June',
        '7':'July',
        '8':'August',
        '9':'September',
        '10':'October',
        '11':'November',
        '12':'December',
        
      }
    

#class SignUp(generic.CreateView):
 #   form_class = CustomUserCreationForm
 #   success_url = reverse_lazy('login')
 #   template_name = 'signup.html'

def check_admin(request):
   return request.user.is_superuser
@login_required(login_url = '/users/login/')
#@user_passes_test(check_admin)
def SignUp(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                #username = form.cleaned_data.get('username')
                #raw_password = form.cleaned_data.get('password1')
                #user = authenticate(username=username, password=raw_password)
                #login(request, user)
                #return redirect('home')
                return render(request, 'success-user.html')
        else:
            form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return render(request, 'unauthorized.html')
        
    
@login_required(login_url = '/users/login/')    
def Dashboard(request):
    d=JobProfile.objects.filter(user=request.user).values('department','job_title')
    b=BankProfile.objects.filter(user=request.user).values('bank_name','bank_ifsc','bank_accountno')
    bname=b[0]['bank_name']
    bifsc=b[0]['bank_ifsc']
    baccno=b[0]['bank_accountno']
    dept=DEP_CODES[d[0]['department']]
    job_name=JOB_CODES[d[0]['job_title']]
    return render(request, 'home.html', {'dept':dept,'job_name':job_name,'b_name':bname,'b_ifsc':bifsc,'b_accno':baccno})

def AllUsers(request):
    allusers=CustomUser.objects.all().values('username','date_joined','last_login','email','first_name','last_name')
    
    users=[]
    for i in range(len(allusers)):
        users.append({"username":allusers[i]['username'],"date_joined":allusers[i]['date_joined'],"last_login":allusers[i]['last_login'],
            "email":allusers[i]['email'],"first":allusers[i]['first_name'],"last":allusers[i]['last_name']
        })
  
    
    return render(request, 'users.html',{"user_name":users})
def SalaryLog(request):
    allusers=Salary.objects.all().values('user','amount','hours','created_date','month','id')

    a=CustomUser.objects.prefetch_related('relatedusers').values("id","first_name","last_name")
    
    log=[]
    for i in range(len(allusers)):
        for j in range(len(a)):
            aa=a[j]["id"]
            bb=allusers[i]['user']
            if(aa==bb):
                f=a[j]["first_name"]
                l=a[j]["last_name"]
        log.append({"first":f,"last":l,"amount":allusers[i]['amount'],
            "hours":allusers[i]['hours'],"created_date":allusers[i]['created_date'],"month":MONTH[allusers[i]['month']]
        })
  
    
    return render(request, 'salarylog.html',{"log":log})
def SalaryUser(request):
    allusers=Salary.objects.all().values('user','amount','hours','created_date','month','id')

    a=CustomUser.objects.prefetch_related('relatedusers').values("id","first_name","last_name")
    
    log=[]
    person=request.user.id
    for i in range(len(a)):

        bb=allusers[i]['user']
        if(person==bb):
            f=request.user.first_name
            l=request.user.last_name
            log.append({"first":f,"last":l,"amount":allusers[i]['amount'],
            "hours":allusers[i]['hours'],"created_date":allusers[i]['created_date'],"month":MONTH[allusers[i]['month']]
        })
  
    
    return render(request, 'salaryuser.html',{"log":log})
def job(request):
 
    if request.method == "POST":
        form = JobProfileForm(request.POST)

        if form.is_valid():
            person=request.POST['user']
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.identify= model_instance.user
            #model_instance.save()
            form.save()
            return render(request, 'success.html')
        else:
            return render(request, 'error.html')
       
 
    else:
 
        form = JobProfileForm()
 
        return render(request, "job.html", {'form': form})
def bank(request):
 
    if request.method == "POST":
        form = BankForm(request.POST)
       
        if form.is_valid():
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            #model_instance.save()
            form.save()
            return render(request, 'success.html')
        else:
            return render(request, 'error.html')
       
 
    else:
 
        form = BankForm()
 
        return render(request, "bank.html", {'form': form})
def salary(request):
    d=JobProfile.objects.all().values("identify",'department','job_title')

    
    if request.method == "POST":
        form = SalaryForm(request.POST)
        
        if form.is_valid():
            
            for j in range(len(d)):
                aa=d[j]["identify"]
                bb=int(request.POST['user'])
                if(aa==bb):
                    paygrade=d[j]['job_title']
               
            
            
            
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            hrs=int(request.POST['hours'])
            model_instance.amount= PAY[paygrade]*hrs+hra+da+ma
        
            model_instance.pay_grade=paygrade
            model_instance.save()
           
            return render(request, 'success.html')
        else:
            return render(request, 'error.html')
       
 
    else:
 
        form = SalaryForm()
 
        return render(request, "salary.html", {'form': form})