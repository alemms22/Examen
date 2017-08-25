from django.db import models

# Create your models here.

class RRHH(models.Model):
    Sexo =(
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )


    Name=models.CharField(max_length=50,help_text='Ingrese su nombre: ')
    Telephone=models.IntegerField(max_length=10,help_text='Ingrese su numero de telefono: ')
    Sex=models.CharField(max_length=1,help_text='Ingrese su sexo: ')
    Fecha=models.DateField(auto_now=True)
