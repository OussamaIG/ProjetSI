
from tokenize import group
from django.http import request
from django.shortcuts import render , redirect
from django.template import context
from .models import *
from .forms import *
from django.db.models import Q 

def homePage(request):
    etudiants = Etudiant.objects.all()
    labels = []
    data = []
    paliers = Palier.objects.all()
    for palierr in paliers:
        labels.append(palierr.libelle)
        data.append(Stage.objects.filter(palier = palierr).count())
    
    second_labels = []
    second_data = []
    entreprises = Entreprise.objects.all()
    for entreprise in entreprises:
        second_labels.append(entreprise.nom)
        stages = Stage.objects.all()
        all_paliers = Palier.objects.all()
        stages_count = stages.filter(Q(fourni_par = entreprise)).filter(palier = all_paliers.get(code_stage = 2)).count()
        second_data.append(stages_count)

    stages = Stage.objects.all()
    promoteurs = Promoteur.objects.all()


    third_labels = []
    third_data = []

    for entreprise in entreprises:
        third_labels.append(entreprise.nom)
        entreprise_groups = Groupe.objects.filter(entreprise = entreprise)
        count = etudiants.filter(groupe__in = entreprise_groups).count()
        third_data.append(count)

    fourth_labels = []
    fourth_data = []
    annees = DateStage.objects.all()
    for annee in annees:
        fourth_labels.append(str(annee.annee))
        entreprises_count = Entreprise.objects.filter(groupe__stage__palier__libelle = 'PFE').filter(groupe__stage__annee_stage = annee).distinct().count()
        fourth_data.append(entreprises_count)
    
    print(fourth_labels)
    print(fourth_data)
    context = {'etudiants' : etudiants , 'labels' : labels , 'data' : data , 'second_labels' : second_labels
         , 'second_data' : second_data , 'stages' : stages , 'promoteurs' : promoteurs , 
         'third_label' : third_labels , 'third_data' : third_data , 'fourth_labels' : fourth_labels, 'fourth_data' : fourth_data,
         'entreprises' : entreprises }
    return render(request,'index.html',context)

def etudiantProfile(request,pk):
    etudiant = Etudiant.objects.get(id=int(pk))
    context = {'etudiant' : etudiant}
    return render(request,'etudiant_profile.html',context)

def entrepriseProfile(request,pk):
    annees = DateStage.objects.all()
    my_entreprise = Entreprise.objects.get(id = pk)
    nombre_encadreurs = Encadreur.objects.filter(entreprise = my_entreprise).count()
    nombre_stages = Stage.objects.filter(fourni_par = my_entreprise).count()
    labels = []
    data = [] 
    for annee in annees:
        stages_pfe = Stage.objects.filter(palier__libelle = 'PFE')
        stages_current_year = Stage.objects.filter(annee_stage =  annee)
        etudiants_count = Etudiant.objects.filter(groupe__entreprise = my_entreprise).filter(groupe__stage__in = stages_current_year).filter(groupe__stage__in = stages_pfe).count()
        labels.append(str(annee.annee))
        data.append(etudiants_count)
    
    print(labels)
    print(data)
    context = {'labels' : labels , 'data' : data, 'nombre_encadreurs' : nombre_encadreurs , 
    'nombre_stages' : nombre_stages , 'entreprise' : my_entreprise}

    return render(request , 'entreprise_profile.html' , context)

def encadreurProfile(request,pk):
    encadreur = Encadreur.objects.get(id = int(pk))
    nombre_stages_encadrees = Stage.objects.filter(groupe__encadreur = encadreur).count()
    context = {'encadreur' : encadreur , 'nb' : nombre_stages_encadrees}
    return render(request,'encadreur_profile.html',context) 

def promoteurProfile(request,pk):
    promoteur = Promoteur.objects.get(id = int(pk))
    nombre_stages_encadrees = Stage.objects.filter(groupe__promoteur = promoteur).count()
    context = {'promoteur' : promoteur , 'nb' : nombre_stages_encadrees}
    return render(request ,'promoteur_profile.html',context)

def stageProfile(request,pk):
    stage = Stage.objects.get(id = int(pk))
    context = {'stage' : stage}
    return render(request , 'stage_profile.html', context) 

def gorupeProfile(request,pk):
    groupe = Groupe.objects.get(id = int(pk))
    nb = Etudiant.objects.filter(groupe = groupe).count()
    context = {'groupe' : groupe , 'nb' : nb}
    return render(request , 'groupe_profile.html', context)

def ficheProfile(request,pk):
    fiche = FicheEvaluation.objects.get(id = int(pk))
    context = {'fiche' : fiche}
    return render(request,'fiche_profile.html',context)
    
## forms
def ajouterEtudiant(request):
    form = EtudiantForm()
    if request.method == 'GET':
       context = {'form' : form}
       return render(request , 'ajouter_etudiant.html' , context)
    elif request.method == 'POST':
         form = EtudiantForm(request.POST)
         if form.is_valid:
            form.save()
            return redirect('gestionaire')

