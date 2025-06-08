from django import forms
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
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")
        is_superuser = cleaned_data.get("is_superuser")
        code = cleaned_data.get("superuser_code")

        if password != confirm:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        if is_superuser and code != "2020":
            raise forms.ValidationError("Clave de superusuario incorrecta.")
