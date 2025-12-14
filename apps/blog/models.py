from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class BlogPost(models.Model):
    """Posts del Blog"""
    title = models.CharField('Título', max_length=200)
    slug = models.SlugField('Slug', unique=True)
    content = models.TextField('Contenido')
    excerpt = models.TextField('Extracto', max_length=300, help_text='Resumen breve del post')
    featured_image = models.ImageField('Imagen Destacada', upload_to='blog/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    category = models.CharField('Categoría', max_length=100, default='General')
    published_date = models.DateTimeField('Fecha de Publicación', auto_now_add=True)
    is_published = models.BooleanField('Publicado', default=True)
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado', auto_now=True)
    
    class Meta:
        verbose_name = 'Post del Blog'
        verbose_name_plural = 'Posts del Blog'
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """Testimonios de clientes"""
    client_name = models.CharField('Nombre del Cliente', max_length=200)
    profession = models.CharField('Profesión', max_length=200, blank=True)
    photo = models.ImageField('Foto', upload_to='testimonials/', blank=True, null=True)
    testimonial_text = models.TextField('Testimonio')
    rating = models.IntegerField('Calificación', default=5, help_text='De 1 a 5 estrellas')
    is_active = models.BooleanField('Activo', default=True)
    order = models.IntegerField('Orden', default=0)
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Testimonio'
        verbose_name_plural = 'Testimonios'
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return f'{self.client_name} - {self.rating}★'


class PricingPlan(models.Model):
    """Planes de Precios"""
    name = models.CharField('Nombre del Plan', max_length=100)
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    period = models.CharField('Período', max_length=50, default='mes', help_text='Ej: mes, año')
    description = models.TextField('Descripción', blank=True)
    features = models.TextField('Características', help_text='Una característica por línea')
    is_popular = models.BooleanField('Plan Popular', default=False)
    is_active = models.BooleanField('Activo', default=True)
    order = models.IntegerField('Orden', default=0)
    
    class Meta:
        verbose_name = 'Plan de Precios'
        verbose_name_plural = 'Planes de Precios'
        ordering = ['order']
    
    def __str__(self):
        return f'{self.name} - €{self.price}/{self.period}'
    
    def get_features_list(self):
        """Retorna las características como lista"""
        return [f.strip() for f in self.features.split('\n') if f.strip()]
