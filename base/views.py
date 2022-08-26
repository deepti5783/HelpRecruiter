from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from base.forms import UserRegistrationForm,UserLoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home_view(request):
   return render(request,"dashboard.html")


def register(request):
   context={}
   if request.POST:
      form=UserRegistrationForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('login')
      context['registration_form']=form
   else:
      form=UserRegistrationForm()
      context['registration_form']=form
   return render(request,'register.html') 


def login_view(request):
   context={}
   if request.POST:
      form=UserLoginForm(request.POST)
      if form.is_valid():
         email=request.POST['email']
         password=request.POST[password]
         user=authenticate(request,email=email,password=password)

         if user is not None:
            login(request,user)
            return redirect("dashboard")
      else:
         context['login_form']=form

   else:
      form=UserLoginForm()
      context["login_form"]=form      
    
   return render(request,'login.html')


def logout_view(request):
   logout(request)
   return redirect("login")
