from django.db import models

# Create your models here.


class Tramite (models.Model):
    class Meta:
        verbose_name = _("Tramite")
        verbose_name_plural = _("Tramites")

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

    numeroVentanilla = models.CharField(
        _("Numero Radicado de Ventanilla"), unique=True, max_length=20)
    tipoTramite = models.CharField(
        _("Tipo de Tramite"), max_length=1, choices=TIPO_TRAMITE_CHOICES, default='P')
    asunto = models.CharField(_("Asunto"), max_length=4000)
    medioRecepcion = models.CharField(
        _("Medio de Recepcion"), max_length=2, choices=TIPO_MEDIO_CHOICES)
    fechaRecepcion = models.DateField(
        _("Fecha de Recepcion"), auto_now=False, auto_now_add=False)
    fechaVencimiento = models.DateField(
        _("Fecha de Vencimiento"), auto_now=False, blank=True, auto_now_add=False)

    numeroOficio = models.CharField(
        _("Numero de Oficio"), blank=True, max_length=20)
    oficioRespuesta = models.CharField(
        _("Oficio de Respuesta"), blank=True, max_length=500)
    fechaRespuesta = models.DateField(
        _("Fecha de Respuesta"), auto_now=False, blank=True, auto_now_add=False)

    nombrePeticionario = models.CharField(
        _("Nombre de Peticionario"), blank=True, max_length=80)
    tipoPeticionario = models.CharField(_("Tipo de Peticionario"), blank=True,
                                        max_length=3, choices=TIPO_PETICIONARIO_CHOICES, default='EXT')
    direccionPeticionario = models.CharField(
        _("Direccion de Petionario"), blank=True, max_length=50)
    telefonoPeticionario = models.IntegerField(
        _("Telefono de Peticionario"), blank=True,)
    celularPeticionario = models.IntegerField(
        _("Celular de Peticionario"), blank=True,)
    correoPeticionario = models.CharField(
        _("Correo de Peticionario"), blank=True, max_length=64)


class Tramitante (models.Model):
    class Meta:
        verbose_name = _("Tramitante")
        verbose_name_plural = _("Tramitantes")

    nombreTramitante = models.CharField(
        _("Nombre de Tramitante"), unique=True, max_length=80)
    correoTramitante = models.CharField(
        _("Correo de Peticionario"), blank=True, max_length=64)
    dependenciaTramitante = models.CharField(
        _("Correo de Peticionario"), max_length=200)
    
    
class Traslado(models.Model):
    class Meta:
        verbose_name = _("Traslado")
        verbose_name_plural = _("Traslados")
        
    fechaTraslado = models.DateField(
        _("Fecha de Traslado"), auto_now=False, auto_now_add=False)
    idTramite = models.ForeignKey(Tramite, verbose_name=_("Id del Tramite"), on_delete=models.CASCADE)
    idTramitante = models.ForeignKey(Tramitante, verbose_name=_("Id del Tramitante"), on_delete=models.CASCADE)
