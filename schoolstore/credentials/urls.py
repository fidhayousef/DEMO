# from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('commerce', views.commerce, name="commerce"),
    path('computer application', views.computer, name="computer application"),
    path('psychology', views.psychology, name="psychology"),
    path('physics', views.physics, name="physics"),
    path('chemistry', views.chemistry,name="chemistry"),
]