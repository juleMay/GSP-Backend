from rest_framework import serializers
from .models import Configuracion


class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = ['id', 'tipo_configuracion', 'tiempo_limite']