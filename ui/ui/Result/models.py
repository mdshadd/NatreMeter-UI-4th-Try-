from django.db import models

# Create your models here.

class Reading(models.Model):
    intensity = models.FloatField()
    level     = models.FloatField()

    # def __str__(self):
    #     return f'{self.intensity} > {self.level}'
