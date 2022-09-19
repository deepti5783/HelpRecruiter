# import email
from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import JobApplicant

from .models import CustomUser, JobApplicant

'''class AuthenticationFormWithInactiveUsersOkay(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass'''

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)  
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
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

class App_form(forms.Form):
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 25)
    email = forms.EmailField(max_length = 50)
    contact_number = forms.CharField(max_length = 12)
    resume = forms.FileField()
    notice_period = forms.IntegerField()
    
    def save(self, commit = True):
        user = super(App_form, self).save(commit = False)
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
        



'''class App_form(forms.ModelForm):
    def __init__(self, **kwargs):

        self.base_fields['user'].initial = kwargs.pop('user', None)
        self.base_fields['jobDescription'].initial = kwargs.pop('jobDescription', None)

        super(App_form, self).__init__(**kwargs)
        print(self.fields)
    
    
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20) 
    resume = forms.FileField() 
    email = forms.EmailField(max_length = 50)
    contact_number = forms.CharField(max_length = 12)
    notice_period = forms.IntegerField()
    
      
    class Meta:
        model = JobApplicant
        widgets = {
            "user": forms.HiddenInput(),
            "jobDescription": forms.HiddenInput(),
            "status": forms.HiddenInput(),
        }
        fields = "__all__"
   
    def save(self, commit=True, *args, **kwargs):
        m = super(App_form, self).save(commit=False, *args, **kwargs)
        if commit:
            m.save()
        return m    

'''