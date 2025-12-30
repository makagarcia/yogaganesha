from django.db import models


class ClassCategory(models.Model):
    """Categorías de clases de yoga (ej: Hatha, Pilates, Vinyasa)"""
    name = models.CharField('Nombre', max_length=100)
    slug = models.SlugField('Slug', unique=True)
    description = models.TextField('Descripción', blank=True)
    order = models.IntegerField('Orden', default=0)
    
    class Meta:
        verbose_name = 'Disciplina / Categoría'
        verbose_name_plural = 'Disciplinas / Categorías'
        ordering = ['order', 'name']
        
    def __str__(self):
        return self.name


class YogaClass(models.Model):
    """Clases de Yoga disponibles"""
    
    name = models.CharField('Nombre', max_length=200)
    slug = models.SlugField('Slug', unique=True)
    description = models.TextField('Descripción')
    
    # Changed from CharField/Choices to ForeignKey
    category = models.ForeignKey(ClassCategory, on_delete=models.CASCADE, verbose_name='Disciplina/Categoría', related_name='classes')
    
    image = models.ImageField('Imagen', upload_to='classes/', blank=True, null=True)
    
    # Changed from ForeignKey to ManyToManyField
    instructors = models.ManyToManyField('instructors.Instructor', verbose_name='Instructores', related_name='classes', blank=True)
    
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
