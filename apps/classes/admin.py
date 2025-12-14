from django.contrib import admin
from .models import YogaClass


@admin.register(YogaClass)
class YogaClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'instructor', 'schedule_days', 'schedule_time', 'is_active', 'order')
    list_filter = ('category', 'is_active', 'instructor')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active', 'order')
    ordering = ('order', 'name')
