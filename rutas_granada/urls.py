from django.urls import path
from . import views

urlpatterns = [
	path('excursion/todas/',              views.excursion_todas),
	path('excursion/<int:número>/', views.excursion),
	]