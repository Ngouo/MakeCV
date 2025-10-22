from django.urls import path
from CV.views import *


urlpatterns = [
    path('Accueil', accueil, name='Accueil'),
    path('form', form, name='form'),
    path('verification', verification, name='verification'),
    path('generer_cv/<int:cv_id>/', generer_cv, name='generer_cv'),
    path('delete_cv/<int:cv_id>/', delete_cv, name='delete_cv'),
    path('infos', infos, name='infos'),
]