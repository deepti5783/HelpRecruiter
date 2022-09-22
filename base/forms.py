from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)  
    class Meta:
        model = CustomUser
        fields = ( 'email', 'password1', 'password2')
    def save(self, commit = True):
        user = super(UserRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
class UserLoginForm(UserChangeForm):
     
    class Meta:
        model = CustomUser
        fields = ("email",)

class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 25)
    email = forms.EmailField(max_length = 50)
    contact_number = forms.CharField(max_length = 12)
    resume = forms.FileField()
    notice_period = forms.IntegerField()
    
    
    def save(self, commit = True):
        user = super(ApplicationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
 
    def clean_email(self):
        email = self.cleaned_data.get("email")

        try:
            CustomUser.objects.get(email=email)

        except CustomUser.DoesNotExist:
            return email

        raise ValidationError('This email address is already in use.')
    
        