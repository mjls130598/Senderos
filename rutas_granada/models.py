from django.db import models
from datetime import datetime

class Comentarios(models.Model):
	contenido = models.TextField()
	autor     = models.CharField(max_length=120)
	fecha     = models.DateTimeField(default=datetime.now())

class Fotos(models.Model):
	foto = models.CharField()
	pie = models.CharField(max_length=120)