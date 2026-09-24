from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .forms import MemeForm
from .models import Meme

URL = "https://i.imgflip.com/1bij.jpg"


class ModeloYForm(TestCase):
    def test_crud_con_el_orm(self):
        m = Meme(titulo="Uno", url_imagen=URL); m.save()
        Meme.objects.create(titulo="Dos", url_imagen=URL, publicado=False)
        self.assertEqual(Meme.objects.count(), 2)
        m.titulo = "Uno editado"; m.save()
        self.assertEqual(Meme.objects.get(id=m.id).titulo, "Uno editado")
        m.delete()
        self.assertEqual(Meme.objects.count(), 1)

    def test_form_rechaza_url_no_https(self):
        form = MemeForm({"titulo": "Mal", "url_imagen": "http://inseguro.cl/f.jpg"})
        self.assertFalse(form.is_valid())
        self.assertIn("url_imagen", form.errors)


class VistasGenericas(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user("ana", password="clave123")
        self.meme = Meme.objects.create(titulo="Publicado", url_imagen=URL, autor=self.user)
        Meme.objects.create(titulo="Oculto", url_imagen=URL, publicado=False)

    def test_list_muestra_solo_publicados(self):
        r = self.client.get(reverse("meme_list"))
        self.assertContains(r, "Publicado")
        self.assertNotContains(r, "Oculto")

    def test_create_update_delete_logueado(self):
        self.client.login(username="ana", password="clave123")
        r = self.client.post(reverse("meme_create"), {
            "titulo": "Nuevo", "url_imagen": URL, "categoria": "random", "publicado": True,
        })
        self.assertRedirects(r, reverse("meme_list"))
        nuevo = Meme.objects.get(titulo="Nuevo")
        self.assertEqual(nuevo.autor, self.user)

        r = self.client.post(reverse("meme_delete", args=[nuevo.pk]))
        self.assertRedirects(r, reverse("meme_list"))
        self.assertFalse(Meme.objects.filter(pk=nuevo.pk).exists())


class Seguridad(TestCase):
    def setUp(self):
        self.meme = Meme.objects.create(titulo="Publicado", url_imagen=URL)

    def test_sin_login_redirige_a_login(self):
        login = reverse("login")
        for nombre, args in [("meme_create", []), ("meme_update", [self.meme.pk]), ("meme_delete", [self.meme.pk])]:
            url = reverse(nombre, args=args)
            r = self.client.get(url)
            self.assertRedirects(r, f"{login}?next={url}", msg_prefix=nombre)

    def test_post_sin_csrf_da_403(self):
        cliente = self.client_class(enforce_csrf_checks=True)
        get_user_model().objects.create_user("ana", password="clave123")
        cliente.login(username="ana", password="clave123")
        r = cliente.post(reverse("meme_create"), {"titulo": "X", "url_imagen": URL})
        self.assertEqual(r.status_code, 403)
