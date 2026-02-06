# Script para desbloquear acceso al admin

echo "=== Desbloqueo de Admin - Django Axes ==="
echo ""
echo "Opciones:"
echo "1. Desbloquear TODO (resetear todos los bloqueos)"
echo "2. Desbloquear por nombre de usuario"
echo "3. Desbloquear por IP"
echo "4. Ver intentos bloqueados"
echo ""
read -p "Selecciona una opción (1-4): " opcion

cd /var/www/yogaganesha

case $opcion in
    1)
        echo "Desbloqueando todos los accesos..."
        docker compose exec -T web python manage.py axes_reset
        echo "✅ Todos los bloqueos han sido eliminados"
        ;;
    2)
        read -p "Introduce el nombre de usuario: " username
        docker compose exec -T web python manage.py axes_reset_username $username
        echo "✅ Usuario '$username' desbloqueado"
        ;;
    3)
        read -p "Introduce la IP: " ip
        docker compose exec -T web python manage.py axes_reset_ip $ip
        echo "✅ IP '$ip' desbloqueada"
        ;;
    4)
        echo "Intentos bloqueados:"
        docker compose exec -T web python manage.py axes_list_attempts
        ;;
    *)
        echo "Opción no válida"
        ;;
esac
