from django.db.models import fields
from django.forms import ModelForm
from .models import *

class EtudiantForm(ModelForm):
       class Meta:
           model = Etudiant
           fields = '__all__'
    

class StageForm(ModelForm):
       class Meta:
           model = Stage
           fields = '__all__'

class EncadreurForm(ModelForm):
       class Meta:
           model = Encadreur
           fields = '__all__'
           

class PromoteurForm(ModelForm):
       class Meta:
           model = Promoteur
           fields = ['nom' , 'prenom']

class EntrepriseForm(ModelForm):
       class Meta:
           model = Entreprise
           fields = '__all__'

class GroupeForm(ModelForm):
        class Meta:
            model = Groupe
            fields = '__all__'

class FicheEvaluationForm(ModelForm):
        class Meta:
            model = FicheEvaluation
            fields = '__all__'