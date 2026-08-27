from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# class Usuario(models.Model): 
#     """Usuarios de mayab app que inician sesion"""

#     class Tipos_usuario(models.TextChoices): 
#         """Categorias validas para el atributo Tipo_usuario"""
#         Administrador = "Administrador", "Administrador"
#         Empleado = "Empleado", "Empleado"

#     Nombre = models.CharField(max_length=50,
#                               help_text="Nombre del usuario")
#     Apellido_paterno = models.CharField(max_length=50,
#                                         help_text="Apellido paterno del usuario")
#     Apellido_materno = models.CharField(max_length=50,
#                                         help_text="Apellido materno del usuario")
#     Contrasena = models.CharField(verbose_name="Contraseña",
#                                         max_length=50,
#                                         help_text="Contraseña del usuario")
#     Email = models.EmailField(verbose_name="Correo electrónico", 
#                                         help_text="Correo electrónico del usuario", 
#                                         unique = True)
#     Fecha_registro = models.DateField(auto_now_add=True,
#                                         verbose_name="Fecha de registro del usuario",
#                                         help_text="Fecha  de registro del usuario")
#     Tipo_usuario = models.CharField(verbose_name="Tipo de usuario",
#                                     choices=Tipos_usuario.choices,
#                                     max_length=20)
#     Activo = models.BooleanField(default=True) 

#     ### relations
#     Registrado_por = models.IntegerField(null=True) # ID de usuario que creó al usuario

#     # productos
#     # exhibiciones

#### relaciones de modelos 
# usuarios - muebles (1 - n)
# usuarios - arte (1 - n)
# usuarios - decoracion (1 - n)
# usuarios - exhibiciones (1 - n)
# usuarios - interiorismo (1 - n)
# usuarios - fotos (1 - n)
# muebles - fotos (1 -n)
# arte - fotos (1 -n)
# decoracion - fotos (1 -n)
# interiorismo - fotos (1 -n)
# exhibiciones - fotos (1 - n)



class Mueble(models.Model): 
    """
    Datos asociados a cada registro de mueble
    """

    class CategoriasMuebles(models.TextChoices):
        """Categorías válidas para muebles registrados en el atributo Categoria"""

        Mesa = 'mesa', 'Mesas'
        Silla_banco = 'silla_banco', 'Sillas y bancos'
        Banca = 'banca', 'Bancas'
        Sofa = 'sofa', 'Sofás'
        Otoman = 'otoman', 'Otomanes'
        Credenza = 'credenza', 'Credenzas'
        Cantina = 'cantina', 'Cantinas'
        Vitrina = 'vitrina', 'Vitrinas'
        Cabecera_cama = 'cabecera_cama', 'Cabeceras de cama'
        Escritorio = 'escritorio', 'Escritorios'

    Nombre = models.CharField(max_length=100,
                              verbose_name="Nombre del mueble", 
                              help_text="Nombre del mueble",
                              unique=True)
    Descripcion = models.TextField(verbose_name="Descripción del mueble",
                                   help_text="Descripción del mueble",
                                   blank=True,
                                   null=True)
    Categoria = models.CharField(max_length=50,
                                 verbose_name="Categoría de mueble",
                                 help_text="Categoría de mueble",
                                 choices=CategoriasMuebles.choices)
    Autor = models.CharField(max_length=100,
                             help_text="Autor o fabricante del mueble")
    Precio = models.DecimalField(max_digits=8,
                                 decimal_places=2,
                                 help_text="Precio del producto")
    Disponible = models.BooleanField(blank=True,
                                     default=True,
                                     help_text="Disponible")
    Fecha_registro = models.DateField(auto_now_add=True,
                                      verbose_name="Fecha de registro por usuario",
                                      help_text="Fecha de registro por usuario")
    Fecha_actualizacion = models.DateTimeField(auto_now=True)
    Registrado_por = models.ForeignKey(User,
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            blank=True,
                                            related_name='muebles_registrados')


    def __str__(self):
        return self.Nombre
    
