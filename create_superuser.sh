#!/bin/bash
# Script para crear superusuario
source venv/bin/activate
python manage.py createsuperuser --username admin --email admin@yogaganesha.com
