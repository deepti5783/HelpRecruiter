"""recruiter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.job_Description, name = "jobDescription"),
    path('register/', views.register, name ="register"),
    path('login/', views.login_view, name = "login"),
    path('logout/', views.logout, name = "logout" ),
    path("detail/<str:pk>/",views.detail,name = "detail"),
    path("detail/app_form/<str:pk>/",views.app_form,name = "apply"),
    path('index/',views.index, name = "index"),
    path("applied-jobs/",views.applied_job,name='applied'),
    
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)