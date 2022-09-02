from base.models import CustomUser,Organization,jobDescription,jobApplicant
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegistrationForm, UserLoginForm

class CustomUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    form = UserLoginForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','last_name', 'password1', 'password2', 'is_staff', 'is_active')
            }
        ),
       )
    search_fields = ('email',)
    ordering = ('email',)
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Organization)
admin.site.register(jobDescription)
admin.site.register(jobApplicant)