class Decoracion(models.Model): 
    """
    Datos asociados a cada registro de accesorio de decoracion
    """

    class CategoriasDecoracion(models.TextChoices):
        """Categorías válidas para articulos registrados en el atributo Categoria"""

        Espejo = 'espejo', 'espejos'
        Lampara = 'lampara', 'lámparas'
        Metalisteria = 'metalisteria', 'Metalistería'
        Acabado_antique = 'acabado_antique', 'Acabado antique'
        Vidrio_ceramica = 'vidrio_ceramica', 'Vidrio y cerámica'
        Tapete = 'tapete', 'Tapetes'
        Cojin = 'cojin', 'Cojines'
        Madera_tallada = 'madera_tallada', 'Madera tallada (ebanistería)'

    Nombre = models.CharField(max_length=100,
                              verbose_name="Nombre del accesorio", 
                              help_text="Nombre del accesorio",
                              unique=True)
    Descripcion = models.TextField(verbose_name="Descripción del accesorio",
                                   help_text="Descripción del accesorio",
                                   blank=True,
                                   null=True)
    Categoria = models.CharField(max_length=50,
                                 verbose_name="Categoría de accesorio",
                                 help_text="Categoría de accesorio",
                                 choices=CategoriasDecoracion.choices)
    Autor = models.CharField(max_length=100,
                             help_text="Autor o fabricante del accesorio")
    Precio = models.DecimalField(max_digits=8,
                                 decimal_places=2,
                                 help_text="Precio del producto")
    Disponible = models.BooleanField(blank=True,
                                     default=True,
                                     help_text="Disponible")
    Fecha_registro = models.DateField(auto_now_add=True,
                                      verbose_name="Fecha de registro por usuario",
                                      help_text="Fecha de registro por usuario")
    Fecha_actualizacion = models.DateTimeField(auto_now=True)
    Registrado_por = models.ForeignKey(User,
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            related_name='articulos_decoracion_registrados')


    def __str__(self):
        return self.Nombre
    
class Arte(models.Model): 
    """
    Datos asociados a cada registro de accesorio de decoracion
    """

    class CategoriasArte(models.TextChoices):
        """Categorías válidas para articulos registrados en el atributo Categoria"""

        Pintura = 'pintura', 'Pinturas'
        Escultura = 'escultura', 'Escultura'
        Fotografia = 'fotografia', 'Fotografía'
        Arte_autoctono = 'arte_autoctono', 'Arte autóctono'

    Nombre = models.CharField(max_length=100,
                              verbose_name="Nombre del producto", 
                              help_text="Nombre del producto",
                              unique=True)
    Descripcion = models.TextField(verbose_name="Descripción del producto",
                                   help_text="Descripción del producto",
                                   blank=True,
                                   null=True)
    Categoria = models.CharField(max_length=50,
                                 verbose_name="Categoría de arte",
                                 help_text="Categoría de arte",
                                 choices=CategoriasArte.choices)
    Autor = models.CharField(max_length=100,
                             help_text="Autor o fabricante del producto")
    Precio = models.DecimalField(max_digits=8,
                                 decimal_places=2,
                                 help_text="Precio del producto")
    Disponible = models.BooleanField(blank=True,
                                     default=True,
                                     help_text="Disponible")
    Fecha_registro = models.DateField(auto_now_add=True,
                                      verbose_name="Fecha de registro por usuario",
                                      help_text="Fecha de registro por usuario")
    Fecha_actualizacion = models.DateTimeField(auto_now=True)
    Registrado_por = models.ForeignKey(User,
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            related_name='arte_registrado')
    def __str__(self):
        return self.Nombre


