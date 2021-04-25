from django.urls import path
from . import views

urlpatterns = [
	path('excursion/todas/',              views.excursion_todas),
	path('excursion/<str:id>/', views.excursion),
	path('', views.index)
	]