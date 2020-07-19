from django.urls import path
from . import views

urlpatterns = [
	path("", views.printer_index, name="printer_index"),
	path("<int:pk>/", views.printer_detail, name="printer_detail"),
]