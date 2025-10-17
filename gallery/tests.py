from django.test import TestCase
from django.template import Template, Context
from django.core.files.uploadedfile import SimpleUploadedFile
from gallery.forms import MediaForm
from gallery.models import Category

class MediaFormTest(TestCase):
    def test_mediaform_valid_with_image_and_crispy_render(self):
        # create a category for the FK
        category = Category.objects.create(name="Test Category", list_position=1)

        # minimal 1x1 PNG bytes
        png_bytes = (
            b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'
            b'\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89'
            b'\x00\x00\x00\nIDATx\x9cc`\x00\x00\x00\x02\x00\x01\xe2!\xbc3'
            b'\x00\x00\x00\x00IEND\xaeB`\x82'
        )
        uploaded = SimpleUploadedFile("test.png", png_bytes, content_type="image/png")

        data = {
            "title": "Test Media",
            "alt_text": "An alt text",
            "category": category.pk,
        }

        form = MediaForm(data=data, files={"image": uploaded})
        self.assertTrue(form.is_valid(), msg=form.errors)

        tpl = Template("{% load crispy_forms_tags %}{% crispy form %}")
        rendered = tpl.render(Context({"form": form}))
        self.assertIn('name="title"', rendered)