def ajouterGroupe(request):
    form = GroupeForm()
    if request.method == 'GET':
        context = {'form' : form}
        return render(request , 'ajouter_groupe.html' , context)
    elif request.method == 'POST':
         form = GroupeForm(request.POST)
         if form.is_valid:
            form.save()
            return redirect('gestionaire')

def ajouterEntreprise(request):
    form = EntrepriseForm()
    if request.method == 'GET':
        context = {'form' : form}
        return render(request , 'ajouter_entreprise.html' , context)
    elif request.method == 'POST':
         form = EntrepriseForm(request.POST)
         if form.is_valid:
            form.save()
            return redirect('gestionaire')

def ajouterEncadreur(request):
    form = EncadreurForm()
    if request.method == 'GET':
        context = {'form' : form}
        return render(request , 'ajouter_encadreur.html' , context)
    elif request.method == 'POST':
         form = EncadreurForm(request.POST)
         if form.is_valid:
            form.save()
            return redirect('gestionaire')

def ajouterPromoteur(request):
    form = PromoteurForm()
    if request.method == 'GET':
        context = {'form' : form}
        return render(request , 'ajouter_promoteur.html' , context)
    elif request.method == 'POST':
         form = PromoteurForm(request.POST)
         if form.is_valid:
            form.save()
            return redirect('gestionaire')

def ajouterStage(request):
    form = StageForm()
    if request.method == 'GET':
        context = {'form' : form}
        return render(request , 'ajouter_stage.html' , context)
    elif request.method == 'POST':
         form = StageForm(request.POST)
         if form.is_valid:
            form.save()
            return redirect('gestionaire')

def ajouterFicheEvaluation(request):
    form = FicheEvaluationForm()
    if request.method == 'GET':
        context = {'form' : form}
        return render(request , 'ajouter_fiche_evaluation.html' , context)
    elif request.method == 'POST':
         form = FicheEvaluationForm(request.POST)
         if form.is_valid:
            form.save()
            return redirect('gestionaire')


## tables
def entreprises(request):
    entreprises = Entreprise.objects.all()
    context = {'entreprises': entreprises}
    return render(request , 'entreprises.html' , context)  

def stages(request):
    stages = Stage.objects.all()
    context = {'stages' : stages}
    return render(request , 'stages.html' , context)

def etudiants(request):
    etudiants = Etudiant.objects.all()
    context = {"etudiants": etudiants}
    return render(request , 'etudiants.html' , context)

def encadreurs(request):
    encadreurs = Encadreur.objects.all()
    context = {'encadreurs' : encadreurs}
    return render(request , 'encadreurs.html' , context)  

def promoteurs(request):
    promoteurs = Promoteur.objects.all()
    context = {'promoteurs' : promoteurs}
    return render(request,'promoteurs.html',context)

def fichesEvaluation(request):
    fiches = FicheEvaluation.objects.all()
    context = {'fiches' : fiches}
    return render(request,'fiches_evaluation.html',context)

def groupes(request):
    groupes = Groupe.objects.all()
    context = {'groupes' : groupes}
    return render(request , 'groupes.html' , context)

def gestionaire(request):
    return render(request , 'gestionaire.html')


def preStatistiques(request):
    annees = DateStage.objects.all()
    context = {'annees' : annees}
    return render(request,'liste_statistiques.html',context)

def statistiques(request,annee):
    entreprises = Entreprise.objects.all()
    current_year = DateStage.objects.get(annee = annee)
    print(current_year)
    ## PFE/ENTREPRISE
    first_labels = []
    first_data = []
    stages = Stage.objects.all()
    all_paliers = Palier.objects.all()  
    for entreprise in entreprises:
        first_labels.append(entreprise.nom)
        stages_count = stages.filter(fourni_par = entreprise).filter(palier = all_paliers.get(code_stage = 2)).filter(annee_stage = current_year).count() 
        first_data.append(stages_count)
    
    ## STAGIAIRES/ENTREPRISES
    second_labels = []
    second_data = []

    current_year_stages = Stage.objects.filter(annee_stage = current_year)
    etudiants = Etudiant.objects.all()

    for entreprise in entreprises:
        second_labels.append(entreprise.nom)
        entreprise_groups = Groupe.objects.filter(entreprise = entreprise).filter(stage__in = current_year_stages)
        count = etudiants.filter(groupe__in = entreprise_groups).count()
        second_data.append(count)
    return render(request , 'statistiques.html')

def updateEtudiant(request,pk):
    etudiant = Etudiant.objects.get(id = int(pk))
    if request.method == 'POST':
       form = EtudiantForm(request.POST,instance=etudiant)
       if form.is_valid:
           form.save()
           return redirect('home')
    form = EtudiantForm(instance=etudiant)
    context = {'form' : form}
    return render(request , 'ajouter_etudiant.html' , context) 

