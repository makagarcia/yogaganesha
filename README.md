# Yoga Ganesha - Django Website

Centro de Yoga y Meditación con gestión completa desde Django Admin.

## 🚀 Quick Start

### Desarrollo Local

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Migrar base de datos
python manage.py migrate

# Poblar datos iniciales
python populate_db.py

# Ejecutar servidor
python manage.py runserver
```

Acceder a: `http://localhost:8000`

### Producción con Docker

```bash
# 1. Configurar variables de entorno
cp .env.example .env
nano .env  # Editar con tus valores

# 2. Inicializar SSL (si tienes dominio)
./init-letsencrypt.sh

# 3. Levantar servicios
docker-compose up -d --build
```

Ver guía completa: [docker_deployment_guide.md](file:///home/p3t4/.gemini/antigravity/brain/7e9084af-076a-4a5c-aff4-ffa277cd4864/docker_deployment_guide.md)

## 📚 Documentación

- [Guía del Admin](file:///home/p3t4/.gemini/antigravity/brain/7e9084af-076a-4a5c-aff4-ffa277cd4864/guia_admin_completa.md) - Cómo gestionar contenido
- [Deployment con Docker](file:///home/p3t4/.gemini/antigravity/brain/7e9084af-076a-4a5c-aff4-ffa277cd4864/docker_deployment_guide.md) - Guía de producción
- [Guía Rápida](file:///home/p3t4/.gemini/antigravity/brain/7e9084af-076a-4a5c-aff4-ffa277cd4864/guia_rapida.md) - Comandos y URLs útiles

## ✨ Características

- ✅ Panel de administración moderno (Django Jazzmin)
- ✅ Gestión de clases de yoga
- ✅ Gestión de instructores
- ✅ Blog integrado
- ✅ Galería de imágenes y videos
- ✅ Testimonios de clientes
- ✅ Formulario de contacto
- ✅ Responsive design
- ✅ Todo editable desde el admin

## 🔐 Admin

- URL: `/admin/`
- Usuario por defecto: `admin`
- Contraseña por defecto: `admin123`

**⚠️ Cambiar contraseña en producción**

## 🛠️ Stack Tecnológico

- Django 4.2.8
- PostgreSQL 15 (producción)
- Nginx (reverse proxy)
- Gunicorn (WSGI server)
- Docker & Docker Compose
- Let's Encrypt (SSL)

## 📦 Estructura

```
├── apps/                   # Aplicaciones Django
│   ├── core/              # Configuración y galería
│   ├── classes/           # Clases de yoga
│   ├── instructors/       # Instructores
│   ├── blog/              # Blog y testimonios
│   └── contact/           # Contacto
├── templates/             # Templates Django
├── static/                # Archivos estáticos
├── nginx/                 # Configuración Nginx
├── docker-compose.yml     # Orquestación Docker
├── Dockerfile             # Imagen Docker
└── requirements.txt       # Dependencias Python
```

## 🐳 Servicios Docker

- **web**: Django + Gunicorn
- **nginx**: Reverse proxy + SSL
- **db**: PostgreSQL
- **certbot**: Certificados SSL automáticos

## 📝 Licencia

Proyecto privado - Yoga Ganesha
