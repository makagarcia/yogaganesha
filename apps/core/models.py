from django.db import models


class BusinessSettings(models.Model):
    """Configuración general del negocio"""
    business_name = models.CharField('Nombre del Negocio', max_length=200, default='Yoga Ganesha')
    phone = models.CharField('Teléfono', max_length=20, default='+34 123 456 789')
    email = models.EmailField('Email', default='info@yogaganesha.com')
    address = models.TextField('Dirección', default='Villena, Alicante, España')
    schedule = models.CharField('Horario', max_length=100, default='Lun - Vie: 8:00 - 20:00')
    
    # Redes sociales
    facebook_url = models.URLField('Facebook', blank=True, default='https://www.facebook.com/yogaghanesa.villena.9/?locale=es_ES')
    instagram_url = models.URLField('Instagram', blank=True, default='https://www.instagram.com/yogaganeshavillena/')
    twitter_url = models.URLField('Twitter', blank=True, default='')
    whatsapp_number = models.CharField('WhatsApp', max_length=20, blank=True, default='+34123456789')
    
    # Notificaciones por email
    notification_email = models.EmailField('Email para Notificaciones', blank=True, 
                                          help_text='Email donde recibirás las notificaciones de contacto',
                                          default='info@yogaganesha.com')
    send_email_notifications = models.BooleanField('Enviar Notificaciones por Email', default=False,
                                                   help_text='Activar para recibir emails cuando alguien use el formulario de contacto')
    
    # Textos principales
    hero_title = models.CharField('Título Principal', max_length=200, default='Cambia Tu Vida Con Yoga y Meditación')
    hero_subtitle = models.TextField('Subtítulo Principal', default='El yoga es una gran práctica tanto para el cuerpo como para la mente.')
    about_title = models.CharField('Título Sobre Nosotros', max_length=200, default='Sobre Nosotros')
    about_text = models.TextField('Texto Sobre Nosotros', default='Bienvenido a Yoga Ganesha')
    
    class Meta:
        verbose_name = 'Configuración del Negocio'
        verbose_name_plural = 'Configuración del Negocio'
    
    def __str__(self):
        return self.business_name
    
    def save(self, *args, **kwargs):
        # Asegurar que solo haya una instancia
        self.pk = 1
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        # Prevenir eliminación
        pass
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Gallery(models.Model):
    """Galería de imágenes y videos"""
    
    MEDIA_TYPE_CHOICES = [
        ('image', 'Imagen'),
        ('video', 'Video de YouTube'),
    ]
    
    title = models.CharField('Título', max_length=200)
    media_type = models.CharField('Tipo', max_length=10, choices=MEDIA_TYPE_CHOICES, default='image')
    
    # Para imágenes
    image = models.ImageField('Imagen', upload_to='gallery/', blank=True, null=True, 
                             help_text='Sube una imagen desde tu dispositivo')
    
    # Para videos de YouTube
    youtube_url = models.URLField('URL de YouTube', blank=True, 
                                  help_text='Ej: https://www.youtube.com/watch?v=VIDEO_ID')
    
    description = models.TextField('Descripción', blank=True)
    is_active = models.BooleanField('Activo', default=True)
    order = models.IntegerField('Orden', default=0)
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Elemento de Galería'
        verbose_name_plural = 'Galería'
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return f'{self.title} ({self.get_media_type_display()})'
    
    def get_youtube_embed_url(self):
        """Convierte URL de YouTube a formato embed usando youtube-nocookie.com"""
        if self.youtube_url:
            # Extraer video ID de diferentes formatos de URL
            video_id = None
            
            if 'youtube.com/watch?v=' in self.youtube_url:
                video_id = self.youtube_url.split('watch?v=')[1].split('&')[0]
            elif 'youtu.be/' in self.youtube_url:
                video_id = self.youtube_url.split('youtu.be/')[1].split('?')[0]
            elif 'youtube.com/embed/' in self.youtube_url:
                video_id = self.youtube_url.split('embed/')[1].split('?')[0]
            
            if video_id:
                # Usar youtube-nocookie.com para evitar Error 153
                return f'https://www.youtube-nocookie.com/embed/{video_id}'
        
        return self.youtube_url
    
    def get_youtube_video_id(self):
        """Extrae el ID del video de YouTube"""
        if self.youtube_url:
            if 'youtube.com/watch?v=' in self.youtube_url:
                return self.youtube_url.split('watch?v=')[1].split('&')[0]
            elif 'youtu.be/' in self.youtube_url:
                return self.youtube_url.split('youtu.be/')[1].split('?')[0]
            elif 'youtube.com/embed/' in self.youtube_url:
                return self.youtube_url.split('embed/')[1].split('?')[0]
        return None
    
    def get_youtube_thumbnail(self):
        """Obtiene la URL de la miniatura del video de YouTube"""
        video_id = self.get_youtube_video_id()
        if video_id:
            # Usar la miniatura de máxima calidad
            return f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'
        return None
