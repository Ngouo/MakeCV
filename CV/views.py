from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Profile
from django.template.loader import get_template
import io
import pdfkit

# Create your views here.

def accueil(request):
  return render(request, 'Resume.html')

def form(request):
  if request.method == 'POST':
    noms = request.POST.get("noms")
    email = request.POST.get("email")
    adresse = request.POST.get("adresse")
    contact = request.POST.get("contact")
    objectif = request.POST.get("objectif")
    tech_skills = request.POST.get("tech_skills")
    exp_pro = request.POST.get("exp_pro")
    projets = request.POST.get("projets")
    soft_skills = request.POST.get("soft_skills")
    education = request.POST.get("education")
    langue = request.POST.get("langue")
    donnees = Profile(noms=noms, email=email, adresse=adresse, contact=contact, tech_skills=tech_skills, soft_skills=soft_skills, langue=langue, projets=projets, education=education, exp_pro=exp_pro, objectif=objectif)
    donnees.save()
    return redirect("verification")
  return render (request, 'form.html')


def verification(request):
  profiles = Profile.objects.all()[:1]
  for profile in profiles:
    noms = profile.noms
    contact = profile.contact
    email = profile.email
    objectif = profile.objectif
    tech_skills = profile.tech_skills
    soft_skills = profile.soft_skills
    education = profile.education
    adresse = profile.adresse
    exp_pro = profile.exp_pro
    langue = profile.langue
    projets = profile.projets
  return render(request, 'verification.html',{'noms':noms, 'email':email, 'contact':contact,'exp_pro':exp_pro, "adresse":adresse, 'tech_skills':tech_skills, 'soft_skills':soft_skills, 'objectif':objectif, 'education':education, 'projets':projets, 'langue':langue})


def generate(request, id):
  profile = Profile.objects.get(pk=id)
  noms = profile.noms
  contact = profile.contact
  email = profile.email
  objectif = profile.objectif                         #fonction pour generer un pdf à partir d'un template et le rendre téléchargeable
  tech_skills = profile.tech_skills
  soft_skills = profile.soft_skills
  education = profile.education
  adresse = profile.adresse
  exp_pro = profile.exp_pro
  langue = profile.langue
  projets = profile.projets
  
  template = get_template('generate.html')
  context = {'noms':noms, 'email':email, 'contact':contact,'exp_pro':exp_pro, "adresse":adresse, 'tech_skills':tech_skills, 'soft_skills':soft_skills, 'objectif':objectif, 'education':education, 'projets':projets, 'langue':langue}
  html = template.render(context)         #ici on récupere les informations qu'on souhaite afficher et on les transmet dans le template avec "context"
  options = {
    'page-size': 'Letter',
    'encoding': 'UTF-8',
    "enable-local-file-access": ''
  }
  config =pdfkit.configuration(wkhtmltopdf= r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')   #toujours renseigner le chemin d'acces a wkhtmltopdf
  pdf = pdfkit.from_string(html, False ,options,configuration=config)                              #instruction pour configurer le template 
  reponse = HttpResponse(pdf, content_type='application/pdf')
  reponse["Content-Disposition"] = 'attachement'
  return reponse


def download(request):
  profile = Profile.objects.all()
  return render(request, 'download.html', {'profile':profile})


def infos(request):
  return render(request, 'infos.html')