from django.urls import path
from . import views

urlpatterns = [
	path('excursion/', views.excursion_todas, name="excursiones"),
	path('excursion/<str:id>/', views.excursion, name = "excursion"),
	path('', views.index),
	path('buscar/', views.buscar),
	path('aniadir/', views.añadir_excursion, name="añadir"),
	path('editar/<str:id>/', views.editar_excursion, name="editar"),
	path('signup/', views.signup, name='signup'),
	path('api/excursiones/', views.ExcursionesView.as_view(), name="excursiones_api"),
	path('api/excursion/<str:id>/', views.ExcursiónView.as_view(), name = "excursion_api"),
	]