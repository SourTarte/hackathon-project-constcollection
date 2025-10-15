from django.db import models
from django.db.models import PROTECT
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField


# Create your models here.


class Category(models.Model):
    """Represents an art category, e.g. 'Dualistic Art', 'Perimenopausal
        Art."""
    name = models.CharField(max_length=200)
    information = models.TextField(max_length=3000, blank=True, null=True)

    def __str__(self):
        return self.name


class Media(models.Model):
    """ Represents a piece of media - either a video or art image"""
    category = models.ForeignKey(
        Category,
        on_delete=PROTECT,
        related_name='media'
    )
    title = models.CharField(max_length=200, default="new_art")
    description = models.CharField(
        max_length=200,
        default="new_art_description"
    )
    image = CloudinaryField(blank=True, null=True, resource_type='image')
    video = models.URLField(
        blank=True,
        null=True,
        help_text="Youtube embed URL"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        if bool(self.image) == bool(self.video):
            raise ValidationError(
                (
                    "Media must have either an image or a video, "
                    "not both or neither."
                )
            )

    class Meta:
        verbose_name = "Media Item"
        verbose_name_plural = "Media Items"
        ordering = ['created_on']

    def __str__(self):
        return self.title

