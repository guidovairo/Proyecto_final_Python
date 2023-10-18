from django.db import models


# Create your models here.

class MateriasAprobadas(models.Model):
    materia = models.CharField(max_length=40)
    Nota_primer_parcial = models.IntegerField(null=True, blank=True)
    Nota_segundo_parcial = models.IntegerField(null=True, blank=True)
    Nota_del_final = models.IntegerField(null=True, blank=True)

    def __str__(self):
       return f"{self.materia}"


class Cuota(models.Model):
   debe_cuotas = models.CharField(max_length=40)
   importe_a_pagar = models.IntegerField(null=True, blank=True)
   
   

   def __str__(self):
       return f"{self.debe_cuotas}"
    

class FinalesPrevios(models.Model):
    debe_final_de = models.CharField(max_length=40)

    def __str__(self):
       return f"{self.debe_final_de}"
    





