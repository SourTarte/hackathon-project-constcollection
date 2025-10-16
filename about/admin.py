from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import AboutSection

# Register your models here.


@admin.register(AboutSection)
class MediaAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = (
        'id',
        'section_name',
        'created_on'
    )
    search_fields = ['section_name',]
    list_filter = ('created_on',)
    summernote_fields = ('section_information',)