def updateEntreprise(request,pk):
    entreprise = Entreprise.objects.get(id = int(pk))
    if request.method == 'POST':
       form = EntrepriseForm(request.POST,instance=entreprise)
       if form.is_valid:
           form.save()
           return redirect('home')
    form = EntrepriseForm(instance=entreprise)
    context = {'form' : form}
    return render(request , 'ajouter_entreprise.html' , context) 

def updateStage(request,pk):
    stage = Stage.objects.get(id = int(pk))
    if request.method == 'POST':
       form = StageForm(request.POST,instance=stage)
       if form.is_valid:
           form.save()
           return redirect('home')
    form = StageForm(instance=stage)
    context = {'form' : form}
    return render(request , 'ajouter_stage.html' , context)

def updateGroupe(request,pk):
    groupe = Groupe.objects.get(id = int(pk))
    if request.method == 'POST':
       form = GroupeForm(request.POST,instance=groupe)
       if form.is_valid:
           form.save()
           return redirect('home')
    form = GroupeForm(instance=group)
    context = {'form' : form}
    return render(request , 'ajouer_groupe.html' , context)

def updateEncadreur(request,pk):
    encdareur = Encadreur.objects.get(id = int(pk))
    if request.method == 'POST':
       form = EncadreurForm(request.POST,instance=encdareur)
       if form.is_valid:
           form.save()
           return redirect('home')
    form = EncadreurForm(instance=group)
    context = {'form' : form}
    return render(request , 'ajouter_encadreur.html' , context)

def updatePromoteur(request,pk):
    promoteur = Promoteur.objects.get(id = int(pk))
    if request.method == 'POST':
       form = PromoteurForm(request.POST,instance=promoteur)
       if form.is_valid:
           form.save()
           return redirect('home')
    form = PromoteurForm(instance=promoteur)
    context = {'form' : form}
    return render(request , 'ajouter_promoteur.html' , context)

def updateFicheEvaluation(request,pk):
    fiche_evaluation = FicheEvaluation.objects.all(id = int(pk))
    if request.method == 'POST':
       form = FicheEvaluationForm(request.POST,instance=fiche_evaluation)
       if form.is_valid:
           form.save()
           return redirect('home')
    form = FicheEvaluationForm(instance=fiche_evaluation)
    context = {'form' : form}
    return render(request , 'ajouter_fiche_evaluation.html' , context)

def deleteEtudiant(request,pk):
    nature = 'Etudiant'
    etudiant = Etudiant.objects.get(id = int(pk))
    if request.method == 'GET':
        context = {'nature' : nature,'etudiant' : etudiant}
        return render(request , 'delete.html',context)
    elif request.method == 'POST':
         etudiant.delete()
         return redirect('etudiants-list')

def deleteGroupe(request,pk):
    nature = 'Groupe'
    groupe = Groupe.objects.get(id = int(pk))
    if request.method == 'GET':
        context = {'nature' : nature,'groupe' : groupe}
        return render(request , 'delete.html',context)
    elif request.method == 'POST':
         groupe.delete()
         return redirect('groupes-list')

def deleteEntreprise(request,pk):
    nature = 'Entreprise'
    entreprise = Entreprise.objects.get(id = int(pk))
    if request.method == 'GET':
        context = {'nature' : nature,'entreprise' : entreprise}
        return render(request , 'delete.html',context)
    elif request.method == 'POST':
         entreprise.delete()
         return redirect('entreprises-list')

def deleteEncadreur(request,pk):
    nature = 'Encadreur'
    encadreur = Encadreur.objects.get(id = int(pk))
    if request.method == 'GET':
        context = {'nature' : nature,'encadreur' : encadreur}
        return render(request , 'delete.html',context)
    elif request.method == 'POST':
         encadreur.delete()
         return redirect('encadreurs-list')  

def deletePromoteur(request,pk):
    nature = 'Promoteur'
    promoteur = Promoteur.objects.get(id = int(pk))
    if request.method == 'GET':
        context = {'nature' : nature,'promoteur' : promoteur}
        return render(request , 'delete.html',context)
    elif request.method == 'POST':
         promoteur.delete()
         return redirect('promoteurs-list')

def deleteStage(request,pk):
    nature = 'Stage'
    stage = Stage.objects.get(id = int(pk))
    if request.method == 'GET':
        context = {'nature' : nature,'stage' : stage}
        return render(request , 'delete.html',context)
    elif request.method == 'POST':
         stage.delete()
         return redirect('stages-list')

def deleteFicheEvaluation(request,pk):
    nature = 'Fiche Evaluation'
    fiche_evaluation = FicheEvaluation.objects.get(id = int(pk))
    if request.method == 'GET':
        context = {'nature' : nature,'fiche_evaluation' : fiche_evaluation}
        return render(request , 'delete.html',context)
    elif request.method == 'POST':
         fiche_evaluation.delete()
         return redirect('fiches_evaluation-list')



