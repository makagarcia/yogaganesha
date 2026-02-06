from django.contrib import admin
from .models import YogaClass, ClassCategory, Event


@admin.register(ClassCategory)
class ClassCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('order',)
    ordering = ('order', 'name')


@admin.register(YogaClass)
class YogaClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'get_instructors', 'schedule_days', 'schedule_time', 'is_active', 'order')
    list_filter = ('category', 'is_active', 'instructors')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active', 'order')
    ordering = ('order', 'name')
    filter_horizontal = ('instructors',)
    
    def get_instructors(self, obj):
        return ", ".join([p.name for p in obj.instructors.all()])
    get_instructors.short_description = 'Instructores'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_text', 'is_active', 'order', 'created_at')
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'subtitle')
    list_filter = ('is_active',)
    ordering = ('order', '-created_at')
