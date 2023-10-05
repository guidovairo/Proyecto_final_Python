from django.db import models

# Create your models here.

class MateriasAprobadas(models.Model):
    materia = models.CharField(max_length=40)


class Cuota(models.Model):
   debe_cuotas = models.CharField(max_length=40)
    

class FinalesPrevios(models.Model):
    debe_final_de = models.CharField(max_length=40)
