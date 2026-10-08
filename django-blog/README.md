# Portfolio personal + Blog con Django

Este proyecto es un sitio personal desarrollado con Django que combina un portfolio profesional con un blog de publicaciones.

## Descripción

El sitio incluye:
- una presentación personal con información sobre el autor,
- una sección de proyectos,
- un blog con entradas ordenadas cronológicamente,
- comentarios en cada entrada,
- gestión de contenido desde Django Admin,
- una identidad visual coherente con el portfolio.

## Requisitos

- Python 3.11+
- Django 5.x
- SQLite (incluido por defecto con Django)

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd django-blog
   ```

2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   ```

3. Activar el entorno virtual:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

4. Instalar dependencias:
   ```bash
   pip install django
   ```

5. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```

6. Crear un superusuario para Django Admin:
   ```bash
   python manage.py createsuperuser
   ```

7. Ejecutar el proyecto:
   ```bash
   python manage.py runserver
   ```

8. Abrir en el navegador:
   ```text
   http://127.0.0.1:8000/
   ```

## Acceso de administración

Para crear nuevas entradas, categorías y gestionar comentarios:

```text
http://127.0.0.1:8000/admin/
```

Solo el administrador puede crear nuevas publicaciones. Los comentarios los puede administrar el admin y eliminarlos desde el panel.

## Estructura del proyecto

- `blog/`: aplicación principal del blog.
- `portfolio/`: recursos y templates del portfolio.
- `personal_blog/`: configuración del proyecto Django.
- `media/`: archivos subidos por el usuario.
- `db.sqlite3`: base de datos local.

## Bitácora

La bitácora personal del proyecto se puede consultar en `bitacora.md`.

## Observaciones

Este trabajo permite combinar un portfolio personal con un blog funcional, manteniendo una estética coherente y un flujo de administración simple con Django Admin.
