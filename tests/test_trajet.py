from django.db import IntegrityError
from covoiturage.models import Trajet 
import pytest

def test_creation_d_un_trajet(db):
    trajet = Trajet.objects.create(
        conducteur ="dieudonné",
        ville_depart = "Sokodé",
        ville_arrive = "Lomé",
        date_depart = "2026-10-17",
        heure_depart = "18:00",
        places = 4,
        prix_place=3000
    )

    
    assert trajet.conducteur
    assert trajet.ville_depart
    assert trajet.ville_arrive
    assert trajet.date_depart
    assert trajet.heure_depart
    assert trajet.places
    assert trajet.prix_place

def test_trajet_propose_au_moin_une_place(db):

    with pytest.raises(BaseException):
    
        trajet = Trajet.objects.create(
            conducteur ="dieudonné",
            ville_depart = "Sokodé",
            ville_arrive = "Lomé",
            date_depart = "2026-10-17",
            heure_depart = "18:00",
            places = 0,
            prix_place=3000
        )

        trajet.clean_fields()

def test_affichage_d_un_trajet(db):

    trajet = Trajet.objects.create(
        conducteur ="dieudonné",
        ville_depart = "Sokodé",
        ville_arrive = "Lomé",
        date_depart = "2026-10-17",
        heure_depart = "18:00",
        places = 0,
        prix_place=3000
    ) 

    assert str(trajet) == "Sokodé -> Lomé, le 2026-10-17 à 18:00"

