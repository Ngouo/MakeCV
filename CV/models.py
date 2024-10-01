from django.db import models

# Create your models here.

class Profile(models.Model):
  noms = models.CharField(max_length=500)
  email = models.EmailField(max_length=254)
  adresse = models.CharField(max_length=50)
  contact = models.BigIntegerField()
  objectif = models.TextField()
  tech_skills = models.TextField()
  exp_pro = models.TextField()
  projets = models.TextField()
  soft_skills = models.TextField()
  education = models.TextField()
  langue = models.CharField( max_length=150)
  date_ajout = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.noms
  
  class Meta:
    ordering = ["-date_ajout"]
