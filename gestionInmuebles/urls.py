from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("inmuebles/", views.lista_inmuebles, name="lista_inmuebles"),
    path("inmuebles/<int:pk>/", views.detalle_inmueble, name="detalle_inmueble"),
]
