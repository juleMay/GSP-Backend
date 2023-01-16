from rest_framework import serializers
from .models import Tramite, Traslado

class TrasladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traslado
        fields = ['id', 'fecha_traslado', 'id_tramitante']
        depth = 2

class TramiteSerializer(serializers.ModelSerializer):
    traslados = TrasladoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Tramite
        fields = ['id', 'numero_ventanilla', 'tipo_tramite', 'asunto_tramite', 'medio_recepcion', 'fecha_recepcion', 'fecha_vencimiento', 'numero_oficio', 'oficio_respuesta',
                  'fecha_respuesta', 'nombre_peticionario', 'tipo_peticionario', 'direccion_peticionario', 'telefono_peticionario', 'celular_peticionario', 'correo_peticionario', 'traslados' ]
