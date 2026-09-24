# Cómo correr la Galería de Memes en GitHub Codespaces

## 1. Crea el repositorio en GitHub

Crea un repo nuevo llamado (por ejemplo) `PruebaPracticaN1_Galeria_memes`
y sube ahí TODO el contenido de esta carpeta (no la carpeta contenedora,
sino lo que hay adentro: manage.py, requirements.txt, galeria_memes/, memes/, etc.,
todo directamente en la raíz del repo).

## 2. Abre un Codespace

Botón verde **Code** → pestaña **Codespaces** → **Create codespace on main**.

## 3. En la terminal del Codespace

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py poblar
python manage.py runserver 0.0.0.0:8000
```

`poblar` crea el usuario **profe** / **inacap2026** y varios memes de ejemplo.
Si prefieres tu propio usuario: `python manage.py createsuperuser`.

## 4. Abre la app

Ve a la pestaña **PORTS**, busca el puerto 8000 y haz clic en el ícono del
navegador. O si VS Code también te abrió `localhost:8000`, usa esa URL.

| Qué | Dirección |
|---|---|
| Galería | / |
| Ver un meme | /1/ |
| Nuevo meme (pide login) | /nueva/ |
| Editar / borrar (piden login) | /1/editar/ · /1/borrar/ |
| Login | /accounts/login/ |
| Registro | /accounts/registro/ |
| Django Admin | /admin/ |

## 5. Tests

```bash
python manage.py test
```

## Problemas frecuentes

| Síntoma | Solución |
|---|---|
| CSRF verification failed | Ya está resuelto de fábrica: `settings.py` trae `CSRF_TRUSTED_ORIGINS`, `SECURE_PROXY_SSL_HEADER` y `USE_X_FORWARDED_HOST` listos para Codespaces y para `localhost:8000`. |
| ModuleNotFoundError: No module named 'galeria_memes' | Estás parado en la carpeta equivocada. Ejecuta `ls`, debe aparecer manage.py; si no, `cd` a la carpeta correcta. |
| No such table | Falta `python manage.py migrate`. |
