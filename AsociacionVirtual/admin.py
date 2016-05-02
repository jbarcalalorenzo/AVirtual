from django.contrib import admin
from .models import Asociacion,Socio,Cuota,Stock,Material,Evento,Contacto
# Register your models here.
class SocioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'mail', 'fecha_alta', 'foto')

admin.site.register(Socio, SocioAdmin)

class CuotaAdmin(admin.ModelAdmin):

    list_display = ('fecha_pago', 'cantidad', 'socio')

admin.site.register(Cuota, CuotaAdmin)

class MaterialAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'tipo', 'foto')

admin.site.register(Material, MaterialAdmin)
admin.site.register(Contacto)
admin.site.register(Asociacion)
admin.site.register(Stock)
admin.site.register(Evento)