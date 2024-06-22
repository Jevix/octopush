from django.db import models
from django.core.exceptions import ValidationError

class Alumno(models.Model):
    idAlumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    contraseña = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15 , null=True)
    tipousuario = models.CharField(max_length=15)
    cantTokens = models.IntegerField(max_length=10, default=0)
    



    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    def clean(self):
        # Validación personalizada para verificar duplicados de documento
        if Alumno.objects.filter(documento=self.documento).exists():
            raise ValidationError('Ya existe un alumno con este documento.')

    def save(self, *args, **kwargs):
        self.clean()  # Llama a la validación antes de guardar
        super(Alumno, self).save(*args, **kwargs)
