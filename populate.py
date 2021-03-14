# populate.py

from mongoengine import connect, Document, EmbeddedDocument	
from mongoengine.fields import EmbeddedDocumentField, StringField, ListField, IntField, DateTimeField
from datetime import datetime

connect('senderos', host='mongo')

class Comentarios(EmbeddedDocument):
	contenido = StringField(required=True)
	autor     = StringField(max_length=120, required=True)
	fecha     = DateTimeField(default=datetime.now())

class Fotos(EmbeddedDocument):
	foto = StringField(required=True)
	pie = StringField(max_length=120, required=True)

class Excursión(Document):
	nombre      = StringField(max_length=120, required=True)
	descripción = StringField(required=True)
	likes       = IntField(default=0)
	visitas     = IntField(default=0)
	tags        = ListField(StringField(max_length=20))
	duración    = IntField(default=0)
	comentarios = ListField(EmbeddedDocumentField(Comentarios))
	fotos 		= ListField(EmbeddedDocumentField(Fotos)) 


comentarios = [
	{
		"contenido" : 'Primer comentario',
		"autor" : 'Yo'
	},
	{
		"contenido" : 'Otro comentario',
		"autor" : 'Pepito'
	}
]

fotos = [
	{
		"foto" : "./prado.png",
		"pie" : "Prado verde"
	}
]

excursión = Excursión(nombre="Prueba", descripción="asfd asf asdf", likes=1, 
                      tags=['fácil'], comentarios=comentarios, fotos=fotos)
excursión.save() # Para escribir en la BD


for excursion in Excursión.objects.all():
	print(excursion)