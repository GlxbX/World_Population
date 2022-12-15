from django.db import models

# Create your models here.

class Population_by_countries(models.Model):

    country_name = models.CharField(max_length=256, verbose_name='Год')

    code = models.CharField(max_length = 64, verbose_name= "Код", null=False)

    year = models.IntegerField(verbose_name='Год')

    data = models.BigIntegerField(verbose_name="Люди")

        
        


class World_population(models.Model):

    year = models.IntegerField(verbose_name='Год')

    data = models.BigIntegerField(verbose_name="Люди")
   
