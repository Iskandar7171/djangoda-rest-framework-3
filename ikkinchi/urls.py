from django.urls import path
from .views import IkkinchiListCreateAPiView

urlpatterns = [
    path('ikkinchi/', IkkinchiListCreateAPiView.as_view(), name='ikkinchi-list-create'),
]