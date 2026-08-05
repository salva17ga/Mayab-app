# Register your models here.
from django.contrib import admin
from apps.portal.models import Producto, Exhibicion, Foto

admin.site.register(Producto)
admin.site.register(Exhibicion)
admin.site.register(Foto)
