from django.urls import  path
from . import views

urlpatterns=[
    path('', views.teacherListCreate.as_view()),  
    path('update/<pk>', views.teacherUpdate.as_view()),
]