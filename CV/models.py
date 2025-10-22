from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  auteur = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
  noms = models.CharField(max_length=500)
  email = models.EmailField(max_length=254)
  linkedin = models.URLField(unique=True, default='')
  github = models.URLField(unique=True, default='')
  contact = models.BigIntegerField()
  objectif = models.TextField()

  ecole_1 = models.CharField(max_length=255)
  diplome_1 = models.CharField(default='BACCALAUREAT', max_length=255)
  date_debut_1 = models.IntegerField(default=0)
  date_fin_1 = models.IntegerField(default=0)


  ecole_2 = models.CharField(blank=True, default='', max_length=255)
  diplome_2 = models.CharField(blank=True, default='', max_length=255)
  date_debut_2 = models.IntegerField(default=0)
  date_fin_2 = models.IntegerField(default=0)
  
  langage_pro = models.CharField(max_length=255, default='')
  frameworks = models.CharField(max_length=255, default='')
  base_donnees = models.CharField(max_length=255, default='')
  soft_skills = models.CharField(max_length=255, default='')

  poste_1 = models.CharField(default='', max_length=255)
  entreprise_1 = models.CharField(default='', max_length=255)

  date_debut_poste_1 = models.IntegerField(default=0)
  date_fin_poste_1 = models.IntegerField(default=0)

  projet_1 = models.CharField(max_length=255, default='')
  lien_1 = models.URLField(unique=True, blank=True, default='')
  description_1 = models.CharField(max_length=500, default=' ')

 

  
  def __str__(self):
    return self.noms
  
