from django.urls import path
from . import views
urlpatterns= [
    path("",views.liste_employe, name="liste_employe"),
    path("ajouter/", views.ajouter_employe ,  name="ajouter_employe"),
    path("modifier/<int:id>/", views.modifier_employe, name="modifier_employe"),
    path("suprimer/<int:id>",views.suprimer_employe , name="suprimer_employe"),
]