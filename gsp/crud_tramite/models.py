from django.db import models

# Create your models here.

class Tramite (models.Model):
    def __str__(self):
        return "TRAMITE ID:" + str(self.pk) + " | RADICADO: " + self.numeroVentanilla + " | RECIBIDO: " + str(self.fechaRecepcion)
    
    TIPO_TRAMITE_CHOICES = [
        ('P', 'PETICION'),
        ('Q', 'QUEJA'),
        ('R', 'RECLAMO'),
        ('S', 'SUGERENCIA'),
        ('F', 'FELICITACION'),
    ]

    TIPO_MEDIO_CHOICES = [
        ('WE', 'WEB'),
        ('ES', 'ESCRITO'),
    ]

    TIPO_PETICIONARIO_CHOICES = [
        ('PRE', 'ESTUDIANTE PREGRADO'),
        ('POS', 'ESTUDIANTE POSGRADO'),
        ('EMP', 'EMPLEADO'),
        ('DOC', 'DOCENTE'),
        ('EGR', 'EGRESADO'),
        ('JUB', 'JUBILADO'),
        ('EXT', 'PERSONA EXTERNA'),
    ]

    numeroVentanilla = models.CharField(unique=True, max_length=20)
    tipoTramite = models.CharField(max_length=1, choices=TIPO_TRAMITE_CHOICES, default='P')
    asunto = models.CharField(max_length=4000)
    medioRecepcion = models.CharField(max_length=2, choices=TIPO_MEDIO_CHOICES, default='WE')
    fechaRecepcion = models.DateField(auto_now=False, auto_now_add=False)
    fechaVencimiento = models.DateField(auto_now=False, blank=True, auto_now_add=False)

    numeroOficio = models.CharField(blank=True, max_length=20)
    oficioRespuesta = models.CharField(blank=True, max_length=500)
    fechaRespuesta = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)

    nombrePeticionario = models.CharField(blank=True, max_length=80)
    tipoPeticionario = models.CharField(blank=True, max_length=3, choices=TIPO_PETICIONARIO_CHOICES, default='EXT')
    direccionPeticionario = models.CharField(blank=True, max_length=50)
    telefonoPeticionario = models.CharField(blank=True, max_length=12)
    celularPeticionario = models.CharField(blank=True, max_length=12)
    correoPeticionario = models.CharField(blank=True, max_length=64)


class Tramitante (models.Model):
    def __str__(self):
        return "TRAMITANTE ID:" + str(self.pk) + " | NOMBRE: " + self.nombreTramitante + " | DEPENDENCIA: " + self.dependenciaTramitante
    
    nombreTramitante = models.CharField(unique=True, max_length=80)
    correoTramitante = models.CharField(blank=True, max_length=64)
    dependenciaTramitante = models.CharField(max_length=200)


class Traslado(models.Model):
    def __str__(self):
        return "TRASLADO ID:" + str(self.pk) + " {TRAMITE: " + str(self.idTramite) + "} {TRAMITANTE: " + str(self.idTramitante) + "}"
    
    fechaTraslado = models.DateField(auto_now=False, auto_now_add=False)
    idTramite = models.ForeignKey(Tramite, on_delete=models.CASCADE)
    idTramitante = models.ForeignKey(Tramitante, on_delete=models.CASCADE)
