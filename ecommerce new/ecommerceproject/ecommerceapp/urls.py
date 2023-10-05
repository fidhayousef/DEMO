from django.urls import path
from . import views

app_name = 'ecommerceapp'
urlpatterns = [
    path('', views.allProductCategory, name='allProductCategory'),
    path('<slug:c_slug>/', views.allProductCategory, name='Products_BY_Category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetails,name='prodcatdetail'),
]
