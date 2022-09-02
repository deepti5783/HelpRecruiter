from django.shortcuts import render,redirect
from base.forms import UserRegistrationForm,UserLoginForm
from email import message
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import ValidationError
# from django.http import HttpResponse
# from django.template import loader

# Create your views here.
def home_view(request):
   return render(request,"dashboard.html")


def register(request):
   context = {}
   if request.method == 'POST':
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
         form.save()
         message.success(request, "Your account has been created successfully.")
         return redirect('login')
      context['registration_form'] = form
   elif request.method == 'GET':
      form = UserRegistrationForm()

   else:
      return ValidationError("This is not correct method.")

   context = {
      'registration_form' : form
      }
   return render(request,'register.html', context) 
     

   


def login_view(request):
   context = {}
   if request.POST:
      form = UserLoginForm(request.POST)
      if form.is_valid():
         email = request.POST['email']
         password = request.POST[password]
         user = authenticate(request, email = email, password = password)

         if user is not None:
            login(request, user)
            return redirect("dashboard")
      else:
         context['login_form'] = form

   else:
      form = UserLoginForm()
      context["login_form"] = form      
    
   return render(request,'login.html')


def logout_view(request):
   message.success("logged out successfully")
   logout(request)
   
   return redirect('login.html')
