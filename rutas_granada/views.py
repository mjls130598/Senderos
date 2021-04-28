from django.shortcuts import render
from django.http import HttpResponseRedirect
from rutas_granada import models
from .forms import ComentarioForm

def index(request):
	return render(request, "base.html")
					
def excursion(request, id):
	excursión = models.Excursión.objects.get(id = id)

	if request.method == "GET":
		excursión.visitas = excursión.visitas + 1
		excursión.save()
		comentarioForm = ComentarioForm()
		context = {
			'excursión': excursión,
			'comentario': comentarioForm
		}

		return render(request, "rutas_granada/excursion.html", context)

	if request.method == "POST":

		if(request.POST.get("method", "") == "delete"):
			excursión.delete()
			return HttpResponseRedirect("/excursion/")

		if(request.POST.get("method", "") == "like"):
			excursión.likes = excursión.likes + 1
			excursión.save()
			return HttpResponseRedirect("/excursion/" + id)

		if(request.POST.get("method", "") == "comentario"):
			form = ComentarioForm(request.POST)

			if form.is_valid():
				comentario = models.Comentarios(contenido = form.cleaned_data['contenido'], 
						autor = form.cleaned_data['autor'])

				excursión.comentarios.append(comentario)
				excursión.save()
			
				return HttpResponseRedirect("/excursion/" + id)

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
