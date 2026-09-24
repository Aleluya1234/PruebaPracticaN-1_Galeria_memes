import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='título')),
                ('url_imagen', models.URLField(help_text='Dirección web de la imagen, ej: https://i.imgflip.com/xxxx.jpg', max_length=500, verbose_name='URL de la imagen')),
                ('categoria', models.CharField(choices=[('animales', 'Animales'), ('gaming', 'Gaming'), ('series', 'Series y películas'), ('random', 'Random')], default='random', max_length=20, verbose_name='categoría')),
                ('descripcion', models.TextField(blank=True, verbose_name='descripción')),
                ('publicado', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'meme',
                'verbose_name_plural': 'memes',
                'ordering': ['-creado'],
            },
        ),
    ]
