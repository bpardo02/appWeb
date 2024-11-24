import os
import django

# Configurar el entorno Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyectoInmuebles.settings")
django.setup()

from gestionInmuebles.models import Inmueble, Region


def export_inmuebles_por_region():
    output_file = "inmuebles_por_region.txt"

    with open(output_file, "w", encoding="utf-8") as file:
        regiones = Region.objects.prefetch_related("inmueble_set").all()

        for region in regiones:
            file.write(f"Región: {region.nombre}\n")
            file.write("-" * 40 + "\n")

            inmuebles = Inmueble.objects.filter(region=region).only(
                "nombre", "descripcion"
            )

            for inmueble in inmuebles:
                file.write(f"Nombre: {inmueble.nombre}\n")
                file.write(f"Descripción: {inmueble.descripcion}\n")
                file.write("\n")

            file.write("=" * 40 + "\n\n")

    print(f"Archivo generado: {output_file}")


if __name__ == "__main__":
    export_inmuebles_por_region()
