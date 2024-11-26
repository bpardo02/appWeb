from django.shortcuts import render, get_object_or_404, redirect
from .models import Inmueble
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomAuthenticationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login
from .forms import InmuebleForm, EditProfileForm
from django.core.exceptions import PermissionDenied
from django.contrib import messages


def lista_inmuebles(request):
    inmuebles = Inmueble.objects.all()
    return render(request, "lista_inmuebles.html", {"inmuebles": inmuebles})


def detalle_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    return render(request, "detalle_inmueble.html", {"inmueble": inmueble})


def index(request):
    return render(request, "index.html")


class CustomLoginView(LoginView):
    template_name = "login.html"
    form_class = CustomAuthenticationForm
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")


def registro_usuario(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    return render(request, "registro.html", {"form": form})


@login_required
def actualizar_usuario(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("perfil")
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, "actualizar_usuario.html", {"form": form})


@login_required
def perfil_usuario(request):
    return render(request, "perfil.html", {"usuario": request.user})


def registro_usuario_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "registro.html", {"form": form})


@login_required
def publicar_inmueble(request):
    if request.user.tipo_usuario != "arrendatario":
        messages.error(request, "Solo los arrendatarios pueden publicar inmuebles.")
        raise PermissionDenied

    if request.method == "POST":
        form = InmuebleForm(request.POST, request.FILES)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.save()
            messages.success(request, "¡Inmueble publicado exitosamente!")
            return redirect("lista_inmuebles")
        else:
            messages.error(request, "Hubo un error al publicar el inmueble.")
    else:
        form = InmuebleForm()
    return render(request, "publicar_inmueble.html", {"form": form})


def custom_permission_denied_view(request, exception=None):
    return render(request, "403.html", status=403)


@login_required
def profile_view(request):
    return render(request, "profile.html", {"user": request.user})


@login_required
def edit_profile_view(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado con éxito.")
            return redirect("profile")
        else:
            messages.error(request, "Por favor corrige los errores indicados.")
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, "edit_profile.html", {"form": form})
