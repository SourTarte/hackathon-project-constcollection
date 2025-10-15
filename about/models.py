from django.db import models
from gallery.models import Media
# Create your models here.


class AboutSection(models.Model):
    """
    Represents an informational section about the artist, such as Bio,
    Exhibitions, or Press. Each section can contain descriptive text and
    be linked to multiple media items.
    """
    section_name = models.CharField(
        max_length=200,
        help_text=(
            "Name of the about section "
            "(e.g. Bio, Exhibitions)"
        )
    )
    section_information = models.TextField(max_length=3000)
    media = models.ManyToManyField(Media, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ('section_name',)

    def __str__(self):
        return self.section_name
