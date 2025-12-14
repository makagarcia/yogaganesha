from django.db import models


class Instructor(models.Model):
    """Instructores de Yoga"""
    name = models.CharField('Nombre', max_length=200)
    slug = models.SlugField('Slug', unique=True)
    bio = models.TextField('Biografía')
    specialization = models.CharField('Especialización', max_length=200, blank=True)
    photo = models.ImageField('Foto', upload_to='instructors/', blank=True, null=True)
    
    # Redes sociales
    facebook = models.URLField('Facebook', blank=True)
    instagram = models.URLField('Instagram', blank=True)
    twitter = models.URLField('Twitter', blank=True)
    linkedin = models.URLField('LinkedIn', blank=True)
    
    order = models.IntegerField('Orden', default=0)
    is_active = models.BooleanField('Activo', default=True)
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado', auto_now=True)
    
    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructores'
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name
