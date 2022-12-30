from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.


class teacherUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=teacher.objects.all()
    serializer_class=teacherSerializer
    

    

    

    
class teacherListCreate(generics.ListCreateAPIView):
    queryset=teacher.objects.all()
    serializer_class=teacherSerializer
