from django.shortcuts import render
from apps.classes.models import YogaClass, ClassCategory, Event
from apps.instructors.models import Instructor
from apps.blog.models import BlogPost, Testimonial, PricingPlan
from apps.core.models import BusinessSettings, Gallery


def home(request):
    """Vista principal"""
    context = {
        'settings': BusinessSettings.load(),
        'events': Event.objects.filter(is_active=True),
        'categories': ClassCategory.objects.filter(classes__is_active=True).distinct().order_by('order'),
        'classes': YogaClass.objects.filter(is_active=True).order_by('order')[:6],
        'instructors': Instructor.objects.filter(is_active=True).order_by('order')[:4],
        'testimonials': Testimonial.objects.filter(is_active=True).order_by('order')[:4],
        'blog_posts': BlogPost.objects.filter(is_published=True)[:3],
        'pricing_plans': PricingPlan.objects.filter(is_active=True).order_by('order'),
    }
    return render(request, 'index.html', context)


def about(request):
    """Vista sobre nosotros"""
    context = {
        'settings': BusinessSettings.load(),
    }
    return render(request, 'about.html', context)


def classes_list(request):
    """Vista de clases"""
    context = {
        'settings': BusinessSettings.load(),
        'categories': ClassCategory.objects.filter(classes__is_active=True).distinct().order_by('order'),
        'classes': YogaClass.objects.filter(is_active=True).order_by('order'),
    }
    return render(request, 'class.html', context)


def team(request):
    """Vista del equipo"""
    context = {
        'settings': BusinessSettings.load(),
        'instructors': Instructor.objects.filter(is_active=True),
    }
    return render(request, 'team.html', context)


def pricing(request):
    """Vista de precios"""
    context = {
        'settings': BusinessSettings.load(),
        'pricing_plans': PricingPlan.objects.filter(is_active=True).order_by('order'),
    }
    return render(request, 'price.html', context)


def blog_list(request):
    """Vista del blog"""
    context = {
        'settings': BusinessSettings.load(),
        'posts': BlogPost.objects.filter(is_published=True),
    }
    return render(request, 'blog.html', context)


def blog_detail(request, slug):
    """Vista de post individual"""
    from django.shortcuts import get_object_or_404
    context = {
        'settings': BusinessSettings.load(),
        'post': get_object_or_404(BlogPost, slug=slug, is_published=True),
        'posts': BlogPost.objects.filter(is_published=True).exclude(slug=slug)[:3],
    }
    return render(request, 'single.html', context)


def contact(request):
    """Vista de contacto"""
    from django.contrib import messages
    from apps.contact.models import ContactMessage
    from django.core.mail import send_mail
    from django.conf import settings as django_settings
    
    business_settings = BusinessSettings.load()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Guardar en base de datos
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Enviar email si está habilitado
        if business_settings.send_email_notifications and business_settings.notification_email:
            try:
                email_subject = f'Nuevo mensaje de contacto: {subject}'
                email_body = f"""
Nuevo mensaje recibido desde el formulario de contacto:

Nombre: {name}
Email: {email}
Asunto: {subject}

Mensaje:
{message}

---
Este mensaje fue enviado desde {business_settings.business_name}
                """
                
                send_mail(
                    email_subject,
                    email_body,
                    django_settings.DEFAULT_FROM_EMAIL,
                    [business_settings.notification_email],
                    fail_silently=False,
                )
                messages.success(request, '¡Mensaje enviado correctamente! Te contactaremos pronto.')
            except Exception as e:
                # Guardar en base de datos pero mostrar advertencia
                messages.warning(request, f'Mensaje guardado, pero no se pudo enviar email: {str(e)}')
        else:
            messages.success(request, '¡Mensaje enviado correctamente! Te contactaremos pronto.')
    
    context = {
        'settings': business_settings,
    }
    return render(request, 'contact.html', context)


def gallery(request):
    """Vista de galería"""
    context = {
        'settings': BusinessSettings.load(),
        'gallery_items': Gallery.objects.filter(is_active=True),
    }
    return render(request, 'gallery.html', context)


def test_video(request):
    """Página de prueba de videos"""
    return render(request, 'test_video.html')
