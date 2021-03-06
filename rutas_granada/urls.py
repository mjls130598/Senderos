from django.urls import path
from . import views

urlpatterns = [
	path('excursion/', views.excursion_todas, name="excursiones"),
	path('excursion/<str:id>/', views.excursion, name = "excursion"),
	path('', views.index),
	path('buscar/', views.buscar, name="buscar"),
	path('aniadir/', views.excursion_todas, name="añadir"),
	path('editar/<str:id>/', views.excursion, name="editar"),
	path('aniadir_comentario/<str:id>/', views.aniadir_comentario, name="aniadir_comentario"),
	path('borrar/<str:id>/', views.borrar_excursion, name="borrar"),
	path('cambiarlike/<str:id>/', views.cambiar_like, name="like"),
	path('signup/', views.signup, name='signup'),
	path('api/excursiones/', views.ExcursionesView.as_view(),name="excursiones_api"),
	path('api/excursion/<str:id>/', views.ExcursiónView.as_view(), name = "excursion_api"),
	]