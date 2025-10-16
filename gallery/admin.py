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
        'title',
        'created_on'
    )
    search_fields = ['title', 'subtitle',]
    list_filter = ('created_on',)
    summernote_fields = ('description',)

admin.site.register(Category)
