from django.db import models
from datetime import datetime

class Comentario(models.Model):
	contenido = models.TextField()
	autor     = models.CharField(max_length=120)
	fecha     = models.DateTimeField(default=datetime.now())

class Foto(models.Model):
	foto = models.CharField()
	pie = models.CharField(max_length=120)

class Excursion(models.Model):
	nombre      = models.CharField(max_length=120)
	descripción = models.TextField()
	likes       = models.IntegerField(default=0)
	visitas     = models.IntegerField(default=0)
	tags        = models.ListField(models.CharField(max_length=20))
	duración    = models.IntegerField(default=0)
	comentarios = models.ForeignKey(Comentario, on_delete=models.CASCADE)
	fotos 		= models.ForeignKey(Foto, on_delete=models.CASCADE) 