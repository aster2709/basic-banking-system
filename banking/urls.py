from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.customer, name='customer'),
    path('transfer/', views.transfer, name='transfer'),
    path('log/', views.log, name='log'),
    path('customers/<int:customer_id>/', views.detail, name='detail'),
]
