#!/usr/bin/env python
"""
Script para poblar la base de datos con datos iniciales de Yoga Ganesha
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yogaganesha.settings')
django.setup()

from apps.core.models import BusinessSettings
from apps.instructors.models import Instructor
from apps.classes.models import YogaClass, ClassCategory
from apps.blog.models import PricingPlan, Testimonial, BlogPost
from django.contrib.auth.models import User

def populate():
    print("🚀 Poblando base de datos...")
    
    # 1. BusinessSettings
    print("\n📋 Configurando BusinessSettings...")
    settings = BusinessSettings.load()
    settings.business_name = "Yoga Ganesha"
    settings.phone = "+34 123 456 789"
    settings.email = "info@yogaganesha.com"
    settings.address = "Villena, Alicante, España"
    settings.schedule = "8:00 - 20:00"
    settings.facebook_url = "https://www.facebook.com/yogaghanesa.villena.9/?locale=es_ES"
    settings.instagram_url = "https://www.instagram.com/yogaganeshavillena/"
    settings.whatsapp_number = "+34123456789"
    settings.hero_title = "Cambia Tu Vida Con Yoga y Meditación"
    settings.hero_subtitle = "El yoga es una gran práctica tanto para el cuerpo como para la mente, ofrece paz y conciencia plena a sus amantes y les ayuda a superar el estrés diario."
    settings.about_title = "Bienvenido a Yoga Ganesha"
    settings.about_text = "El verdadero yoga no se trata de la forma de tu cuerpo, sino de la forma de tu vida. El yoga no es para ser realizado, el yoga es para ser vivido. Al yoga no le importa lo que has sido, al yoga le importa la persona en la que te estás convirtiendo."
    settings.save()
    print("✅ BusinessSettings configurado")
    
    # 2. Instructores
    print("\n👥 Creando instructores...")
    instructors_data = [
        {
            'name': 'Patricia',
            'slug': 'patricia',
            'bio': 'Instructora certificada con más de 10 años de experiencia en Yoga Iyengar y Hatha.',
            'specialization': 'Yoga Iyengar',
            'order': 1,
            'photo': 'teacher-1.png'
        },
        {
            'name': 'Lucía',
            'slug': 'lucia',
            'bio': 'Experta en Vinyasa Flow y meditación mindfulness.',
            'specialization': 'Vinyasa Yoga',
            'order': 2,
            'photo': 'teacher-2.png'
        },
        {
            'name': 'Pepe',
            'slug': 'pepe',
            'bio': 'Instructor de Ashtanga Yoga con formación en India.',
            'specialization': 'Ashtanga Yoga',
            'order': 3,
            'photo': 'teacher-3.png'
        },
        {
            'name': 'Jorge',
            'slug': 'jorge',
            'bio': 'Especialista en Kundalini Yoga y técnicas de respiración.',
            'specialization': 'Kundalini Yoga',
            'order': 4,
            'photo': 'teacher-4.png'
        },
    ]
    
    all_instructors = []
    for data in instructors_data:
        instructor, created = Instructor.objects.get_or_create(
            slug=data['slug'],
            defaults=data
        )
        # Update photo if it was created or exists but has no photo
        if not instructor.photo:
            instructor.photo = data.get('photo')
            instructor.save()
            
        all_instructors.append(instructor)
        if created:
            print(f"  ✅ Creado: {instructor.name}")
        else:
            print(f"  ℹ️  Ya existe: {instructor.name}")
    
    # 3. Categorías de Clases
    print("\n🏷️ Creando categorías de clases...")
    categories_data = [
        {'name': 'Pilates', 'slug': 'pilates', 'order': 1},
        {'name': 'Hatha', 'slug': 'hatha', 'order': 2},
        {'name': 'Vinyasa', 'slug': 'vinyasa', 'order': 3},
        {'name': 'Iyengar', 'slug': 'iyengar', 'order': 4},
        {'name': 'Ashtanga', 'slug': 'ashtanga', 'order': 5},
        {'name': 'Kundalini', 'slug': 'kundalini', 'order': 6},
        {'name': 'Yin', 'slug': 'yin', 'order': 7},
    ]
    
    categories = {}
    for data in categories_data:
        cat, created = ClassCategory.objects.get_or_create(
            slug=data['slug'],
            defaults=data
        )
        categories[data['slug']] = cat
        if created:
            print(f"  ✅ Creada: {cat.name}")
        else:
            print(f"  ℹ️  Ya existe: {cat.name}")

    # 4. Clases de Yoga
    print("\n🧘 Creando clases de yoga...")
    
    # Helpers for mapping slug to instructor object list
    # Patricia (0), Lucia (1), Pepe (2), Jorge (3)
    
    classes_data = [
        {
            'name': 'Yoga Iyengar',
            'slug': 'yoga-iyengar',
            'description': 'Enfoque en la alineación precisa y el uso de props para perfeccionar las posturas.',
            'category': categories['iyengar'],
            'schedule_days': 'Lun, Mié, Vie',
            'schedule_time': '9:00 - 10:00',
            'instructors_to_add': [all_instructors[0]] if len(all_instructors) > 0 else [],
            'order': 1
        },
        {
            'name': 'Yoga Ashtanga Vinyasa',
            'slug': 'yoga-ashtanga-vinyasa',
            'description': 'Práctica dinámica que sincroniza respiración y movimiento en secuencias fluidas.',
            'category': categories['ashtanga'],
            'schedule_days': 'Mar, Jue',
            'schedule_time': '10:00 - 11:30',
            'instructors_to_add': [all_instructors[2]] if len(all_instructors) > 2 else [],
            'order': 2
        },
        {
            'name': 'Yoga Vinyasa',
            'slug': 'yoga-vinyasa',
            'description': 'Flujo creativo de posturas coordinadas con la respiración.',
            'category': categories['vinyasa'],
            'schedule_days': 'Lun, Mié, Vie',
            'schedule_time': '18:00 - 19:00',
            'instructors_to_add': [all_instructors[1]] if len(all_instructors) > 1 else [],
            'order': 3
        },
        {
            'name': 'Yoga Yin',
            'slug': 'yoga-yin',
            'description': 'Práctica suave y meditativa con posturas mantenidas por largos períodos.',
            'category': categories['yin'],
            'schedule_days': 'Sáb',
            'schedule_time': '10:00 - 11:30',
            'instructors_to_add': [all_instructors[1]] if len(all_instructors) > 1 else [],
            'order': 4
        },
        {
            'name': 'Yoga Kundalini',
            'slug': 'yoga-kundalini',
            'description': 'Combinación de posturas, respiración, mantras y meditación para despertar la energía.',
            'category': categories['kundalini'],
            'schedule_days': 'Mar, Jue',
            'schedule_time': '19:00 - 20:30',
            'instructors_to_add': [all_instructors[3]] if len(all_instructors) > 3 else [],
            'order': 5
        },
        {
            'name': 'Yoga Hatha',
            'slug': 'yoga-hatha',
            'description': 'Práctica tradicional que equilibra cuerpo y mente a través de asanas y pranayama.',
            'category': categories['hatha'],
            'schedule_days': 'Lun, Mié, Vie',
            'schedule_time': '17:00 - 18:00',
            'instructors_to_add': [all_instructors[0]] if len(all_instructors) > 0 else [],
            'order': 6
        },
        # Adding Pilates for completeness based on categories
        {
            'name': 'Pilates Mat',
            'slug': 'pilates-mat',
            'description': 'Fortalecimiento del core y mejora de la postura con ejercicios de suelo.',
            'category': categories['pilates'],
            'schedule_days': 'Mar, Jue',
            'schedule_time': '9:00 - 10:00',
            'instructors_to_add': [all_instructors[0]] if len(all_instructors) > 0 else [],
            'order': 7
        },
    ]
    
    for data in classes_data:
        # Extract instructors list before creating object
        instructors_list = data.pop('instructors_to_add')
        
        yoga_class, created = YogaClass.objects.get_or_create(
            slug=data['slug'],
            defaults=data
        )
        
        # Always update instructors just in case
        if instructors_list:
            yoga_class.instructors.set(instructors_list)
            
        if created:
            print(f"  ✅ Creada: {yoga_class.name}")
        else:
            print(f"  ℹ️  Ya existe: {yoga_class.name}")
    
    # 5. Planes de Precios
    print("\n💰 Creando planes de precios...")
    pricing_data = [
        {
            'name': 'Básico',
            'price': 49.00,
            'period': 'mes',
            'features': 'Acceso a clases grupales\\n4 clases al mes\\nAsesoramiento básico\\nMaterial incluido',
            'is_popular': False,
            'order': 1
        },
        {
            'name': 'Estándar',
            'price': 89.00,
            'period': 'mes',
            'features': 'Acceso ilimitado a clases\\nClases especiales\\nAsesoramiento personalizado\\nMaterial premium\\nDescuentos en talleres',
            'is_popular': True,
            'order': 2
        },
        {
            'name': 'Premium',
            'price': 129.00,
            'period': 'mes',
            'features': 'Todo lo del plan Estándar\\nClases privadas (2/mes)\\nPlan nutricional\\nAcceso a retiros\\nPrioridad en reservas',
            'is_popular': False,
            'order': 3
        },
    ]
    
    for data in pricing_data:
        plan, created = PricingPlan.objects.get_or_create(
            name=data['name'],
            defaults=data
        )
        if created:
            print(f"  ✅ Creado: {plan.name}")
        else:
            print(f"  ℹ️  Ya existe: {plan.name}")
    
    # 6. Testimonios
    print("\n💬 Creando testimonios...")
    testimonials_data = [
        {
            'client_name': 'María García',
            'profession': 'Profesora',
            'testimonial_text': 'Yoga Ganesha ha transformado mi vida. La práctica diaria me ha ayudado a encontrar paz interior y mejorar mi flexibilidad. ¡Los instructores son increíbles!',
            'rating': 5,
            'order': 1
        },
        {
            'client_name': 'Carlos Martínez',
            'profession': 'Ingeniero',
            'testimonial_text': 'Después de años de estrés laboral, el yoga me ha dado las herramientas para manejar la ansiedad. El ambiente en Yoga Ganesha es perfecto para desconectar.',
            'rating': 5,
            'order': 2
        },
        {
            'client_name': 'Ana López',
            'profession': 'Diseñadora',
            'testimonial_text': 'Las clases de Vinyasa son mi favoritas. La energía y profesionalismo de los instructores hacen que cada sesión sea única y transformadora.',
            'rating': 5,
            'order': 3
        },
    ]
    
    for data in testimonials_data:
        testimonial, created = Testimonial.objects.get_or_create(
            client_name=data['client_name'],
            defaults=data
        )
        if created:
            print(f"  ✅ Creado: {testimonial.client_name}")
        else:
            print(f"  ℹ️  Ya existe: {testimonial.client_name}")
    
    # 7. Posts del Blog
    print("\n📝 Creando posts del blog...")
    try:
        admin_user = User.objects.get(username='admin')
    except User.DoesNotExist:
        print("  ⚠️  Usuario admin no encontrado, creando...")
        admin_user = User.objects.create_superuser('admin', 'admin@yogaganesha.com', 'admin123')
    
    blog_posts_data = [
        {
            'title': 'Beneficios del Yoga para la Salud Mental',
            'slug': 'beneficios-yoga-salud-mental',
            'excerpt': 'Descubre cómo la práctica regular de yoga puede mejorar tu bienestar emocional y reducir el estrés.',
            'content': 'El yoga es mucho más que ejercicio físico. Es una práctica holística que integra cuerpo, mente y espíritu. Estudios científicos han demostrado que la práctica regular de yoga puede reducir significativamente los niveles de estrés, ansiedad y depresión...',
            'category': 'Salud Mental',
            'author': admin_user
        },
        {
            'title': 'Posturas de Yoga para Principiantes',
            'slug': 'posturas-yoga-principiantes',
            'excerpt': 'Guía completa de las posturas básicas de yoga perfectas para comenzar tu práctica.',
            'content': 'Si estás comenzando en el mundo del yoga, es importante empezar con posturas básicas que te ayuden a construir fuerza, flexibilidad y conciencia corporal. Aquí te presentamos las posturas fundamentales...',
            'category': 'Principiantes',
            'author': admin_user
        },
        {
            'title': 'La Importancia de la Respiración en Yoga',
            'slug': 'importancia-respiracion-yoga',
            'excerpt': 'Aprende técnicas de respiración (pranayama) que transformarán tu práctica de yoga.',
            'content': 'La respiración es el puente entre el cuerpo y la mente. En yoga, el pranayama (control de la respiración) es fundamental para profundizar la práctica y obtener todos sus beneficios...',
            'category': 'Técnicas',
            'author': admin_user
        },
    ]
    
    for data in blog_posts_data:
        post, created = BlogPost.objects.get_or_create(
            slug=data['slug'],
            defaults=data
        )
        if created:
            print(f"  ✅ Creado: {post.title}")
        else:
            print(f"  ℹ️  Ya existe: {post.title}")
    
    print("\n✨ ¡Base de datos poblada exitosamente!")
    print("\n📊 Resumen:")
    print(f"  - Instructores: {Instructor.objects.count()}")
    print(f"  - Categorías: {ClassCategory.objects.count()}")
    print(f"  - Clases: {YogaClass.objects.count()}")
    print(f"  - Planes de Precios: {PricingPlan.objects.count()}")
    print(f"  - Testimonios: {Testimonial.objects.count()}")
    print(f"  - Posts del Blog: {BlogPost.objects.count()}")

if __name__ == '__main__':
    populate()
