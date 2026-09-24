"""
Vistas de la galería de memes.

  · vista de FUNCIÓN con ModelForm (patrón GET/POST) para crear_meme
  · las 5 vistas GENÉRICAS del CRUD
  · seguridad: @login_required / LoginRequiredMixin
"""
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import MemeForm
from .models import Meme


# ── Vista de función con ModelForm ───────────────────────────────────────────
@login_required
def crear_meme(request):
    if request.method == "POST":
        form = MemeForm(request.POST)
        if form.is_valid():
            meme = form.save(commit=False)
            meme.autor = request.user
            meme.save()
            return redirect("meme_list")
    else:
        form = MemeForm()
    return render(request, "memes/meme_form.html", {"form": form})


# ── Vistas genéricas ──────────────────────────────────────────────────────────
class MemeList(ListView):
    """READ (varios). Solo memes publicados; ordenados por Meta.ordering."""
    model = Meme
    paginate_by = 12

    def get_queryset(self):
        return Meme.objects.filter(publicado=True)


class MemeDetail(DetailView):
    """READ (uno)."""
    model = Meme


class MemeCreate(LoginRequiredMixin, CreateView):
    """CREATE."""
    model = Meme
    form_class = MemeForm
    success_url = reverse_lazy("meme_list")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class MemeUpdate(LoginRequiredMixin, UpdateView):
    """UPDATE. Mismo template y form que Create."""
    model = Meme
    form_class = MemeForm


class MemeDelete(LoginRequiredMixin, DeleteView):
    """DELETE. GET muestra la confirmación, POST borra."""
    model = Meme
    success_url = reverse_lazy("meme_list")


# ── Registro de usuarios ──────────────────────────────────────────────────────
def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("meme_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/registro.html", {"form": form})
