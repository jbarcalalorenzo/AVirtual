import django_tables2 as tables
from AsociacionVirtual import models

class SocioTable(tables.Table):
    class Meta:
        model = models.Socio
        fields = ("nombre","mail","telefono")