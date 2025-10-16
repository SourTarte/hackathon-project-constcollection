from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Media, Category

# Register your models here.

@admin.register(Media)
class MediaAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = (
        'id',
        'title',
        'created_on'
    )
    search_fields = ['title',]
    list_filter = ('created_on',)
    summernote_fields = ('description',)

@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = (
        'name',
        'list_position',
        'associated_media',
    )
    search_fields = ['name',]
    summernote_fields = ('information',)
