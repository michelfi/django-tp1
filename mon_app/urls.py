# Les routes de l'APP. Inclus par mon_projet/urls.py → URL finale = « » + chemin d'ici.
from django.urls import path  # path(chemin, vue, name=…)

from . import views  # « . » = ce dossier → mon_app/views.py

urlpatterns = [
    path("", views.home, name="home"),             # /
    path("about/", views.about, name="about"),     # /about/
    path("contact/", views.contact, name="contact"),
    path("help/", views.help_page, name="help"),  # /help/ → JSON (DRF)
]