from django.db import models

# Create your models here.


class Tramite (models.Model):
    def __str__(self):
        return "TRAMITE ID:" + str(self.pk) + " | RADICADO: " + self.numero_ventanilla + " | RECIBIDO: " + str(self.fecha_recepcion)

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

    numero_ventanilla = models.CharField(unique=True, max_length=20)
    tipo_tramite = models.CharField(
        max_length=1, choices=TIPO_TRAMITE_CHOICES, default='P')
    asunto_tramite = models.CharField(max_length=4000)

    medio_recepcion = models.CharField(
        max_length=2, choices=TIPO_MEDIO_CHOICES, default='WE')
    fecha_recepcion = models.DateField(auto_now=False, auto_now_add=False)
    fecha_vencimiento = models.DateField(
        null=True, blank=True, auto_now=False, auto_now_add=False)

    numero_oficio = models.CharField(blank=True, max_length=20)
    oficio_respuesta = models.CharField(blank=True, max_length=500)
    fecha_respuesta = models.DateField(
        null=True, blank=True, auto_now=False, auto_now_add=False)

    nombre_peticionario = models.CharField(blank=True, max_length=80)
    tipo_peticionario = models.CharField(
        blank=True, max_length=3, choices=TIPO_PETICIONARIO_CHOICES, default='EXT')
    direccion_peticionario = models.CharField(blank=True, max_length=50)
    telefono_peticionario = models.CharField(blank=True, max_length=12)
    celular_peticionario = models.CharField(blank=True, max_length=12)
    correo_peticionario = models.CharField(blank=True, max_length=64)


class Tramitante (models.Model):
    def __str__(self):
        return "TRAMITANTE ID:" + str(self.pk) + " | NOMBRE: " + self.nombre_tramitante + " | DEPENDENCIA: " + self.dependencia_tramitante

    nombre_tramitante = models.CharField(unique=True, max_length=80)
    correo_tramitante = models.CharField(blank=True, max_length=64)
    dependencia_tramitante = models.CharField(max_length=200)


class Traslado(models.Model):
    def __str__(self):
        return "TRASLADO ID:" + str(self.pk) + " {TRAMITE: " + str(self.id_tramite) + "} {TRAMITANTE: " + str(self.id_tramitante) + "}"

    fecha_traslado = models.DateField(auto_now=False, auto_now_add=False)
    id_tramite = models.ForeignKey(Tramite, on_delete=models.CASCADE)
    id_tramitante = models.ForeignKey(Tramitante, on_delete=models.CASCADE)
