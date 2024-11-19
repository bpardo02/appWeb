from django.contrib import admin
from .models import Inmueble, Region, Comuna


@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "direccion",
        "comuna",
        "region",
        "tipo_inmueble",
        "precio_mensual",
    )

    search_fields = ("nombre", "direccion", "comuna__nombre", "region__nombre")

    list_filter = ("region", "comuna", "tipo_inmueble")

    list_select_related = ("comuna", "region")


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "region")
    search_fields = ("nombre", "region__nombre")
    list_filter = ("region",)
