from django.contrib import admin
from .models import BusinessSettings, Gallery


@admin.register(BusinessSettings)
class BusinessSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información General', {
            'fields': ('business_name', 'phone', 'email', 'address', 'schedule')
        }),
        ('Redes Sociales', {
            'fields': ('facebook_url', 'instagram_url', 'twitter_url', 'whatsapp_number')
        }),
        ('Notificaciones por Email', {
            'fields': ('notification_email', 'send_email_notifications'),
            'description': 'Configura el email donde recibirás notificaciones del formulario de contacto'
        }),
        ('Textos Principales', {
            'fields': ('hero_title', 'hero_subtitle', 'about_title', 'about_text')
        }),
    )
    
    def has_add_permission(self, request):
        # Solo permitir una instancia
        return not BusinessSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # No permitir eliminar
        return False


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'is_active', 'order', 'created_at')
    list_filter = ('media_type', 'is_active')
    search_fields = ('title', 'description')
    list_editable = ('is_active', 'order')
    ordering = ('order', '-created_at')
    
    fieldsets = (
        ('Información General', {
            'fields': ('title', 'media_type', 'description')
        }),
        ('Contenido', {
            'fields': ('image', 'youtube_url'),
            'description': 'Sube una imagen O ingresa una URL de YouTube (no ambas)'
        }),
        ('Configuración', {
            'fields': ('is_active', 'order')
        }),
    )
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Ayuda contextual
        form.base_fields['image'].help_text = 'Sube una imagen desde tu dispositivo (JPG, PNG, etc.)'
        form.base_fields['youtube_url'].help_text = 'Pega la URL completa del video de YouTube. Ej: https://www.youtube.com/watch?v=abc123'
        return form
