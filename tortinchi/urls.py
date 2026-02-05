from django.urls import path
from .views import TortinchiListCreateAPiView

urlpatterns = [
    path('tortinchi/', TortinchiListCreateAPiView.as_view(), name='tortinchi-list-create'),
]