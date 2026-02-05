from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializer import BirinchiSerializer
from .models import Salom1,Salom2,Salom3,Salom4,Salom5
# Create your views here.

class BirinchiListCreateAPiView(ListCreateAPIView):
    serializer_class = BirinchiSerializer
    queryset = Salom1.objects.all()