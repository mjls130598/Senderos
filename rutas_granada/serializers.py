from rest_framework_mongoengine import serializers
from rest_framework import serializers as serializer
from rutas_granada.models import Excursión

class ExcursiónSerializer(serializer.Serializer):
    nombre = serializer.CharField(label='Título', max_length=120, required=True)
    descripcion = serializer.CharField(label='Descripción de la ruta', max_length = 1000, required=True)
    tags = serializer.CharField(label= 'Etiquetas', max_length=120, required=True)
    fotos = serializer.ImageField()
    pie = serializer.CharField(label='Pie de foto', max_length=100)


class ExcursiónModelSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Excursión
        fields = ['nombre', 'descripción', 'tags', 'likes', 'visitas', 'fotos', 'comentarios']
