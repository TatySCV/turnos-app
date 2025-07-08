from django.contrib import admin
from .models import Turno  # importa bien el modelo
from .models import Cliente, Servicio, Peluquera  # importa los otros modelos si es necesario

admin.register(Turno)

admin.register(Cliente)

admin.register(Servicio)

admin.register(Peluquera)