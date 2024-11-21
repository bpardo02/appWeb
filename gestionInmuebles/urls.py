from django.urls import path
from . import views
from .views import CustomLoginView, CustomLogoutView
from .views import registro_usuario, actualizar_usuario, perfil_usuario

urlpatterns = [
    path("", views.index, name="index"),
    path("inmuebles/", views.lista_inmuebles, name="lista_inmuebles"),
    path("inmuebles/<int:pk>/", views.detalle_inmueble, name="detalle_inmueble"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("registro/", registro_usuario, name="registro"),
    path("actualizar/", actualizar_usuario, name="actualizar"),
    path("perfil/", perfil_usuario, name="perfil"),
    path("registro/", views.registro_usuario_view, name="registro"),
    path("publicar-inmueble/", views.publicar_inmueble, name="publicar_inmueble"),
]
