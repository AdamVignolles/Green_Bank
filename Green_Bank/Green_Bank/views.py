from django.http import HttpResponse
from django.shortcuts import render
from .use_data import *
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):

    data_vehicule = get_json(f"{BASE_DIR}/Green_Bank/data/donnee_vehicule.json")
    data_bancaire = get_json(f"{BASE_DIR}/Green_Bank/data/donnee_bancaires.json")


    context = {
        "hide_vehicule" : "show",
        "hide_resultat" : "hide",
        "kilometrage1" : "5-10",
        "kilometrage2" : "10-15",
        "kilometrage3" : "15-20",
        "kilometrage4" : "20-25",
        "kilometrage5" : "25-30",
        "annee1" : "2010",
        "annee2" : "2000-2010",
        "annee3" : "1990-2000",
        "annee4" : "1970-1980",
        "annee5" : "1960-1970",
    }

    if request.method == 'GET':

        try :
            donnees = request.GET.dict()["liste_choix"]

            l_donnees = donnees.split(",")

            # On récupère les données du formulaire dans un dictionnaire
            donnees = {}
            for i in l_donnees:
                i = i.replace("}", "")
                i = i.replace("{", "")
                i = i.replace("'", "")
                i = i.replace(" ", "")
                i = i.replace('"', "")
                i = i.split(":")
                donnees[i[0]] = i[1]
            
            car = donnees["car"]
            energie = donnees["energie"]
            kilometrage = donnees["kilometrage"]
            annee = donnees["annee"]
            passager = donnees["passager"].replace("passager", "")

            
            note = 0.0
            
            note += data_vehicule["type_de_vehicule"][car]["note_eco"]
            note += data_vehicule["energie"][energie]
            note += data_vehicule["kilometrage"][kilometrage]
            note += data_vehicule["annee"][annee]


            taux_d_emprunt = data_bancaire["taux_d_emprunt"]
            for tau in taux_d_emprunt:
                tau_split = tau.split("-")
                if int(tau_split[0]) <= note <= int(tau_split[1]):
                    taux = taux_d_emprunt[tau]

            data_passager = data_bancaire["passagers"][str(passager)]

            if data_passager[0] == "+":
                taux += float(data_passager[1:])
            else:
                taux -= float(data_passager[1:])

        
            context["hide_vehicule"] = "hide"
            context["hide_resultat"] = "show"
            context["resultat"] = "Le Taux de votre emprunt sera de  " + str(taux) + "%"
            
        except Exception as e:
            print("error")  
            print(e)

    return render(request, 'index.html' , context=context)
