from django.shortcuts import render
from django.http import HttpResponse
from rutas_granada import models

def index(request):
	return render(request, "base.html")
					
def excursion(request, id):
	excursión = models.Excursión.objects.get(id = id) 
	context = {
		'excursión': excursión
	}
	return render(request, "rutas_granada/excursion.html", context)

def excursion_todas(request):
	context = {
		'excursiones': models.Excursión.objects.all()
	}
	return render(request, "rutas_granada/excursiones.html", context)