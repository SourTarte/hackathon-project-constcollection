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

    def clean(self):
        cleaned = super().clean()
        image = cleaned.get('image')
        video = cleaned.get('video')

        # Temporary debug logging to inspect values/types and uploaded files
        # Remove or replace with proper logging once you finish debugging.
        print("DEBUG MediaForm.clean called (id={}):".format(id(self)))
        print("  image repr:", repr(image), "type:", type(image), "truthy:", bool(image))
        print("  video repr:", repr(video), "type:", type(video), "truthy:", bool(video))
        try:
            files_keys = list(self.files.keys())
        except Exception as e:
            files_keys = f"<error getting files: {e}>"
        print("  self.files keys:", files_keys)

        # Require exactly one of image or video
        if not image and not video:
            raise forms.ValidationError("Please provide either an image or a video.")
        if image and video:
            raise forms.ValidationError("Please provide only one of image or video.")

        return cleaned