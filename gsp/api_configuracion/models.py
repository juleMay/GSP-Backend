from django.db import models

# Create your models here.


class Configuracion (models.Model):
    def __str__(self):
        return "CONFIGURACION ID:" + str(self.pk) + " | TIPO: " + self.tipo_configuracion + " | LIMITE: " + str(self.tiempo_limite) + " DIAS"
    
    TIPO_TRAMITE_CHOICES = [
        ('P', 'PETICION'),
        ('Q', 'QUEJA'),
        ('R', 'RECLAMO'),
        ('S', 'SUGERENCIA'),
    ]

    tipo_configuracion = models.CharField(unique=True, max_length=1, choices=TIPO_TRAMITE_CHOICES)
    tiempo_limite = models.IntegerField()