from django.shortcuts import render
from django.http import HttpResponseRedirect
from rutas_granada import models

def index(request):
	return render(request, "base.html")
					
def excursion(request, id):

	if request.method == "GET":
		excursión = models.Excursión.objects.get(id = id) 
		context = {
			'excursión': excursión
		}
		return render(request, "rutas_granada/excursion.html", context)

	if request.method == "POST":

		if(request.POST.get("method", "") == "delete"):
			excursión = models.Excursión.objects.get(id = id)
			excursión.delete()
			return HttpResponseRedirect("/excursion/")

def excursion_todas(request):
	context = {
		'excursiones': models.Excursión.objects.all()
	}
	return render(request, "rutas_granada/excursiones.html", context)

def buscar(request):

	context = {
		'excursiones': models.Excursión.objects.all()
	}

	return render(request, "rutas_granada/buscar.html", context)
