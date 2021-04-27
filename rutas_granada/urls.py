from django.urls import path
from . import views

urlpatterns = [
	path('excursion/', views.excursion_todas),
	path('excursion/<str:id>/', views.excursion),
	path('', views.index),
	path('buscar', views.buscar),
	]