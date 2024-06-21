from django.db import models


class Alumno(models.Model):
    idAlumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    documento = models.CharField(max_length=20)
    cantTokens = models.IntegerField(default=0)
    contraseña = models.CharField(max_length=100)  # Asegúrate de almacenar la contraseña de manera segura

    def __str__(self):
        return f'{self.nombre} {self.apellido}'