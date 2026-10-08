# Bitácora personal del proyecto

## Fecha de inicio
2026-10

## Objetivo
Crear un sitio web personal con portfolio y blog, desarrollado completamente en Django, con una estética coherente y una estructura funcional para publicaciones y comentarios.

## Dificultades encontradas

### 1. Unificar estilo del portfolio y del blog
El primer problema fue que el blog tenía un estilo base muy genérico y no coincidía con la identidad visual del portfolio. Se resolvió conectando el blog a la misma hoja de estilos del portfolio y ajustando las plantillas para mantener colores, tipografías y estructura visual coherentes.

### 2. Archivos multimedia en los posts
El modelo de Post contemplaba imagen y video, pero no se estaban mostrando de forma adecuada en la vista de detalle. Se corrigió incorporando renderizado de imagen y video en la plantilla de cada entrada.

### 3. Comentarios y administración
Se necesitaba que los comentarios fueran agregados desde la vista del post y administrados por el administrador. El problema fue dejarlo funcional sin crear un sistema de usuarios complejo. Se resolvió usando campos simples en el modelo de Comentario y gestionando todo desde Django Admin.

### 4. Estructura de archivos estáticos
La hoja de estilo del portfolio no cargaba correctamente porque estaba en una ruta que Django no servía como static. Se corrigió moviendo los archivos a la carpeta `static` adecuada y dejando la configuración de `STATICFILES_DIRS` correcta.

## Soluciones aplicadas
- Diseño visual uniforme para portfolio y blog.
- Uso de modelos `Post`, `Category` y `Comment` con relación adecuada.
- Vistas para listado de posts y detalle de cada publicación.
- Uso de Django Admin para crear posts y eliminar comentarios.
- Configuración correcta de archivos estáticos para que el CSS funcione.

## Qué haría distinto
- Implementaría autenticación de usuarios para comentarios con más control.
- Agregaría validación más estricta de permisos para publicaciones y comentarios.
- Mejoraría la estructura de vistas para separar mejor portfolio y blog si el proyecto creciera.

## Pendientes
- Revisar detalles de UX en pantallas pequeñas.
- Completar contenido real de publicaciones para darle una temática más sólida al blog.
- Considerar una versión del blog con más secciones, por ejemplo: categorías, buscador o filtros.
