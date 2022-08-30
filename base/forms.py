from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)
        
class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label = "password",
                            widget = forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

        if not AuthenticationForm(email = email, password = password):
            raise forms.ValidationError("invalid credential")