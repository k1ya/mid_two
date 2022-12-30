from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.
class employeeUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=employee.objects.all()
    serializer_class=employeeSerializer
    
class employeeListCreate(generics.ListCreateAPIView):
    queryset=employee.objects.all()
    serializer_class=employeeSerializer