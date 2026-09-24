"""
Conectar las vistas en urls.py.
"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.MemeList.as_view(), name="meme_list"),
    path("<int:pk>/", views.MemeDetail.as_view(), name="meme_detail"),
    path("nueva/", views.MemeCreate.as_view(), name="meme_create"),
    path("<int:pk>/editar/", views.MemeUpdate.as_view(), name="meme_update"),
    path("<int:pk>/borrar/", views.MemeDelete.as_view(), name="meme_delete"),

    # La misma creación pero con vista de función, para comparar.
    path("nueva/funcion/", views.crear_meme, name="meme_create_funcion"),
]
