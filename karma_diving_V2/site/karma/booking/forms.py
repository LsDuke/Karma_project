from django.contrib.auth import get_user_model
from booking.models import Client
from django.contrib.auth.forms import UserCreationForm
from django import forms

CHOICES = (
        ('a','yoga'),
        ('b','plongee'),
        ('c','snorkling'),
)

class ClientForm(forms.ModelForm):

    class Meta():
        model = Client

        fields = ('prenom','nom_famille','date_birth','sexe','email_adresse','arrivee_date','depart_date','produit')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['prenom'].label = 'yoshi client name'
        self.fields['nom_famille'].label = 'yoshi nom de famille here'
