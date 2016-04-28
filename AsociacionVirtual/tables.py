import django_tables2 as tables
from AsociacionVirtual import models

class SocioTable(tables.Table):
    class Meta:
        model = models.Socio
        fields = ("nombre","mail","telefono")
        template = "custom_table.html"

class GastosTable(tables.Table):
    class Meta:
        model = models.Cuentas
        fields = ("fecha","tipo","nombre","coste")
        template= "custom_table.html"

class IngresosTable(tables.Table):
    class Meta:
        model = models.Cuentas
        fields = ("fecha", "tipo", "nombre", "cantidad")
        template = "custom_table.html"

class EventosTable(tables.Table):
    class Meta:
        model = models.Evento
        fields = ("fecha","nombre","lugar","beneficio")
        template = "custom_table.html"

class BalanceTable(tables.Table):
    class Meta:
        model = models.Cuentas
        fields = ("fecha","tipo","nombre","cantidad","total")
        template = "custom_table.html"

class InvetarioTable(tables.Table):
    class Meta:
        model = models.Stock
        fields =("nombre","tipo","cantidad","propietario")
        template = "custom_table.html"

class Patrocinadores(tables.Table):
    class Meta:
        template = "custom_table.html"
        pass