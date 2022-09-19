from base.models import CustomUser,Organization,JobDescription,JobApplicant
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegistrationForm

class CustomUserAdmin(UserAdmin):
    form = UserRegistrationForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password','username')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name','last_name', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')
            }
        ),
       )
    search_fields = ('email',)
    ordering = ('email',)
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Organization)
admin.site.register(JobDescription)
admin.site.register(JobApplicant)
