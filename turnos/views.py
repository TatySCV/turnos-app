from django.shortcuts import render
from .serializers.turno_serializer import TurnoSerializer
from .serializers.cliente_serializer import ClienteSerializer
from .serializers.peluquera_serializer import PeluqueraSerializer
from .serializers.servicio_serializer import ServicioSerializer
from .models import Turno, Cliente, Servicio, Peluquera
from rest_framework import viewsets

class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer
    
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer  # Assuming you have a serializer for Cliente
    
class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer  # Assuming you have a serializer for Servicio
    
class PeluqueraViewSet(viewsets.ModelViewSet):
    queryset = Peluquera.objects.all()
    serializer_class = PeluqueraSerializer  # Assuming you have a serializer for Peluquera

# Create your views here.
