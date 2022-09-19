
from django.contrib.auth.models import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login
from base.forms import UserRegistrationForm,App_form
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import JobDescription

# Create your views here.
def home(request):
   jds = JobDescription.objects.all()
   context = {'jds':jds}
   return render(request, "home.html", context)



def index(request):
   jds = JobDescription.objects.all()
   context = {'jds':jds}
   return render(request, "index.html", context)

  

def register(request):
   #context={}
   if request.method == 'POST':
      form = UserRegistrationForm(request.POST)
      
      if form.is_valid():
         user = form.save()
         login(request,user)
         return redirect('/')
      
      else:
         for error in list(form.errors.values()):
            print(request, error)
         
   else: 
      form = UserRegistrationForm()

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
               return redirect('index')
            
            else:
               messages.error(request,"Invalid email or password.")
               messages.error(request, form.errors)
               return redirect('/')
         
         
      form = AuthenticationForm()     
      return render(request,'login.html', {'form':form})



def logout(request):
   return render(request, "logout.html")


def job_Description(request):
      jobDescriptions = JobDescription.objects.all()
      context = { "jds": jobDescriptions}
      return render(request, "index.html", context)


def detail(request,pk):
   jobDescriptions = JobDescription.objects.filter(id = pk)
   context = {"jds":jobDescriptions}
   return render(request, 'job_description.html', context)


def app_form(request,pk):
   if request.method == 'POST':
      form = App_form(data = request.POST, files = request.FILES)
      if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('job_description.html', id = pk)

   form = App_form()
   context = {'form':form}
   return render(request,"app_form.html",context)
 
 