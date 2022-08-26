from dataclasses import fields
from distutils.log import error
from multiprocessing import context
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from base.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('first_name','last_name','email','contact_number')
        
class UserLoginForm(forms.ModelForm):
    password=forms.CharField(label="password",widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('email','password')

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password=self.cleaned_data['password']

        if not authenticate(email=email,password=password):
            raise forms.ValidationError("invalid credential")