from django.urls import  path
from . import views

urlpatterns=[
    
    path('update/<int:pk>', views.employeeUpdate.as_view()),
    path('', views.employeeListCreate.as_view()),
    
]