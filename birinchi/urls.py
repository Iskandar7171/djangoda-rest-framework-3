from django.urls import path
from .views import BirinchiListCreateAPiView

urlpatterns = [
    path('birinchi/', BirinchiListCreateAPiView.as_view(), name='birinchi-list-create'),
]