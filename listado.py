import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyectoInmuebles.settings")
django.setup()

from gestionInmuebles.models import Inmueble, Comuna


def export_inmuebles_por_comuna():
    output_file = "inmuebles_por_comuna.txt"

    with open(output_file, "w", encoding="utf-8") as file:
        comunas = Comuna.objects.prefetch_related("inmueble_set").all()

        for comuna in comunas:
            file.write(f"Comuna: {comuna.nombre}\n")
            file.write("-" * 40 + "\n")

            inmuebles = Inmueble.objects.filter(comuna=comuna).only(
                "nombre", "descripcion"
            )

            for inmueble in inmuebles:
                file.write(f"Nombre: {inmueble.nombre}\n")
                file.write(f"Descripción: {inmueble.descripcion}\n")
                file.write("\n")

            # Separador entre comunas
            file.write("=" * 40 + "\n\n")

    print(f"Archivo generado: {output_file}")


if __name__ == "__main__":
    export_inmuebles_por_comuna()
