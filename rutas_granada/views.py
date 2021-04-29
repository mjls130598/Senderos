from django.shortcuts import render
from django.http import HttpResponseRedirect
from rutas_granada import models
from .forms import ComentarioForm, ExcursionForm
import os
from django.conf import settings

def index(request):
	return render(request, "base.html")
					
def excursion(request, id):
	excursión = models.Excursión.objects.get(id = id)

	if request.method == "GET":
		excursión.visitas = excursión.visitas + 1
		excursión.save()
		context = {
			'excursión': excursión,
			'comentario': ComentarioForm()
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

def añadir_excursion(request):

	if request.method == "POST":
		form = ExcursionForm(request.POST, request.FILES)
		if form.is_valid():

			fotos = []
			pie = form.cleaned_data['pie']
			dire = os.path.join(settings.BASE_DIR, "rutas_granada", "static", "rutas_granada","images")

			for image in request.FILES.getlist('fotos'):
				fotos.append(models.Fotos(foto=image.name, pie = pie))
				try:
					file_n = os.path.join(dire, str(image))
					with open(file_n, "wb+") as dest:
						for chunk in image.chunks():
							dest.write(chunk)
				except:
					print("ERROR")


			excursión = models.Excursión(nombre = form.cleaned_data['nombre'], descripción = form.cleaned_data['descripcion'],
					tags = [form.cleaned_data['tags']], fotos = fotos)

			excursión.save()

			return HttpResponseRedirect("/excursion/")

	else: 
		context = {
			'excursión': ExcursionForm(),
		}

		return render(request, "rutas_granada/excursion-formulario.html", context)