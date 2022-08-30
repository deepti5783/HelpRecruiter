from django.urls import path
from base.views import home_view, register,login_view,logout_view
from . import views

urlpatterns = [
    path('', home_view, name = "home"),
    path('register/', views.register, name ="register"),
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
    ]