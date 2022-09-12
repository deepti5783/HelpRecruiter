from django.contrib.auth.models import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from base.forms import UserRegistrationForm
# from django.contrib.auth import authenticate,login
from django.core.exceptions import ValidationError
from django.contrib import messages

# from django.http import HttpResponse
# from django.template import loader

# Create your views here.
def home_view(request):
   return render(request,"home.html")

def index(request):
   return render(request, "index.html")


def register(request):
   # context = {}
   if request.method == 'POST':
      form = UserRegistrationForm(request.POST)
      
      if form.is_valid():
         form.save()
         messages.success(request, "Your account has been created successfully.")     
         return redirect('/login')
      
      # context['registration_form'] = form
      # message.error(request, "Unsuccessfully registration, Invalid Information.")
   
   elif request.method == 'GET':
      form = UserRegistrationForm()

   else:
      return ValidationError("This is not correct method.")

   return render(request, 'register.html', {'form':form}) 
     
   

def login_view(request):
      if request.method == "POST":
         form = AuthenticationForm(request, data = request.POST)
         
         if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username = username, password = password)

            if user is not None:
               auth.login(request, user)
               messages.info(request, f"You are now logged in as {username}.")
               return redirect('/job_desc')
            
            else:
               messages.error(request,"Invalid email or password.")
               return redirect('/login')
         
         
      form = AuthenticationForm()     
      return render(request,'login.html', {'form':form})


def logout(request):
   return render(request, "logout.html")

def job_desc(request):
   return render(request, "jd.html")
