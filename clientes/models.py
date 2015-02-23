from django.db import models


class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()
    direccion = models.TextField()

    def __unicode__(self):
        return self.nombre
