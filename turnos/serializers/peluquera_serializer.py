import datetime
from rest_framework import serializers
from ..models import Peluquera

class PeluqueraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peluquera
        fields = '__all__'
        

