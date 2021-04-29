from django.urls import path
from . import views

urlpatterns = [
	path('excursion/', views.excursion_todas, name="excursiones"),
	path('excursion/<str:id>/', views.excursion, name = "excursion"),
	path('', views.index),
	path('buscar/', views.buscar),
	path('aniadir/', views.añadir_excursion, name="añadir"),
	path('editar/<str:id>/', views.editar_excursion, name="editar")
	]