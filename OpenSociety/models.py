from django.db import models
from datetime import datetime
# Create your models here.

class Cliente(models.Model):
    first_name = models.CharField(max_length=255)
    nif = models.CharField(max_length=11)
    direccion = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    fecha_alta = models.DateTimeField(default=datetime.now, blank=False)
    fecha_baja = models.DateTimeField(blank=True, null=True)

class Producto(models.Model):
    TIPOS = (
        ('A', 'Aplicacion'),
        ('P', 'Plugin')
    )
    nombre = models.CharField(max_length=55,blank=False)
    desc = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2,blank=False)
    duracion = models.IntegerField()# en... meses? 
    
class App(models.Model): #compra 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(default=datetime.now, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2,blank=False)
    fecha_finalizacion = models.DateTimeField(blank=False)
    carpeta = models.CharField(max_length=20)
    database = models.CharField(max_length=20)
    url = models.CharField(max_length=20)

class Plugin(models.Model): #compra 
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    app =  models.ForeignKey(App, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(default=datetime.now, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2,blank=False)
    fecha_finalizacion = models.DateTimeField(blank=False)

   
class Historial(models.Model):
    cliente = models.ForeignKey(Cliente)
    producto = models.ForeignKey(Producto)
    app =  models.ForeignKey(App)
    plugin =  models.ForeignKey(Plugin)
    fecha_compra = models.DateTimeField(default=datetime.now, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2,blank=False)
    fecha_finalizacion = models.DateTimeField(blank=False)

class Admin(models.Model):
    user = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
