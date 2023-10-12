# from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('', views.home, name="home"),
    path('dept', views.dept,name="dept"),
    path('commerce', views.commerce, name="commerce"),
    # path('computer application', views.computer, name="computer application"),
    path('psychology', views.psychology, name="psychology"),
    path('physics', views.physics, name="physics"),
    path('chemistry', views.chemistry, name="chemistry"),
]