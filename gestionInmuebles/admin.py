from django.contrib import admin
from .models import Inmueble, Region, Comuna
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


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


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "rut",
        "tipo_usuario",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("rut", "direccion", "telefono", "tipo_usuario")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("rut", "direccion", "telefono", "tipo_usuario")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
