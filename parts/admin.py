from django.contrib import admin
from .models import CarPart
from django.utils.html import format_html

@admin.register(CarPart)
class CarPartAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview', 'image_url')
    readonly_fields = ('image_preview', 'image_url')
    search_fields = ('name',)

    def image_preview(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" width="100" />', obj.image_url)
        return "-"
    image_preview.short_description = 'صورة'

