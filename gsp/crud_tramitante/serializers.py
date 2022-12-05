from rest_framework import serializers
from crud_tramite.models import Tramitante

class TramitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tramitante
        fields = ['id', 'nombre_tramitante', 'correo_tramitante', 'dependencia_tramitante']
