from rest_framework_mongoengine import serializers
from rutas_granada.models import Excursión

class ExcursiónModelSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Excursión
        fields = ['nombre', 'descripción', 'tags', 'likes', 'visitas', 'fotos', 'comentarios']
