from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.Employee_detail , name='Employee_detail')
]

