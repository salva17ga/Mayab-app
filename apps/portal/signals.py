from django.db.models.signals import post_delete
from django.dispatch import receiver
from pathlib import Path
from .models import Foto

@receiver(post_delete, sender=Foto)
def eliminar_archivo_foto(sender, instance, **kwargs):
    """Elimina el archivo de imagen y su carpeta si queda vacía."""

    if instance.Imagen:
        archivo = Path(instance.Imagen.path)

        # Eliminar el archivo
        instance.Imagen.delete(save=False)

        # Eliminar la carpeta si quedó vacía
        carpeta = archivo.parent

        if carpeta.exists() and not any(carpeta.iterdir()):
            carpeta.rmdir()