class Exhibicion(models.Model): 
    """Datos asociados a exhiciones realizadas en mayab"""
    Nombre = models.CharField(max_length=100,
                              verbose_name="Nombre de la exhibición", 
                              help_text="Nombre de la exhibición")
    Descripcion = models.TextField(verbose_name="Descripción de la exhibición",
                                   help_text="Descripción de la exhibición",
                                   blank=True,
                                   null=True)
    Fecha_exhibicion = models.DateField(verbose_name="Fecha de la exhibición",
                                      help_text="Fecha de la exhibición")
    Fecha_registro = models.DateField(auto_now_add=True,
                                      verbose_name="Fecha de registro",
                                      help_text="Fecha de registro")
    Registrado_por = models.ForeignKey(User,
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            related_name='exhibiciones_registradas')

    def __str__(self):
            return self.Nombre

class Interiorismo(models.Model): 
    '''Datos asociados a fotografias de diseño de espacioos'''
    Nombre = models.CharField(max_length=100,
                                  verbose_name="Nombre de la exhibición", 
                                  help_text="Nombre de la exhibición")
    Descripcion = models.TextField(verbose_name="Descripción de la exhibición",
                                       help_text="Descripción de la exhibición",
                                       blank=True,
                                       null=True)
    Fecha_registro = models.DateField(auto_now_add=True,
                                          verbose_name="Fecha de registro",
                                          help_text="Fecha de registro")
    Registrado_por = models.ForeignKey(User,
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            related_name='interiorismo_registrado')
    

def ruta_foto(instance, filename):
    '''
    Auxiliar function to save the image where it corresponds, in the Productos folder
    or in the Exhibitions folder. 
    '''
    if instance.Mueble: 
        return f"productos/muebles/{instance.Mueble.id}/{filename}"
    elif instance.Decoracion: 
        return f"productos/decoracion/{instance.Decoracion.id}/{filename}"
    elif instance.Arte: 
        return f"productos/arte/{instance.Arte.id}/{filename}"
    elif instance.Exhibicion: 
        return f"exhibicion/{instance.Exhibicion.id}/{filename}"
    elif instance.Interiorismo:
        return f"interiorismo/{instance.Interiorismo.id}/{filename}"
         
    
class Foto(models.Model): 
    """Datos asociados a imagenes cargadas en el sistema de cualquier entidad"""

    Imagen = models.ImageField(upload_to=ruta_foto)
    Fecha_carga = models.DateField(auto_now_add=True,
                                      verbose_name="Fecha de carga de imagen",
                                      help_text="Fecha de carga de imagen")

    ### relations
    Mueble = models.ForeignKey(Mueble, 
                                    on_delete = models.CASCADE,
                                    null=True,
                                    blank=True,
                                    related_name="fotos")
    Decoracion = models.ForeignKey(Decoracion, 
                                    on_delete = models.CASCADE,
                                    null=True,
                                    blank=True,
                                    related_name="fotos")
    Arte = models.ForeignKey(Arte, 
                                on_delete = models.CASCADE,
                                null=True,
                                blank=True,
                                related_name="fotos")
    Exhibicion  = models.ForeignKey(Exhibicion, 
                                    on_delete = models.CASCADE,
                                    null=True,
                                    blank=True,
                                    related_name="fotos")
    Interiorismo = models.ForeignKey(Interiorismo, 
                                    on_delete = models.CASCADE,
                                    null=True,
                                    blank=True,
                                    related_name="fotos")

    Registrado_por = models.ForeignKey(User,
                                                null = True,
                                                on_delete=models.SET_NULL,
                                                related_name='fotos_registradas')
    
    def clean(self):
        '''validar que solo hay una relacion forgeign key en la imagen'''
        super().clean()
        if bool(self.Mueble) + bool(self.Decoracion) + bool(self.Arte) + \
            bool(self.Exhibicion) + bool( self.Interiorismo) > 1: 
            raise ValidationError("Seleccione únicamente un producto o una exhibición.")
         
    def __str__(self):
            return self.Imagen.name

