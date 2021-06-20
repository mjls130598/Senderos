from django.shortcuts import render
from django.http import HttpResponseRedirect
from rutas_granada import models
from .forms import ComentarioForm, ExcursionForm
import os
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
import logging
from rest_framework import viewsets
from rest_framework import permissions
from rutas_granada.serializers import ExcursiónSerializer

logger = logging.getLogger(__name__)

def index(request):
	return render(request, "base.html")
					
def excursion(request, id):
	excursión = models.Excursión.objects.get(id = id)

	if request.method == "GET":
		excursión.visitas = excursión.visitas + 1
		excursión.save()
		context = {
			'excursión': excursión,
			'comentario': ComentarioForm(),
			'formulario': ExcursionForm({
				"nombre": excursión.nombre, 
				"descripcion": excursión.descripción,
				"tags": ' '.join([str(elem) for elem in excursión.tags]),
				"pie": excursión.fotos[0].pie
			}),
		}

		logger.info(f"Obtener excursión {id}")

		return render(request, "rutas_granada/excursion.html", context)

	if request.method == "POST":

		if(request.POST.get("method", "") == "delete"):
			excursión.delete()
			logger.info(f"Borrada excursión {id}")
			return HttpResponseRedirect("/excursion/")

		if(request.POST.get("method", "") == "like"):
			excursión.likes = excursión.likes + 1
			excursión.save()

			logger.info(f"Añadido nuevo like en excursión {id}")

			return HttpResponseRedirect("/excursion/" + id)

		if(request.POST.get("method", "") == "comentario"):
			form = ComentarioForm(request.POST)

			if form.is_valid():
				comentario = models.Comentarios(contenido = form.cleaned_data['contenido'], 
						autor = form.cleaned_data['autor'])

				excursión.comentarios.append(comentario)
				excursión.save()

				logger.info(f"Añadido nuevo comentario en excursión {id}")
			
				return HttpResponseRedirect("/excursion/" + id)

			else:
				logger.error(f"No se ha podido crear comentario en excursión {id}")

def excursion_todas(request):
	context = {
		'excursiones': models.Excursión.objects.all(),
		'formulario': ExcursionForm()
	}
	logger.info(f"Muestra todas las excursiones")
	return render(request, "rutas_granada/excursiones.html", context)

def buscar(request):

	context = {
		'excursiones': models.Excursión.objects.all()
	}

	logger.info(f"Buscar excursión ...")

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
					logger.error("Error con las imágenes de las excursiones")


			excursión = models.Excursión(nombre = form.cleaned_data['nombre'], descripción = form.cleaned_data['descripcion'],
					tags = form.cleaned_data['tags'].split(" "), fotos = fotos)

			excursión.save()

			logger.info("Nueva excursión añadida correctamente")

			return HttpResponseRedirect("/excursion/")

		else:
			logger.error("No se ha podido insertar la nueva excursión")

def editar_excursion(request, id):

	excursión = models.Excursión.objects.get(id = id)

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
					logger.error("Error con las imágenes de las excursiones")


			excursión.nombre = form.cleaned_data['nombre']
			excursión.descripción = form.cleaned_data['descripcion']
			excursión.tags = form.cleaned_data['tags'].split(" ")
			excursión.fotos = fotos

			excursión.save()

			logger.info(f"Modificada la excursión {id} correctamente")

			return HttpResponseRedirect("/excursion/" + id)
		else:
			logger.error(f"Problema al modificar excursión {id}")

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)

			logger.info(f"Usuario {username} creado correctamente")

			return HttpResponseRedirect('/excursion/')

		else:
			logger.error("No se pudo crear el usuario")
			return render(request, 'registration/signup.html', {'form': form})
	else:
		form = UserCreationForm()
		return render(request, 'registration/signup.html', {'form': form})

class ExcursiónViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Excursión.objects.all()
    serializer_class = ExcursiónSerializer

