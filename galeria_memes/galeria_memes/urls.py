"""
URLs del proyecto.

  /admin/              Django Admin
  /                     la galería de memes (memes/urls.py)
  /accounts/login/      login y logout que Django trae listos
  /accounts/registro/   registro sencillo con UserCreationForm
"""
from django.contrib import admin
from django.urls import include, path

from memes.views import registro

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("memes.urls")),
    path("accounts/registro/", registro, name="registro"),
    path("accounts/", include("django.contrib.auth.urls")),
]
