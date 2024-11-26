from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Inmueble


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Usuario",
            }
        ),
        label="Usuario",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Contraseña",
            }
        ),
        label="Contraseña",
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("El campo de usuario no puede estar vacío.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not password:
            raise forms.ValidationError("El campo de contraseña no puede estar vacío.")
        return password


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "rut",
            "direccion",
            "telefono",
            "tipo_usuario",
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = field.label  # Opcional: agregar


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "direccion",
            "telefono",
            "tipo_usuario",
        ]


class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            "nombre",
            "descripcion",
            "m2_construidos",
            "m2_totales",
            "estacionamientos",
            "habitaciones",
            "banos",
            "direccion",
            "comuna",
            "region",
            "tipo_inmueble",
            "precio_mensual",
            "imagen",
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control"}),
            "m2_construidos": forms.NumberInput(attrs={"class": "form-control"}),
            "m2_totales": forms.NumberInput(attrs={"class": "form-control"}),
            "estacionamientos": forms.NumberInput(attrs={"class": "form-control"}),
            "habitaciones": forms.NumberInput(attrs={"class": "form-control"}),
            "banos": forms.NumberInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "comuna": forms.Select(attrs={"class": "form-control"}),
            "region": forms.Select(attrs={"class": "form-control"}),
            "tipo_inmueble": forms.Select(attrs={"class": "form-control"}),
            "precio_mensual": forms.NumberInput(attrs={"class": "form-control"}),
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "telefono",
            "direccion",
            "tipo_usuario",
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Apellido"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Correo Electrónico"}
            ),
            "telefono": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Teléfono"}
            ),
            "direccion": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Dirección"}
            ),
            "tipo_usuario": forms.Select(attrs={"class": "form-select"}),
        }
