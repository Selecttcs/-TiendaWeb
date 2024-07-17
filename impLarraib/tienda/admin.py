from django.contrib import admin
from .models import Usuario,Producto,Venta,Oferta

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Oferta)
