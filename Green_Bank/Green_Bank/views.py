from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    context = {
        "hide_vehicule" : "show",
        "hide_resultat" : "hide"
    }

    if request.method == 'GET':

        donnees = request.GET.dict()["liste_choix"]

    

        print(donnees)
        print(donnees[0])
        
        car = donnees["car"]
        energie = donnees["energie"]
        kilometrage = donnees["kilometrage"]
        annee = donnees["annee"]
        passager = donnees["passager"]

        print(car)


        #context["hide_vehicule"] = "hide"
        #context["hide_resultat"] = "show"
        context["resultat"] = "Votre véhicule est éligible à la prime à la conversion !"


    return render(request, 'index.html' , context=context)