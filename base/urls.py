from django.contrib import admin
from django.urls import path
from base.views import home_view, register,login_view
# from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name = "home"),
    path('register/', register, name ="register.html"),
    path('login/', login_view, name = "login"),
    # path('logout/', logout_view, name = "logout"),
    ]