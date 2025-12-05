from django.shortcuts import render, redirect
from .form import SignUpForm
from django.contrib.auth import logout


# Create your views here.


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print('succes')
            return redirect('auth')            
    return render(request, 'Utilisateurs/signup.html', {'form': form})


def deconnection(request):
  logout(request)
  return render(request, 'Utilisateurs/logout.html')


def landing(request):
    return render(request, 'Utilisateurs/landing.html')


def modeles(request):
   return render(request, 'Utilisateurs/modeles.html')