from rest_framework_mongoengine import serializers
from rutas_granada.models import Excursión, Comentarios

class ExcursiónModelSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Excursión
        fields = ['id','nombre', 'descripción', 'tags', 'likes', 'visitas', 'fotos', 'comentarios']

class ComentarioModelSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = Comentarios
        fields = ['contenido','autor', 'fecha']
