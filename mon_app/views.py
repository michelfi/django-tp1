# TP 1 · Deux sortes de vues dans le même fichier :
# - vues classiques → HttpResponse → du HTML (une page web)
# - vue API (DRF)   → @api_view + Response → du JSON (des données)
from django.http import HttpResponse  # réponse HTML / texte (Django pur)
from django.shortcuts import render

from rest_framework.decorators import api_view  # transforme une fonction en vue API
from rest_framework.response import Response    # dict Python → JSON + Browsable API


# Create your views here.
# Vue classique : reçoit la requête, renvoie du HTML. Pas de décorateur.
def home(request):  # route « / »
    return HttpResponse("<h1>Bienvenue sur la page d'accueil !</h1>")


def about(request):  # route « /about/ »
    return HttpResponse("<h1>Ceci est une page à propos.</h1>")


def contact(request):  # route « /contact/ »
    return HttpResponse("<h1>Voici la page de contact.</h1>")

# Vue API : le décorateur se colle juste au-dessus de SA fonction.
# ["GET"] = n'accepte que la lecture ; un POST renverrait 405.
@api_view(["GET"])
def help_page(request):  # route « /help/ »
    donnees = {"email": "contact@monprojet.com", "telephone": "0123456789"}
    # Response convertit le dictionnaire en JSON (statut 200 OK par défaut).
    return Response(donnees)
