import datetime
from rest_framework import serializers
from ..models import Turno

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'

    def validate(self, data):
        fecha = data.get('fecha')
        hora = data.get('hora')
        peluquera = data.get('peluquera')

        turno_id = self.instance.id if self.instance else None

        if Turno.objects.filter(fecha=fecha, hora=hora, peluquera=peluquera).exclude(id=turno_id).exists():
            raise serializers.ValidationError("Ya hay un turno reservado para esta peluquera en esta fecha y hora.")

        return data

