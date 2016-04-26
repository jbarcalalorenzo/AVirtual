from datetime import datetime

from django.db import models


# Create your models here.


class Asociacion(models.Model):
    first_name = models.CharField(max_length=255)
    nif = models.CharField(max_length=11)
    direccion = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)


class Socio(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=30)
    fecha_alta = models.DateTimeField(default=datetime.now, blank=False)
    fecha_baja = models.DateTimeField(blank=True, null=True)
    mail = models.CharField(max_length=255)
    telefono = models.CharField(max_length=12)
    foto = models.ImageField(upload_to='socios')


class Cuota(models.Model):
    fecha_pago = models.DateTimeField(default=datetime.now, blank=False)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)


class Material(models.Model):
    TIPOS = (
        ('J', 'Juego'),
        ('U', 'Utensilio'),
        ('C', 'Comida'),
    )
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1, choices=TIPOS)
    nombre = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='materiales')


class Stock(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    ESTADOS = (
        ('N', 'Nuevo'),
        ('R', 'Roto'),
        ('S', 'Semi nuevo'),
    )
    estado = models.CharField(max_length=1, choices=ESTADOS)
    fecha_alta = models.DateTimeField(default=datetime.now, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='stock')


class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_alta = models.DateTimeField(blank=True)
    fecha_baja = models.DateTimeField(blank=True)
    coste = models.DecimalField(max_digits=10, decimal_places=2)
    beneficio = models.DecimalField(max_digits=10, decimal_places=2)
    participantes = models.ManyToManyField(Socio)


class Alquila(models.Model):
    """
    stock - socio n n 
    """
    fecha_alquiler = models.DateTimeField(default=datetime.now, )
    material = models.ForeignKey(Stock, on_delete=models.CASCADE)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fecha_devolucion = models.DateTimeField(blank=True)

    class Meta:
        unique_together = ('socio', 'material', 'fecha_alquiler')
