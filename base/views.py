from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from base.forms import UserRegistrationForm
from django.contrib.auth import authenticate,login
from django.core.exceptions import ValidationError
from django.contrib import messages

# from django.http import HttpResponse
# from django.template import loader

# Create your views here.
def home_view(request):
   return render(request,"home.html")


def register(request):
   context = {}
   if request.method == 'POST':
      form = UserRegistrationForm(request.POST)
      
      if form.is_valid():
         form.save()
         messages.success(request, "Your account has been created successfully.")     
         return redirect(login.html)
      
      context['registration_form'] = form
      # message.error(request, "Unsuccessfully registration, Invalid Information.")
   
   elif request.method == 'GET':
      form = UserRegistrationForm()

   else:
      return ValidationError("This is not correct method.")

   return render(request, 'register.html', {'form':form}) 
     
   

def login_view(request):
   context = {}
   if request.POST:
      form = AuthenticationForm(request, data = request.POST)
      
      if form.is_valid():
         email = form.cleaned_data.get('email')
         password = form.cleaned_data.get('password')
         user = authenticate(email = email, password = password)

         if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {email}.")
            return redirect("home.html")
         else:
            messages.error(request,"Invalid email or password.")
      else:
         messages.error(request,"Invalid email or password.")

   form = AuthenticationForm()     
   return render(request,'login.html', {'form':form})


