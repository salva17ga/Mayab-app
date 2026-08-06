# Register your models here.
from django.contrib import admin
from apps.portal.models import Producto, Exhibicion, Foto
from django.utils.html import format_html

class ProductoAdmin(admin.ModelAdmin): 
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

class FotoAdmin(admin.ModelAdmin): 
    list_display = ("preview","Imagen", "Fecha_carga", "image_type", "name_of_parent", "type_of_product")
    fieldsets = (
        ("Archivo",
          {"fields": ("Imagen",)}), 
        ("Pertenencia de la imagen (producto o exhibición, seleccionar solo al que corresponda)", 
         {"fields": ("Producto", "Exhibicion")})
    )
    list_filter = ("Fecha_carga","Exhibicion", "Producto__Categoria", "Producto__Disponible")    
    search_fields = ("Producto__Nombre", "Exhibicion__Nombre")
    list_per_page = 10

    '''
        #######
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
        to create a column that displays if the image belongs to a product
        or to an exhibition
        """
        if obj.Producto: 
            image_type = "Producto"
        elif obj.Exhibicion:  
            image_type = "Exhibición"
        else: 
            image_type = None
        
        return image_type

    @admin.display(description="Registro asociado")
    def name_of_parent(self, obj): 
        """
        returns the name of the object parent of the image, wether it corresponds to a
        product or to an exhibition
        """
        name = obj.Producto or obj.Exhibicion
        return name 

    @admin.display(description="Tipo de producto (si aplica)", empty_value= "No es producto")
    def type_of_product(self, obj): 
        """
        if the parent object is of Product type, returns
        the category of product
        """
        if obj.Producto: 
            type_of_product = obj.Producto.Categoria
            return type_of_product
        else: 
            return None
        
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Exhibicion, ExhibicionAdmin)
admin.site.register(Foto, FotoAdmin)
