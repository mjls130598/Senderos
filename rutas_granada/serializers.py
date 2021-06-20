from rutas_granada.models import Excursión
from rest_framework import serializers

class ExcursiónSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Excursión
        fields = ['nombre', 'descripción', 'likes', 'visitas',
            'flags', 'comentarios', 'fotos']
