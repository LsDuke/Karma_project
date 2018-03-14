from django.db import models
from django.core.urlresolvers import reverse
from django.forms import ModelForm
#Create your models here.
SEX_CHOICES = (
    ('Male','M'),
    ('Female','F')
)


ACTIVITY_CHOICE = (
    ('Yoga','Yoga'),
    ('Pilate','Pilate'),
    ('Plongée','Plongée')
)

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
    sexe = models.CharField(max_length=10,choices=SEX_CHOICES)
    nationalite = models.CharField(max_length=256)
    email_adresse = models.CharField(max_length=256)
    facebook = models.CharField(max_length=256)
    arrivee_date = models.DateField()
    depart_date = models.DateField()
    produit = models.ForeignKey(Produit,default='null')
    # ,choices=ACTIVITY_CHOICE,default='null')
    # product = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())

    def __str__(self):
        return self.prenom + ' ' + self.nom_famille


    def get_absolute_url(self):
        return reverse('booking:thanks')
