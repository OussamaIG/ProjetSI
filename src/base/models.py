from tkinter.tix import Tree
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields.related import ForeignKey

class Entreprise(models.Model):
      nom = models.CharField(max_length=40)
      
      def __str__(self):
          return self.nom

class Groupe(models.Model):
       nom = models.CharField(max_length=40 , null=True)
       stage = models.OneToOneField('Stage' , on_delete= SET_NULL , null = True)
       encadreur = models.ForeignKey('Encadreur' , on_delete = SET_NULL , null = True)
       promoteur = models.ForeignKey('Promoteur', on_delete = SET_NULL , null = True)
       entreprise = models.ForeignKey(Entreprise , on_delete=SET_NULL , null=True)

       def __str__(self):
           return self.nom

class Etudiant(models.Model):
      nom = models.CharField(max_length=40)
      prenom = models.CharField(max_length=40)
      niveau = models.IntegerField()
      groupe = models.ForeignKey('Groupe' , on_delete=SET_NULL , null=True)


      def __str__(self):
          return self.nom + " " + self.prenom

class Palier(models.Model):
      code_stage = models.IntegerField(null=True)
      libelle = models.CharField(max_length=40)

      def __str__(self):
          return self.libelle

class Stage(models.Model):
      intitule = models.CharField(max_length=200)
      duree = models.IntegerField() # jours
      date_debut = models.DateField()
      date_fin = models.DateField()
      annee_stage = models.ForeignKey('DateStage' , on_delete = SET_NULL , null = True)
      palier = models.ForeignKey(Palier , on_delete= SET_NULL , null=True)
      fourni_par = models.ForeignKey(Entreprise , on_delete = SET_NULL , null=True)
      

      def __str__(self):
          return self.intitule

class DateStage(models.Model):
      annee = models.IntegerField(null = True)

      def __str__(self):
          return str(self.annee)


class Encadreur(models.Model):
      nom = models.CharField(max_length=40)
      prenom = models.CharField(max_length=40)
      entreprise = models.ForeignKey(Entreprise , on_delete=models.CASCADE)

      def __str__(self):
          return self.nom + " " + self.prenom

class Promoteur(models.Model):
      nom = models.CharField(max_length=40)
      prenom = models.CharField(max_length=40)
      encadreurs = models.ManyToManyField(Encadreur,through='FicheEvaluation')

      def __str__(self):
          return self.nom + " " + self.prenom

class FicheEvaluation(models.Model):
      groupe = models.ForeignKey(Groupe , on_delete = SET_NULL , null=True)
      promoteur = models.ForeignKey(Promoteur , on_delete = SET_NULL , null = True)
      encadreur = models.ForeignKey(Encadreur , on_delete = SET_NULL , null = True)
      promoteur_note = models.IntegerField()
      encadreur_note = models.IntegerField()

