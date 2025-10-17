from django import forms
from .models import Category, Media


class CategoryForm(forms.ModelForm):
    """
    Form class for Admins to submit new sections
    """

    class Meta:
        model = Category
        fields = ['name', 'information', 'list_position',]

class MediaForm(forms.ModelForm):
    """
    Form class for Admins to submit new media files
    """

    class Meta:
        model = Media
        fields = ['title', 'alt_text', 'image', 'video', 'category']