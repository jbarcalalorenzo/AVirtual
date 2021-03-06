from datetime import datetime
from django.conf import settings
from django.db import models


# Create your models here.


class Asociacion(models.Model):
    first_name = models.CharField(max_length=255)
    nif = models.CharField(max_length=11)
    direccion = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='media/asociacion/')

class Socio(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=30)
    fecha_alta = models.DateTimeField(default=datetime.now, blank=False)
    fecha_baja = models.DateTimeField(blank=True, null=True)
    mail = models.CharField(max_length=255)
    telefono = models.CharField(max_length=12)
    foto = models.ImageField(upload_to='media/socios/')


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
    foto = models.ImageField(upload_to='media/materiales/')


class Stock(models.Model):
    ESTADOS = (
        ('N', 'Nuevo'),
        ('R', 'Roto'),
        ('S', 'Semi nuevo'),
    )
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, choices=ESTADOS)
    fecha_alta = models.DateTimeField(default=datetime.now, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='media/stock/')
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    direccion = models.CharField(max_length=30)
    fecha_alta = models.DateTimeField(default=datetime.now, blank=False)
    telefono = models.CharField(max_length=30)
    mail = models.CharField(max_length=100)

class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_alta = models.DateTimeField(blank=True)
    fecha_baja = models.DateTimeField(blank=True)
    coste = models.DecimalField(max_digits=10, decimal_places=2)
    beneficio = models.DecimalField(max_digits=10, decimal_places=2)
    participantes = models.ManyToManyField(Socio)
    contactos = models.ManyToManyField(Contacto)

class Alquila(models.Model):
    """
    stock - socio n n 
    """
    fecha_alquiler = models.DateTimeField(default=datetime.now)
    material = models.ForeignKey(Stock, on_delete=models.CASCADE)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fecha_devolucion = models.DateTimeField(blank=True)

    class Meta:
        unique_together = ('socio', 'material', 'fecha_alquiler')

class Documentos(models.Model):
    TIPOS = (
        ('A', 'Alta'),
        ('B', 'Baja'),
        ('AY','Ayudas'),
    )
    id = models.OneToOneField(Socio,primary_key=True)
    nombre = models.CharField(max_length=255,blank=False,)
    tipo = models.CharField(max_length=2, choices=TIPOS)
    fecha_alta = models.DateTimeField(default=datetime.now, blank=False)
    link = models.FilePathField(path=settings.MEDIA_ROOT)
