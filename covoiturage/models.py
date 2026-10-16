from django.db import models

class Trajet(models.Model):
    conducteur = models.CharField(max_length=200)
    ville_depart = models.CharField(max_length=200)
    ville_arrive = models.CharField(max_length=200)
    date_depart = models.DateField()  
    heure_depart = models.CharField(max_length=200)
    places = models.IntegerField()
    prix_place = models.IntegerField(null=True, blank=True)
