from django.contrib import admin
from .models import Inmueble


class InmuebleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "direccion",
        "comuna",
        "tipo_inmueble",
        "precio_mensual",
    )

    search_fields = ("nombre", "direccion", "comuna", "tipo_inmueble")

    list_filter = ("comuna", "tipo_inmueble", "precio_mensual")


admin.site.register(Inmueble, InmuebleAdmin)
