from django.urls import path, include
from . import views
# from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('', include('recruiter.urls')),
]
    
    