"""
Carga datos de ejemplo:

    python manage.py poblar

Crea el usuario `profe` (clave `inacap2026`) si no existe y varios memes
de ejemplo con imágenes públicas.
"""
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from memes.models import Meme

MEMES = [
    ("Lunes otra vez", "gaming", "https://i.imgflip.com/1bij.jpg", "Cuando suena la alarma un lunes."),
    ("Cuando el código sí funciona", "random", "https://i.imgflip.com/26am.jpg", "Nadie sabe por qué, pero funciona."),
    ("Gato jefe", "animales", "https://i.imgflip.com/1ur9b0.jpg", "El verdadero dueño de la oficina."),
    ("Final de temporada", "series", "https://i.imgflip.com/2fm6x.jpg", "Esperando el próximo capítulo."),
    ("Debug a las 3am", "gaming", "https://i.imgflip.com/4t0m5.jpg", "console.log everywhere."),
    ("Perro sorprendido", "animales", "https://i.imgflip.com/39t1o.jpg", "Reacción al ver la boleta de luz."),
]


class Command(BaseCommand):
    help = "Crea un usuario de prueba y memes de ejemplo"

    def handle(self, *args, **options):
        User = get_user_model()
        profe, creado = User.objects.get_or_create(username="profe")
        if creado:
            profe.set_password("inacap2026")
            profe.is_staff = True
            profe.is_superuser = True
            profe.save()
            self.stdout.write("Usuario creado: profe / inacap2026")

        nuevos = 0
        for titulo, categoria, url, descripcion in MEMES:
            if Meme.objects.filter(titulo=titulo).exists():
                continue
            Meme.objects.create(
                titulo=titulo,
                categoria=categoria,
                url_imagen=url,
                descripcion=descripcion,
                autor=profe,
            )
            nuevos += 1
        self.stdout.write(self.style.SUCCESS(f"{nuevos} memes nuevos · {Meme.objects.count()} en total"))
