from django.shortcuts import render
# Create your views here.
from rest_framework.generics import ListCreateAPIView
from .serializer import UchinchiSerializer
from .models import Salom1,Salom2,Salom3,Salom4,Salom5
# Create your views here.

class UchinchiListCreateAPiView(ListCreateAPIView):
    serializer_class = UchinchiSerializer
    queryset = Salom1.objects.all()