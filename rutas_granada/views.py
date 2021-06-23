from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from rutas_granada import models
from .forms import ComentarioForm, ExcursionForm
import os
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rutas_granada.serializers import ExcursiónModelSerializer
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS

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

def borrar_excursion(request, id):
	if request.method == "POST":
		excursión = models.Excursión.objects.get(id = id)
		excursión.delete()
		logger.info(f"Borrada excursión {id}")
		return HttpResponseRedirect("/excursion/")

def aniadir_comentario(request, id):
	if request.method == "POST":
		excursión = models.Excursión.objects.get(id = id)
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

def cambiar_like(request, id):
	excursión = models.Excursión.objects.get(id = id)
	like = request.GET.get("like")

	if like == "true":
		excursión.likes += 1
	else:
		excursión.likes -= 1
	
	excursión.save()

	logger.info(f"Modificado likes de excursión {id}")

	return HttpResponse(excursión.likes)
		

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

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class ExcursiónView(APIView):

	permission_classes = [IsAdminUser | ReadOnly]
    
	def get_object(self, id):
		try:
			return models.Excursión.objects.get(id=id)
		except models.Excursión.DoesNotExist:
			raise Http404

	def get(self, request, id, format=None):
		excursion = self.get_object(id)
		serializer = ExcursiónModelSerializer(excursion)
		return Response(serializer.data)

	def put(self, request, id, format=None):
		excursion = self.get_object(id)
		serializer = ExcursiónModelSerializer(excursion, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, id, format=None):
		excursion = self.get_object(id)
		excursion.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class ExcursionesView(APIView):

	permission_classes = [IsAdminUser | ReadOnly]

	def get(self, request):
		return Response(ExcursiónModelSerializer(models.Excursión.objects.all(), many=True).data)

	def post(self, request):
		serializer = ExcursiónModelSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

