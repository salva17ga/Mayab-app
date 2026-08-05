# Register your models here.
from django.contrib import admin
from apps.portal.models import Producto, Exhibicion, Foto

class ProductoAdmin(admin.ModelAdmin): 
    list_display = ("Nombre", "Categoria", "Autor", "Precio", "Disponible", "Fecha_registro", "Fecha_actualizacion")
    list_filter = ("Categoria", "Disponible", "Fecha_registro")
    date_hierarchy = "Fecha_registro"
    search_fields = ("Nombre", "Autor")

class ExhibicionAdmin(admin.ModelAdmin): 
    list_display = ("Nombre", "Descripcion", "Fecha_exhibicion")
    list_filter = ("Fecha_exhibicion",)
    date_hierarchy = "Fecha_exhibicion"
    search_fields = ("Nombre",) 

class FotoAdmin(admin.ModelAdmin): 
    # pendiente de dejar en version final
    list_display = ("Imagen", "Fecha_carga")
    # TODO: mostrar atributos de modelos relacionados

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Exhibicion, ExhibicionAdmin)
admin.site.register(Foto, FotoAdmin)
