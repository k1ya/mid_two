from django.urls import  path
from . import views

urlpatterns=[
    path('', views.studentListCreate.as_view()),
    path('update/<int:pk>',views.studentUpdate.as_view()),
    ]