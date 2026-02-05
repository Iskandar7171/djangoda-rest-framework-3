from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializer import IkkinchiSerializer
from .models import Salom1,Salom2,Salom3,Salom4,Salom5


class IkkinchiListCreateAPiView(ListCreateAPIView):
    serializer_class = IkkinchiSerializer
    queryset = Salom1.objects.all()
# Create your views here.