# Register your models here.
from django.contrib import admin
from apps.portal.models import Mueble, Decoracion, Arte, Exhibicion, Interiorismo, Foto
from django.utils.html import format_html

class MuebleAdmin(admin.ModelAdmin): 
    list_display = ("Nombre", "Categoria", "Autor", "Precio", "Disponible", "Fecha_registro", "Fecha_actualizacion")
    list_filter = ("Categoria", "Disponible", "Fecha_registro")
    date_hierarchy = "Fecha_registro"
    search_fields = ("Nombre", "Autor")
    list_per_page = 10

class DecoracionAdmin(admin.ModelAdmin): 
    list_display = ("Nombre", "Categoria", "Autor", "Precio", "Disponible", "Fecha_registro", "Fecha_actualizacion")
    list_filter = ("Categoria", "Disponible", "Fecha_registro")
    date_hierarchy = "Fecha_registro"
    search_fields = ("Nombre", "Autor")
    list_per_page = 10

class ArteAdmin(admin.ModelAdmin): 
    list_display = ("Nombre", "Categoria", "Autor", "Precio", "Disponible", "Fecha_registro", "Fecha_actualizacion")
    list_filter = ("Categoria", "Disponible", "Fecha_registro")
    date_hierarchy = "Fecha_registro"
    search_fields = ("Nombre", "Autor")
    list_per_page = 10

class ExhibicionAdmin(admin.ModelAdmin): 
    list_display = ("Nombre", "Descripcion", "Fecha_exhibicion")
    list_filter = ("Fecha_exhibicion",)
    date_hierarchy = "Fecha_exhibicion"
    search_fields = ("Nombre",) 
    list_per_page = 10

class InteriorismoAdmin(admin.ModelAdmin): 
    list_display = ("Nombre", "Descripcion", "Fecha_registro")
    list_filter = ("Fecha_registro",)
    date_hierarchy = "Fecha_registro"
    search_fields = ("Nombre",) 
    list_per_page = 10

class FotoAdmin(admin.ModelAdmin): 
    list_display = ("preview","Imagen", "Fecha_carga", "image_type", "name_of_parent", "type_of_product")
    fieldsets = (
        ("Archivo",
          {"fields": ("Imagen",)}), 
        ("Pertenencia de la imagen (Seleccionar solo al que corresponda)", 
         {"fields": ("Mueble", "Decoracion, Arte, Exhibicion, Interiorismo")})
    )
    list_filter = ("Fecha_carga","Exhibicion", "Mueble__Categoria", "Decoracion__Categoria", 
                   "Arte__Categoria", "Interiorismo")    
    search_fields = ("Mueble__Nombre", "Decoracion__Nombre", "Arte__Nombre", "Exhibicion__Nombre", 
                     "Interiorismo__Nombre")
    list_per_page = 10

    '''
        ####### TODO
        implementar list_select_related porque cada fila hace obj.Producto y obj.Exhibicion 
        o sobrescribir get_queryset()
    '''

    @admin.display(description="Vista previa")
    def preview(self, obj): 
        if obj.Imagen: 
            return format_html('<img src="{}" width="60">', obj.Imagen.url)
        return "-"


    @admin.display(description="Tipo de imagen")
    def image_type(self, obj):
        """
        to create a column that displays the category of association
        """
        if obj.Mueble: 
            image_type = "Mueble"
        elif obj.Decoracion:  
            image_type = "Decoracion"
        elif obj.Arte:  
            image_type = "Arte"
        elif obj.Exhibicion:  
            image_type = "Exhibicion"
        elif obj.Interiorismo:  
            image_type = "Interiorismo"
        else: 
            image_type = None
        return image_type

    @admin.display(description="Registro asociado")
    def name_of_parent(self, obj): 
        """
        returns the name of the object parent of the image
        """
        name = obj.Mueble or obj.Decoracion or obj.Arte or obj.Exhibicion or obj.Interiorismo
        return name 

    @admin.display(description="Tipo de producto (si aplica)", empty_value= "No es producto")
    def type_of_product(self, obj): 
        """
        if the parent object is art, mueble or decoracion , returns
        the category of the product
        """
        if obj.Mueble or obj.Decoracion or obj.Arte: 
            type_of_product = obj.Mueble.Categoria or obj.Decoracion.Categoria or obj.Arte.Categoria
            return type_of_product
        else: 
            return None
        
admin.site.register(Mueble, MuebleAdmin)
admin.site.register(Decoracion, DecoracionAdmin)
admin.site.register(Arte, ArteAdmin)
admin.site.register(Exhibicion, ExhibicionAdmin)
admin.site.register(Interiorismo, InteriorismoAdmin)
admin.site.register(Foto, FotoAdmin)
