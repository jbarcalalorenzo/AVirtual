import django_tables2 as tables
from AsociacionVirtual import models

class SocioTable(tables.Table):
    class Meta:
        model = models.Socio
        fields = ("nombre","mail","telefono")
        template = "custom_table.html"

class CuentasTable(tables.Table):
    class Meta:
        model = models.Cuentas
        fields = None
        template= "custom_table.html"
