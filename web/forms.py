from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    is_superuser = forms.BooleanField(required=False, label="¿Registrar como superusuario?")
    superuser_code = forms.CharField(
        required=False,
        widget=forms.PasswordInput,
        label="Clave de superusuario"
    )

    class Meta:
        model = User
        fields = ['username', 'email']
