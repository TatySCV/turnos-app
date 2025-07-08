from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Turno(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    peluquera = models.ForeignKey('Peluquera', on_delete=models.SET_NULL, null=True, blank=True)  # agregado
    fecha = models.DateField()
    hora = models.TimeField()
    observaciones = models.TextField(blank=True)

    creado_en = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('fecha', 'hora', 'peluquera')  # evita choques de horario

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.cliente} ({self.servicio})"
