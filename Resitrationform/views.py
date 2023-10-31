from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def HemoPage(request):
    pass
def SignupPage(request):
    if request.method=='POST':
       name=request.POST.get('username')
       mail=request.POST.get('email')
       password1=request.POST.get('passwaord')
       password2=request.POST.get('confirm')
       confirm1=request.POST.get('submit')
       
       if password1==password2:
          my_user=User.objects.create_user(name,mail,password1)
          my_user.save()
          return redirect('login')
       else:
          return HttpResponse("Your password and confirm password is not same")
    
    return render(request,'home.html')
             
def LoginPage(request):
    if request.method=='POST':
       name1=request.POST.get('username')
       password2=request.POST.get('passwaord')
       confirm2=request.POST.get('submit')
       user=authenticate(request,username=name1,password=password2)
       
       if user is not None:
           login(request,user)
           return redirect('mainn')
       else:
            return HttpResponse("Your username and  password is not same")
  
    return render(request,'login.html')

def HomePage(request):
    return render(request,'mainn.html')

    