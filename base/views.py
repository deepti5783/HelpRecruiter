from django.contrib.auth.models import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from base.forms import UserRegistrationForm,App_form
from django.core.exceptions import ValidationError
from django.contrib import messages


# Create your views here.
def home_view(request):
   return render(request, "home.html")

   


def index(request):
   form = UserRegistrationForm()
   context = {'form':form}
   return render(request, "index.html", context)

  

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
               return redirect('/jobDescription')
            
            else:
               messages.error(request,"Invalid email or password.")
               return redirect('/login')
         
         
      form = AuthenticationForm()     
      return render(request,'login.html', {'form':form})



def logout(request):
   return render(request, "logout.html")


def job_Description(request):
   jobDescription = jobDescription.objects.all()
   context = { "jds": jobDescription}
   return render(request, "index.html", context)


def app_form(request):
   context = {}
   context['form'] = App_form()
   return render(request, "app_form.html",context)


