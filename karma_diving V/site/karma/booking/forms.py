from django.contrib.auth import get_user_model
from booking.models import Client
from django.contrib.auth.forms import UserCreationForm
from django import forms


class ClientForm(forms.ModelForm):

    class Meta():
        model = Client
        fields = ('prenom','nom_famille','date_birth','email_adresse','depart_date','arrivee_date')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['prenom'].label = 'yoshi client name'
        self.fields['nom_famille'].label = 'yoshi nom de famille here'
