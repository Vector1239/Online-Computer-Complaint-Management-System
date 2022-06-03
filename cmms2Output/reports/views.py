from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import *
from django.contrib.auth import authenticate,login,logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
import math, random

smail="";
def home(request):
     return render(request,'reports/homev2.html')

def slogin(request):
     if request.user.is_authenticated:
          return redirect('sdashB')
     return render(request, "reports/slogin.html")

def alogin(request):
     if request.user.is_authenticated:
          return redirect('sdashB')
     if request.method=='POST':
          al=request.POST.get('all')
          pall=request.POST.get('pall')

          user=authenticate(request,username=al,password=pall)

          if user is not None:
               login(request,user)
               return redirect('sdashB')
          else:
               messages.info(request,'Username or password is incorrect')
     return render(request, "reports/alogin.html")

def logoutUser(request):
     logout(request)
     return redirect('home')

def userLogs(request):
     if(insertM(smail)):
          user = authenticate(request, username=smail, password='student')
          login(request,user)
          return redirect('sdashB')
     else:
          return redirect('home')


@login_required(login_url='home')
def sdashB(request):
     getGroup()
     block=Block.objects.all()
     context={'block':block,'ug':ug}
     return render(request,"reports/sdashB.html",context)

@login_required(login_url='home')
def sdashL(request,pk_b):
     getGroup()    
     # print("here is",std_key)
     bl=Block.objects.get(bl_id=pk_b)
     rooms=bl.lab_set.all()
     context={'rooms':rooms,'bl':bl,'ug':ug}
     return render(request,"reports/sdashL.html",context)

@login_required(login_url='home')
def comp(request,pk_b,pk_l):
     getGroup()
     b1=Block.objects.get(bl_id=pk_b)
     rooms=Lab.objects.get(l_no=pk_l)
     comp=rooms.computer_set.all()
     context={'comp':comp,'b1':b1,'rooms':rooms,'ug':ug}     
     return render(request,"reports/comp.html",context)

@login_required(login_url='home')
@allowed_users(allowed_rules=['student'])
def thing(request,pk_b,pk_l,pk_c):
     b1=Block.objects.get(bl_id=pk_b)
     rooms=Lab.objects.get(l_no=pk_l)
     comp=rooms.computer_set.all()
     context1={'comp':comp,'b1':b1,'rooms':rooms}   
     cid=pk_c
     orig=Computer.objects.get(c_id=pk_c)
     context={'b1':b1,'rooms':rooms,'cid':cid,'orig':orig}
     all=['Keyboard','Mouse','Monitor','OS','Internet']
     res=[0,0,0,0,0]
     c=0

     if request.method=="POST":
          if request.POST.get('r_other'):
               word=request.POST.get('r_other')
               word=word.split()
               for i in all:
                    flag=0
                    for j in word:
                         if i==j:
                              res[c]=1
                              c+=1
                              flag+=1
                    if flag==0:
                         c+=1
               insertR(res,pk_c)
          else:
               messages.success(request,"Please select an Option.")
               return render(request,"reports/thing.html",context)     
          return redirect('/dashboard/navigation/'+str(pk_b)+'/'+str(pk_l)+'/room/')
               # if(any(res)==0):
               #      print("i am here")
               # return redirect('student_dashboard/navigation/'+str(pk_b)+'/'+str(pk_l)+'/'+str(pk_c)+'/report/')
     else:
          return render(request,"reports/thing.html",context)

@allowed_users(allowed_rules=['adminFR'])
def issue(request,pk_b,pk_l,pk_c):
     b1=Block.objects.get(bl_id=pk_b)
     rooms=Lab.objects.get(l_no=pk_l)
     comp=rooms.computer_set.all()
     orig=Computer.objects.get(c_id=pk_c)
     r=Report.objects.get(comp_id=pk_c)
     res=[]
     #starting from 1
     if r.r_mouse==1:
          res.append('Mouse')
     if r.r_keyboard==1:
          res.append('Keyboard')
     if r.r_monitor==1:
          res.append('Monitor')
     if r.r_OS==1:
          res.append('OS')
     if r.r_internet==1:
          res.append('Internet')
     context={'b1':b1,'rooms':rooms,'comp':comp,'r':r,'res':res,'orig':orig}

     if request.method=="POST":
          r.delete()
          p=Computer.objects.get(c_id=pk_c)
          p.c_status=0
          p.save()
          return redirect('/dashboard/navigation/'+str(pk_b)+'/'+str(pk_l)+'/aroom/')

     return render(request, "reports/issue.html",context)

def acomp(request,pk_b,pk_l):
     print("here")
     b1=Block.objects.get(bl_id=pk_b)
     rooms=Lab.objects.get(l_no=pk_l)
     comp=rooms.computer_set.all()
     context={'comp':comp,'b1':b1,'rooms':rooms}  
     return render(request, "reports/acomp.html",context)


def getGroup():
     from django.contrib.auth.models import Group
     global ug
     ug = Group.objects.get(name="student").user_set.all()

def insertR(res,pk_c):
     a=Report()
     p=Computer.objects.get(c_id=pk_c)
     a.comp_id=p
     a.r_mouse=res[0]
     a.r_keyboard=res[1]
     a.r_monitor=res[2]
     a.r_OS=res[3]
     a.r_internet=res[4]
     f=Student.objects.get(std_email=smail)
     a.std_mail=f
     a.save()
     p.c_status=1
     p.save()


def insertM(smail):
     if smail=="":
          return None
     from reports.models import Student
     from django.contrib.auth import get_user_model
     from django.contrib.auth.models import User,Group
     a=Student.objects.all()
     flag=0
     for i in a:
          if smail==str(i):
               print("herer lol ",i)
               flag+=1
               break         
     if flag==0:
          std=Student()
          std.std_email=smail
          std.save()

     UserModel = get_user_model()

     if not UserModel.objects.filter(username=smail).exists():
         user=UserModel.objects.create_user(smail, password='student')
         user.is_superuser=False
         user.is_staff=False
         user.save()
     my_group = Group.objects.get(name='student')
     my_users = User.objects.filter(username=smail)
     for my_user in my_users:
           my_group.user_set.add(my_user)

     if User.objects.filter(username=smail).exists():
          return True
     else:    
          return False


def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_otp(request):
     email=request.POST.get("email")
     global smail
     smail=email
     print(email)
     o=generateOTP()
     htmlgen = f"<p>Your OTP is <strong> {o} </strong></p>"
     send_mail('OTP request',o,'CMMS',[email], fail_silently=False, html_message=htmlgen)
     print(o)
     return HttpResponse(o)