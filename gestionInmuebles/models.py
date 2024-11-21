from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

TIPO_USUARIO_CHOICES = [
    ("arrendatario", "Arrendatario"),
    ("arrendador", "Arrendador"),
]


class CustomUser(AbstractUser):
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.tipo_usuario})"


class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="comunas")

    def __str__(self):
        return self.nombre


TIPO_INMUEBLE_CHOICES = [
    ("casa", "Casa"),
    ("departamento", "Departamento"),
    ("oficina", "Oficina"),
    ("terreno", "Terreno"),
]


class Inmueble(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_inmueble = models.CharField(
        max_length=50, choices=TIPO_INMUEBLE_CHOICES, default="departamento"
    )
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="inmuebles/", null=True, blank=True)

    def __str__(self):
        return self.nombre

    def clean(self):
        if self.precio_mensual < 0:
            raise ValidationError("El precio mensual no puede ser negativo.")
        if self.m2_construidos < 0 or self.m2_totales < 0:
            raise ValidationError("Los metros cuadrados no pueden ser negativos.")
        if self.habitaciones < 0 or self.banos < 0:
            raise ValidationError("Habitaciones y baños no pueden ser negativos.")

    class Meta:
        permissions = [
            ("puede_ver_inmuebles", "Puede ver inmuebles"),
            ("puede_ver_detalle_inmuebles", "Puede ver detalle de inmuebles"),
            ("puede_publicar_inmuebles", "Puede publicar inmuebles"),
        ]
