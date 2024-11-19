from django.contrib import admin
from .models import Inmueble


class InmuebleAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "direccion", "precio", "tipo", "fecha_creacion")

    search_fields = ("nombre", "direccion", "tipo")

    list_filter = ("tipo", "precio", "fecha_creacion")


admin.site.register(Inmueble, InmuebleAdmin)
