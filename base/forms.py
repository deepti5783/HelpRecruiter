from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length = 20, label = "username")    
    class Meta:
        model = CustomUser
        fields = ('email',)
        
class UserLoginForm(UserChangeForm):
    # add_form = UserCreationForm
     
    class Meta:
        model = CustomUser
        fields = ('email',)

class App_form(forms.ModelForm):
    contact_number = forms.CharField(max_length = 12)
    resume = forms.FileField()
    notice_period = forms.IntegerField()
    class Meta:
        model = CustomUser
        fields = ('firstname', 'lastname', 'email')

        def clean_email(self):
            email = self.cleaned_data.get("email")

            try:
                CustomUser.objects.get(email = email)
            except CustomUser.DoesNotExist:
                return email
            
            raise forms.ValidationError('This email address is already in use.')
