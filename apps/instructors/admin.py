from django.contrib import admin
from .models import Instructor


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('name', 'bio', 'specialization')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active', 'order')
    ordering = ('order', 'name')
    
    fieldsets = (
        ('Información General', {
            'fields': ('name', 'slug', 'specialization', 'bio', 'photo')
        }),
        ('Redes Sociales', {
            'fields': ('facebook', 'instagram', 'twitter', 'linkedin'),
            'classes': ('collapse',)
        }),
        ('Configuración', {
            'fields': ('order', 'is_active')
        }),
    )
