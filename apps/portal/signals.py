from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Foto


@receiver(post_delete, sender=Foto)
def eliminar_archivo_foto(sender, instance, **kwargs):
    '''eliminar todas las imagenes asociadas a un registro de un producto 
    si ese registro se elimina'''
    if instance.Imagen:
        instance.Imagen.delete(save=False)