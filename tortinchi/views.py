from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializer import TortinchiSerializer
from .models import Salom1,Salom2,Salom3,Salom4,Salom5
# Create your views here.

class TortinchiListCreateAPiView(ListCreateAPIView):
    serializer_class = TortinchiSerializer
    queryset = Salom1.objects.all()
# Create your views here.
