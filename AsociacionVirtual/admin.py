from django.contrib import admin
from .models import Asociacion,Socio,Cuota,Stock,Material,Evento
# Register your models here.

admin.site.register(Asociacion)
admin.site.register(Socio)
admin.site.register(Stock)
admin.site.register(Cuota)
admin.site.register(Material)
admin.site.register(Evento)