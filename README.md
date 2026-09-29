# Mayab app 
Software para soporte de tienda de arte y diseño Mayab. Esta aplicación web funciona como página de presentación del negocio, y también como catálogo interactivo de productos que cargan los usuarios con acceso desde el admin. 

## *Tipos de usuarios y grupos*: 
- Super admin: todos los permisos. 
- Administrador mayab: responsables del negocio. Pueden añadir nuevos usuarios y añadir registros e imágenes de los distintos articulos del catálogo 
- Empleado: Pueden añadir, editar y eliminar registros de artículos del catálogo, e imágenes. 

## Estructura
Aplicación monolítica, debido a su pequeño tamaño todas las rutas y funcionalidades se encuentran en una única djangp app: 'portal'. 

**Dependencias**: python 3.13.5 . Todos los paquetes necesarios están en requirements.txt.

Versiones: 
- 1.0.0: desplegada el 27/9/2026
- 1.0.1: corrección de motor de autenticación que no permitía que usuarios vieran las posibles acciones correspondientes a su grupo en el admin tras iniciar sesión. | corrección de formulario que mostraba las fotos de cada producto para que si eliminara los registros y los archivos. 


## Contacto: 
Desarrollada por Salvador Garcilita, salvador.garcilita@bioalgoritmia.com