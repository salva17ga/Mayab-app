from django.db import models

# Create your models here.

#### modelos 
# usuarios - productos (1 - n)
# usuarios - exhibiciones (1 - n)
# productos - fotos (1 - n)
# exhibiciones - fotos (1 - n)

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

class Producto(models.Model): 
    """
    Datos asociados a cada producto registrado, pudiendo ser arte, mueble o accesorio 
    de decoracion. 
    """

    class Categorias_productos(models.TextChoices):
        """Categorías válidas para productos registrados en el atributo Categoria"""
        Mueble = "Mueble", "Mueble" 
        Arte = "Arte", "Arte"
        Accesorio_decoracion = "Accesorio_decoracion", "Accesorio de decoración"

    Nombre = models.CharField(max_length=100,
                              verbose_name="Nombre del producto", 
                              help_text="Nombre del producto",
                              unique=True)
    Descripcion = models.TextField(verbose_name="Descripción del producto",
                                   help_text="Descripción del producto",
                                   blank=True,
                                   null=True)
    Categoria = models.CharField(max_length=50,
                                 verbose_name="Categoría de producto",
                                 help_text="Categoría de producto",
                                 choices=Categorias_productos.choices)
    Autor = models.CharField(max_length=100,
                             help_text="Autor o fabricante del producto")
    Precio = models.DecimalField(max_digits=8,
                                 decimal_places=2,
                                 help_text="Precio del producto")
    Disponible = models.BooleanField(blank=True,
                                     default=True,
                                     help_text="Disponible")
    Fecha_registro = models.DateField(auto_now_add=True,
                                      verbose_name="Fecha de registro del usuario",
                                      help_text="Fecha de registro del usuario")
    Fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    ### relations
    # Registrado_por = 

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
    ### relations

    def __str__(self):
            return self.Nombre

    
def ruta_foto(instance, filename):
    '''
    Auxiliar function to save the image where it corresponds, in the Productos folder
    or in the Exhibitions folder. 
    '''
    if instance.producto:
        return f"productos/{instance.producto.id}/{filename}"
    return f"exhibiciones/{instance.exhibicion.id}/{filename}"


class Foto(models.Model): 
    """Datos asociados a imagenes cargadas en el sistema ya sea de exhibiciones o de productos"""

    Imagen = models.ImageField(upload_to=ruta_foto)
    Fecha_carga = models.DateField(auto_now_add=True,
                                      verbose_name="Fecha de la exhibición",
                                      help_text="Fecha de la exhibición")

    ### relations
    Producto = models.ForeignKey(Producto, 
                                    on_delete = models.CASCADE,
                                    null=True,
                                    blank=True,
                                    related_name="fotos")
    Exhibicion  = models.ForeignKey(Exhibicion, 
                                    on_delete = models.CASCADE,
                                    null=True,
                                    blank=True,
                                    related_name="fotos")

         
    def __str__(self):
            return self.Imagen.name

