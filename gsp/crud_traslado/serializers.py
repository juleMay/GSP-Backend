from rest_framework import serializers
from crud_tramite.models import Traslado


class TrasladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traslado
        fields = ['id', 'fecha_traslado', 'id_tramite', 'id_tramitante']
        depth = 2