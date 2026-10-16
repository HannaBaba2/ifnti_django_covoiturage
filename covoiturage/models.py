from django.db import models
from django.core.validators import MinValueValidator


class Trajet(models.Model):
    conducteur = models.CharField(max_length=200)
    ville_depart = models.CharField(max_length=200)
    ville_arrive = models.CharField(max_length=200)
    date_depart = models.DateField()  
    heure_depart = models.CharField(max_length=200)
    places = models.IntegerField(validators=[MinValueValidator(1)])
    prix_place = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.ville_depart} -> {self.ville_arrive}, le {self.date_depart} à {self.heure_depart}"
