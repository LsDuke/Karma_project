from django.db import models
from django.core.urlresolvers import reverse
#Create your models here.
class Produit(models.Model):
    titre = models.CharField(max_length=256)
    categorie = models.CharField(max_length=256)
    prix = models.PositiveIntegerField()
    prix_special = models.PositiveIntegerField()
    nbr_place = models.PositiveIntegerField()

    def __str__(self):
        return self.titre

class Client(models.Model):
    prenom = models.CharField(max_length=256)
    nom_famille = models.CharField(max_length=256)
    date_birth = models.DateField()
    sexe = models.CharField(max_length=256)
    nationalite = models.CharField(max_length=256)
    email_adresse = models.CharField(max_length=256)
    facebook = models.CharField(max_length=256)
    arrivee_date = models.DateField()
    depart_date = models.DateField()
    produit = models.ManyToManyField(Produit)

    def __str__(self):
        return self.prenom + ' ' + self.nom_famille


    def get_absolute_url(self):
        return reverse('booking:thanks')
