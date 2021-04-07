from django.db import models

class Excursión(models.Model):
	nombre      = models.CharField(max_length=100)
	descripción = models.CharField(max_length=1000)
	likes       = models.IntegerField(default=0)