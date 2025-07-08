from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    
    TIPO_CHOICES = [
        ('bebe', 'Bebé'),
        ('niña', 'Niña'),
        ('niño', 'Niño'),
        ('mujer', 'Mujer'),
        ('hombre', 'Hombre'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"
