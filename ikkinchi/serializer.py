from rest_framework.serializers import ModelSerializer
from .models import Salom1,Salom2,Salom3,Salom4,Salom5

class IkkinchiSerializer(ModelSerializer):
    class Meta:
        model = Salom1
        fields = '__all__'