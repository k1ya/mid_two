from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class studentListCreate(generics.ListCreateAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer

class studentUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer
    