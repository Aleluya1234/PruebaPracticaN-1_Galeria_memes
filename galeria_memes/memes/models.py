"""
Modelo · Meme

Cada meme guarda la URL de la imagen (no el archivo), igual que en el
proyecto de la galería de fotos, y además una categoría para practicar
un campo con choices.
"""
from django.conf import settings
from django.db import models
from django.urls import reverse


class Meme(models.Model):
    class Categoria(models.TextChoices):
        ANIMALES = "animales", "Animales"
        GAMING = "gaming", "Gaming"
        SERIES = "series", "Series y películas"
        RANDOM = "random", "Random"

    titulo = models.CharField("título", max_length=100)
    url_imagen = models.URLField(
        "URL de la imagen",
        max_length=500,
        help_text="Dirección web de la imagen, ej: https://i.imgflip.com/xxxx.jpg",
    )
    categoria = models.CharField(
        "categoría",
        max_length=20,
        choices=Categoria.choices,
        default=Categoria.RANDOM,
    )
    descripcion = models.TextField("descripción", blank=True)
    publicado = models.BooleanField(default=True)
    # Quién subió el meme. Se completa solo desde la vista (request.user).
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="memes",
    )
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creado"]
        verbose_name = "meme"
        verbose_name_plural = "memes"

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("meme_detail", kwargs={"pk": self.pk})
