# Register your models here.
from django.contrib import admin
from apps.portal.models import Mueble, Decoracion, Arte, Exhibicion, Interiorismo, Foto
from django.utils.html import format_html

##### First aux models, then practical used models: 
### Aux models: 
# aux model
class BaseProductAdmin(admin.ModelAdmin):
    '''
    This class inherits from ModelAdmin and defines basic methods that
    are used for all the main models that inherit from this class 
    '''

    def save_model(self, request, obj, form, change):
        if not change:
            obj.Registrado_por = request.user

        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        '''
        allows the field 'Registrado_por' to be filled when creating a new
        register of a product and saving a first image in that form using the 
        inline approach. This results in that first image saved with their 
        corresponding register having a 'Registrado_por' valid input.  
        '''
        instances = formset.save(commit=False)

        for obj in instances:
            if not obj.Registrado_por:
                obj.Registrado_por = request.user

            obj.save()

        formset.save_m2m()

# aux model: 
class FotoInline(admin.StackedInline): 
    '''
    this inline is used in all the following product and 
    exhibitions or decorations models to allow save a photo
    in their corresponding form
    '''
    
    model = Foto
    extra = 0
    exclude = ('Registrado_por', )

    readonly_fields = ('show_photo',)

    fields = (
        'Imagen',
        'show_photo',
    )


    @admin.display(description="Vista previa")
    def show_photo(self, obj):
        if obj.Imagen:
            return format_html(
                '<img src="{}" style="width:20rem; height: 20rem; '
            'object-fit:cover; border-radius:0.5rem;">',
                obj.Imagen.url
            )
        return "-"

### Practical models: 

class MuebleAdmin(BaseProductAdmin): 
    list_display = ("Nombre", "Categoria", "Autor", "Precio", "Disponible",
                     "Fecha_registro", "Fecha_actualizacion", "Registrado_por")
    list_filter = ("Categoria", "Disponible", "Fecha_registro")
    date_hierarchy = "Fecha_registro"
    search_fields = ("Nombre", "Autor")
    list_per_page = 10
    inlines = (FotoInline, )
    exclude = ('Registrado_por', )
    
class DecoracionAdmin(BaseProductAdmin): 
    list_display = ("Nombre", "Categoria", "Autor", "Precio", "Disponible",
                     "Fecha_registro", "Fecha_actualizacion", "Registrado_por")
    list_filter = ("Categoria", "Disponible", "Fecha_registro")
    date_hierarchy = "Fecha_registro"
    search_fields = ("Nombre", "Autor")
    list_per_page = 10
    inlines = (FotoInline, )
    exclude = ('Registrado_por', )
        
class ArteAdmin(BaseProductAdmin): 
    list_display = ("Nombre", "Categoria", "Autor", "Precio", "Disponible",
                     "Fecha_registro", "Fecha_actualizacion", "Registrado_por")
    list_filter = ("Categoria", "Disponible", "Fecha_registro")
    date_hierarchy = "Fecha_registro"
    search_fields = ("Nombre", "Autor")
    list_per_page = 10
    inlines = (FotoInline, )
    exclude = ('Registrado_por', )
    
class ExhibicionAdmin(BaseProductAdmin): 
    list_display = ("Nombre", "Descripcion", "Fecha_exhibicion")
    list_filter = ("Fecha_exhibicion",)
    date_hierarchy = "Fecha_exhibicion"
    search_fields = ("Nombre",) 
    list_per_page = 10
    inlines = (FotoInline, )
    exclude = ('Registrado_por', )

class InteriorismoAdmin(BaseProductAdmin): 
    list_display = ("Nombre", "Descripcion", "Fecha_registro")
    list_filter = ("Fecha_registro",)
    date_hierarchy = "Fecha_registro"
    search_fields = ("Nombre",) 
    list_per_page = 10
    inlines = (FotoInline, )
    exclude = ('Registrado_por', )

class FotoAdmin(admin.ModelAdmin): 
    list_display = ("preview","Imagen", "Fecha_carga", "image_type", "name_of_parent",
                     "type_of_product", "Registrado_por")
    fieldsets = (
        ("Archivo",
          {"fields": ("Imagen",)}), 
        ("Pertenencia de la imagen (Seleccionar solo al que corresponda)", 
         {"fields": ("Mueble", "Decoracion", "Arte", "Exhibicion", "Interiorismo")}),
    )
    list_filter = ("Fecha_carga","Exhibicion", "Mueble__Categoria", "Decoracion__Categoria", 
                   "Arte__Categoria", "Interiorismo")    
    search_fields = ("Mueble__Nombre", "Decoracion__Nombre", "Arte__Nombre", "Exhibicion__Nombre", 
                     "Interiorismo__Nombre")
    list_per_page = 10
    exclude = ('Registrado_por', )
    readonly_fields = ('preview',)

    def get_fieldsets(self, request, obj=None):
        '''
        if page and form for edit photo (register), display a preview of the existing photo,
        this ensures creating a new photo (add photo) does not show an empty field for preview
        '''
        if obj:
            return (
                (
                    "Archivo",
                    {
                        "fields": ("Imagen",)
                    }
                ),
                (
                    "Pertenencia de la imagen (Seleccionar solo al que corresponda)",
                    {
                        "fields": (
                            "Mueble",
                            "Decoracion",
                            "Arte",
                            "Exhibicion",
                            "Interiorismo",
                        )
                    },
                ),
                (
                    "Vista previa de la foto",
                    {
                        "fields": ("preview",)
                    }
                ),
            )

        # Creando una Foto nueva
        return self.fieldsets


    @admin.display(description="Vista previa")
    def preview(self, obj): 
        if obj.Imagen: 
            return format_html(
                '<img src="{}" style="width:10rem; height:10rem; object-fit:contain;">',
                obj.Imagen.url)
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
        if obj.Mueble: 
            type_of_product = obj.Mueble.Categoria 
            return type_of_product
        if obj.Decoracion: 
            type_of_product = obj.Decoracion.Categoria
            return type_of_product
        if obj.Arte: 
            type_of_product = obj.Arte.Categoria
            return type_of_product
        else: 
            return None

admin.site.register(Mueble, MuebleAdmin)
admin.site.register(Decoracion, DecoracionAdmin)
admin.site.register(Arte, ArteAdmin)
admin.site.register(Exhibicion, ExhibicionAdmin)
admin.site.register(Interiorismo, InteriorismoAdmin)
admin.site.register(Foto, FotoAdmin)

