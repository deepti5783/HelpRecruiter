from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#from base.views import job_Description
from .models import CustomUser, JobApplicant

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

class ApplicationForm(forms.ModelForm):
    def __init__(self, **kwargs):

        self.base_fields['user'].initial = kwargs.pop('user', None)
        self.base_fields['job_description'].initial = kwargs.pop('job_description', None)
       

        super(ApplicationForm, self).__init__(**kwargs)
        print(self.fields)
 
    resume = forms.FileField() 
      
    class Meta:
        model = JobApplicant
        
        fields = '__all__'
        exclude = ['status']
   
    def save(self, commit=True, *args, **kwargs):
        u = super(ApplicationForm, self).save(commit=False, *args, **kwargs)
        if commit:
            u.save()
        return u    


'''class ApplicationForm(forms.ModelForm):
    #job_description = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 25)
    email = forms.EmailField(max_length = 50)
    contact_number = forms.CharField(max_length = 12)
    resume = forms.FileField()
    notice_period = forms.IntegerField()

    class Meta():
        model = JobApplicant
        fields = (
            
            'first_name',
            'last_name',
            'email',
            'contact_number',
            'resume',
            'notice_period',
            )  
    
    def save(self, commit = True):
        user = super(ApplicationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save(commit = True)
        return user
 
    def clean_email(self):
        email = self.cleaned_data.get("email")

        try:
            CustomUser.objects.get(email=email)

        except CustomUser.DoesNotExist:
            return email

        raise ValidationError('This email address is already in use.')
    
    '''