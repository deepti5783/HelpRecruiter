from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique = True)
    first_name = models.CharField(max_length = 20, null = True)
    last_name = models.CharField(max_length = 20, null = True)
    
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return (self.email)


class Organization(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 40)
    country = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    contact_number = models.CharField(max_length = 12)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name

class JobDescription(models.Model):
    JOB_CAT_CHOICES = (
        ('HR', 'HR'),
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Full stack', 'Full stack'),
        ('Dev Ops', 'Dev Ops'),
        ('BDE', 'BDE'),
        ('Others', 'Others'),
        )   
    
    EMPLOYMENT_CHOICES = (
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        )

    job_category = models.CharField(max_length = 30,choices = JOB_CAT_CHOICES)
    job_title = models.CharField(max_length = 30)
    job_location = models.CharField(max_length = 30)
    employment_type = models.CharField(max_length = 30,choices = EMPLOYMENT_CHOICES)
    organization = models.CharField(max_length = 40)
    mandatory_qualification = models.CharField(max_length = 40)
    optional_qualification = models.CharField(max_length = 40)
    experience = models.CharField(max_length=20)
    what_is_expected = models.CharField(max_length = 50)
    what_we_offer = (models.CharField(max_length = 50))

    def _str_(self):
        return self.job_title
class Meta:
        permissions = (
            ('read_item', 'can read item')
            )
class JobApplicant(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('in-progress', 'in-progress'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
        )
    
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name = 'applicants')
    job_description=models.ForeignKey(JobDescription,on_delete = models.CASCADE, related_name = 'applicants', null=True)
    resume = models.FileField(upload_to='Documents/')
    notice_period = models.IntegerField()
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES ,default='pending')

    def __str__(self):
        return str(self.user)
        