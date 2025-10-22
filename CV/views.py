from django.shortcuts import render, redirect
from .models import Profile
from .form import ProfileForm
import os
from weasyprint import HTML  # type: ignore
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='login')
def accueil(request):
  cvs = Profile.objects.filter(auteur=request.user).order_by('-id')
  first_cv = cvs.first()
  return render(request, 'CV/Resume.html', {'cvs':cvs, "first_cv": first_cv})


@login_required(login_url='login')
def form(request):
  if request.method == 'POST':
    form = ProfileForm(request.POST or None)
    if form.is_valid():
       # Stocker les données dans la session
        request.session['profile_data'] = form.cleaned_data
        return redirect('verification')
    
    else:
      print('erreur : ', ProfileForm.errors)
  else:
    form = ProfileForm()
  return render (request, 'CV/form.html', {'form':form})

@login_required(login_url='login')
def verification(request):
    profile_data = request.session.get('profile_data')
    if not profile_data:
        return redirect('form')
    
    if request.method == 'POST':
        # Ici tu peux enregistrer les données ou continuer le workflow
        Profile.objects.create(auteur=request.user, **profile_data)
        del request.session['profile_data']
        
        messages.success(request, "Ton CV a été généré et enregistré avec succès !")
        return redirect('Accueil')
    return render(request, 'CV/verification.html', {'profile_data': profile_data})


@login_required(login_url='login')
def generer_cv(request, cv_id): 
  cv = Profile.objects.get(id=cv_id, auteur=request.user)  
  print(cv)
  template = get_template('pdf_template.html')
  html_string = template.render({'cv':cv})

  CHEMIN_CV = r"C:\Users\MEN ELECTRONICS\OneDrive\Documents\CV"
  if not os.path.exists(CHEMIN_CV):
    os.makedirs(CHEMIN_CV)

  filename = f'CV - {cv.noms}.pdf'
  filepath = os.path.join(CHEMIN_CV, filename)

  HTML(string=html_string).write_pdf(filepath) 

    # Générer le PDF et l'envoyer dans le dossier indiqué dans le chemin d'accès
  return FileResponse(open(filepath, 'rb'), as_attachment=True, filename=filename)


def delete_cv(request, cv_id):
   cv = Profile.objects.get(id=cv_id)
   cv.delete()
   return redirect('Accueil')



def infos(request):
  return render(request, 'CV/infos.html')

