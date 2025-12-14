from django.contrib import admin
from .models import BlogPost, Testimonial


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published_date', 'is_published')
    list_filter = ('is_published', 'category', 'published_date')
    search_fields = ('title', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)
    
    fieldsets = (
        ('Contenido', {
            'fields': ('title', 'slug', 'excerpt', 'content', 'featured_image')
        }),
        ('Metadatos', {
            'fields': ('author', 'category', 'is_published')
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'profession', 'rating', 'is_active', 'order')
    list_filter = ('is_active', 'rating')
    search_fields = ('client_name', 'testimonial_text')
    list_editable = ('is_active', 'order')
    ordering = ('order', '-created_at')
