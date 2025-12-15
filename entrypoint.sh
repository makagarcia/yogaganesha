#!/bin/bash

# Esperar a que PostgreSQL esté listo
echo "Esperando a PostgreSQL..."
python << END
import socket
import time
import sys

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect(('db', 5432))
        sock.close()
        break
    except:
        time.sleep(0.1)
END
echo "PostgreSQL iniciado"

# Ejecutar migraciones
echo "Ejecutando migraciones..."
python manage.py migrate --noinput

# Recolectar archivos estáticos
echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

# Crear superusuario si no existe
echo "Verificando superusuario..."
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@yogaganesha.com', 'admin123');
    print('Superusuario creado');
else:
    print('Superusuario ya existe');
"

# Ejecutar comando pasado como argumento
exec "$@"
