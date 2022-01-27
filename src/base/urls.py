from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.homePage , name ="home"),
    ## profiles
    path('etudiant/<str:pk>/',views.etudiantProfile,name="etudiant-profile"),
    path('entreprise/<str:pk>/',views.entrepriseProfile,name="entreprise-profile"),
    path('encadreur/<str:pk>/',views.encadreurProfile,name="encadreur-profile"),
    path('promoteur/<str:pk>/',views.promoteurProfile,name="promoteur-profile"),
    path('stage/<str:pk>/',views.stageProfile,name="stage-profile"),
    path('groupe/<str:pk>/',views.stageProfile,name="groupe-profile"),
    path('fiche-evaluation/<str:pk>/',views.ficheProfile,name="fiche-profile"),
    ## page gestionnaire
    path('gestionaire/',views.gestionaire, name="gestionaire"),
    ## forms (create)
    path('ajouter-etudiant/',views.ajouterEtudiant,name="ajouter-etudiant"),
    path('ajouter-encadreur/',views.ajouterEncadreur,name="ajouter-encadreur"),
    path('ajouter-entreprise/',views.ajouterEntreprise,name="ajouter-entreprise"),
    path('ajouter-promoteur/',views.ajouterPromoteur,name="ajouter-Promoteur"),
    path('ajouter-stage/',views.ajouterStage,name="ajouter-stage"),
    path('ajouter-groupe/',views.ajouterGroupe,name="ajouter-groupe"),
    path('ajouter-fiche-evaluation/',views.ajouterFicheEvaluation,name="ajouter-FicheEvaluation"),
    ## tables
    path('entreprises/',views.entreprises,name="entreprises-list"),
    path('stages/',views.stages,name="stages-list"),
    path('encadreurs/',views.encadreurs,name="encadreurs-list"),
    path('etudiants/',views.etudiants,name="etudiants-list"),
    path('promoteurs/',views.promoteurs,name="promoteurs-list"),
    path('fiches-evaluations/',views.fichesEvaluation,name="fiches-evaluation-list"),
    path('groupes/',views.groupes,name="groupes-list"),
    ## update
    path('etudiant/update-etudiant/<str:pk>/',views.updateEtudiant,name="update-etudiant"),
    path('entreprise/update-entreprise/<str:pk>/',views.updateEntreprise,name="update-entreprise"),
    path('stage/update-stage/<str:pk>/',views.updateStage,name="update-stage"),
    path('promoteur/update-promoteur/<str:pk>/',views.updatePromoteur,name="update-promoteur"),
    path('encadreur/update-encadreur/<str:pk>/',views.updateEncadreur,name="update-encadreur"),
    path('groupe/update-gorupe/<str:pk>/',views.updateGroupe,name="update-groupe"),
    path('fiche-evaluation/update-fiche-evaluation/<str:pk>/',views.updateFicheEvaluation,name="update-evaluation"),
    ## liste des annees pour stats
    path('liste-statistiques/',views.preStatistiques,name="liste-statistiques"),
    path('liste-statistiques/<str:annee>',views.statistiques,name="statistiques"),
    ## delete
    path('etudiant/delete-etudiant/<str:pk>',views.deleteEtudiant,name="delete-etudiant"),
    path('entreprise/delete-entreprise/<str:pk>',views.deleteEntreprise,name="delete-entreprise"),
    path('stage/delete-stage/<str:pk>',views.deleteStage,name="delete-stage"),
    path('promoteur/delete-promoteur/<str:pk>',views.deletePromoteur,name="delete-promoteur"),
    path('encadreur/delete-encadreur/<str:pk>',views.deleteEncadreur,name="delete-encadreur"),
    path('groupe/delete-groupe/<str:pk>',views.deleteGroupe,name="delete-groupe"),
    path('fiche-evaluation/delete-fiche-evaluation/<str:pk>',views.deleteFicheEvaluation,name="delete-fiche-evaluation"),
    
]