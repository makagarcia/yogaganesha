from django.db import models


class YogaClass(models.Model):
    """Clases de Yoga disponibles"""
    
    CATEGORY_CHOICES = [
        ('pilates', 'Pilates Yoga'),
        ('hatha', 'Hatha Yoga'),
        ('vinyasa', 'Vinyasa Yoga'),
        ('iyengar', 'Iyengar Yoga'),
        ('ashtanga', 'Ashtanga Yoga'),
        ('kundalini', 'Kundalini Yoga'),
        ('yin', 'Yin Yoga'),
        ('bikram', 'Bikram Yoga'),
    ]
    
    name = models.CharField('Nombre', max_length=200)
    slug = models.SlugField('Slug', unique=True)
    description = models.TextField('Descripción')
    category = models.CharField('Categoría', max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField('Imagen', upload_to='classes/', blank=True, null=True)
    instructor = models.ForeignKey('instructors.Instructor', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Instructor')
    schedule_days = models.CharField('Días', max_length=100, help_text='Ej: Lun, Mié, Vie')
    schedule_time = models.CharField('Horario', max_length=50, help_text='Ej: 9:00 - 10:00')
    is_active = models.BooleanField('Activa', default=True)
    order = models.IntegerField('Orden', default=0)
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado', auto_now=True)
    
    class Meta:
        verbose_name = 'Clase de Yoga'
        verbose_name_plural = 'Clases de Yoga'
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name
