from django.db import models


# Create your models here.


class Usuarios(models.Model):
    nombre = models.CharField(max_length=20)
    mail = models.EmailField()
    contraseña = models.CharField(max_length=128)