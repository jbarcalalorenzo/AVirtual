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
    fecha_baja = models.DateTimeField(blank=True)
    mail = models.CharField(max_length=255)
    telefono = models.CharField(max_length=12)
    foto = models.ImageField(upload_to='socios')
    
class Cuota(models.Model):
    fecha_pago = models.DateTimeField(default=datetime.now, blank=False)
    cantidad = models.DecimalField( max_digits=10, decimal_places=2)
    socio = models.ForeignKey(Socio , on_delete=models.CASCADE)
    
class Stock(models.Model):
    socio = models.ForeignKey(Material , on_delete=models.CASCADE)
    ESTADOS = (
        ('N', 'Nuevo'),
        ('R', 'Roto'),
        ('S', 'Semi nuevo'),
    )
    estado = models.CharField(max_length=1, choices=ESTADOS)
    fecha_alta = models.DateTimeField(default=datetime.now, blank=False)
    precio = models.DecimalField( max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='stock')
    
class Alquila(models.Model):
    """
    stock - socio n n 
    """
    pass
class Juego(models.Model):
    pass

class Material(models.Model):
    pass
    
class Evento(models.Model):
    pass

class Participa(model.Model):
    """
    evento - socio n n
    """
    pass
