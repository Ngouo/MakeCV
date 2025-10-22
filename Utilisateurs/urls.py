from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', signup, name="signup"),
    path('', landing, name='landing'),
    path('modeles', modeles, name='modeles'),
    path('auth', auth_views.LoginView.as_view(template_name='Utilisateurs/login.html'), name='auth'),
    path('logout', deconnection, name='logout'),
]