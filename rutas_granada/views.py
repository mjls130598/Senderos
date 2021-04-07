from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('Hola desde index')
					
def excursion(request, número):
	detalle = Consulta_Model(excursion=número) 
	context = {
		'excursion': número, # se pasan las variables al template
		'detalle': detalle
	}
	return render(request, "excursion.html", context)