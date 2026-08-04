from django.contrib import admin

# Register your models here.
from apps.portal.models import Producto, Exhibicion, Foto

admin.site.register(Producto)
admin.site.register(Exhibicion)
admin.site.register(Foto)
