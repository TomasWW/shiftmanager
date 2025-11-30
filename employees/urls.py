from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('new/', views.employee_create, name='employee_create'),
]
