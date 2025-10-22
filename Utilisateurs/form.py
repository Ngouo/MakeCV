from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

    def __init__(self, *args, **kwargs):                          #cette fonction permet d'enlever toutes les ecritures qui sont sur les
        super(SignUpForm, self).__init__(*args, **kwargs)          #formulaires générés par Django
     
        for fieldname in  ['username', 'email', 'password1'] :
            self.fields[fieldname].help_text = None
