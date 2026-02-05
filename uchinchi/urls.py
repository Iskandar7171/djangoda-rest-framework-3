from django.urls import path
from .views import UchinchiListCreateAPiView

urlpatterns = [
    path('uchinchi/', UchinchiListCreateAPiView.as_view(), name='uchinchi-list-create'),
]