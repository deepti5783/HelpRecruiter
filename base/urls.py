from django.urls import path, include
from . import views
# from . import views


urlpatterns = [
    # path('home/', views.home_view, name = "home"),
    path('index/', views.index, name = 'index'),
    path('', include('recruiter.urls'))
    # path('register/', register, name ="register.html"),
    # path('login/', login_view, name = "login"),
    # path('logout/', views.logout_view, name = "logout"),
    ]