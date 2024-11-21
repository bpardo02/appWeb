from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def asignar_permiso_arrendatario(sender, instance, created, **kwargs):
    if created and instance.tipo_usuario == "arrendatario":
        permiso = Permission.objects.get(codename="puede_publicar_inmuebles")
        instance.user_permissions.add(permiso)
