from django.shortcuts import render
from django.http import HttpResponseRedirect
from rutas_granada import models
from .forms import ComentarioForm, ExcursionForm
import os
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

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
		'excursiones': models.Excursión.objects.all(),
		'formulario': ExcursionForm()
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
					tags = form.cleaned_data['tags'].split(" "), fotos = fotos)

			excursión.save()

			return HttpResponseRedirect("/excursion/")

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
					print("ERROR")


			excursión.nombre = form.cleaned_data['nombre']
			excursión.descripción = form.cleaned_data['descripcion']
			excursión.tags = form.cleaned_data['tags'].split(" ")
			excursión.fotos = fotos

			excursión.save()

			return HttpResponseRedirect("/excursion/" + id)

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		print(form)	

		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect('/excursion/')

		else:
			return render(request, 'registration/signup.html', {'form': form})
	else:
		form = UserCreationForm()
		return render(request, 'registration/signup.html', {'form': form})
